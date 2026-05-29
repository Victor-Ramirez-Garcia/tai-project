#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <map>

using namespace std;

/**
 * Problem: Minimum Sum of Squared Difference
 * Strategy: Greedy Reduction of Absolute Differences
 * * To minimize sum(diff[i]^2), we should always reduce the largest absolute difference
 * because the derivative of x^2 is 2x; larger x results in a larger reduction per step.
 * Since we have k1 + k2 total operations, we can treat them as a single pool 'k'.
 */
class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int n = nums1.size();
        long long k = (long long)k1 + k2;
        
        // Step 1: Calculate absolute differences and find the maximum possible difference
        // We use a frequency map/array to avoid sorting, since values are bounded.
        // The maximum possible difference is 10^5 (max value in nums1/nums2).
        vector<int> freq(100001, 0);
        long long total_diff = 0;
        for (int i = 0; i < n; ++i) {
            int d = abs(nums1[i] - nums2[i]);
            if (d > 0) {
                freq[d]++;
                total_diff += d;
            }
        }

        // Edge case: if total operations k exceeds the sum of all differences,
        // we can make all differences zero.
        if (total_diff <= k) return 0;

        // Step 2: Iterate from the highest difference downwards to distribute 'k'
        for (int d = 100000; d > 0 && k > 0; --d) {
            if (freq[d] > 0) {
                // Number of elements with current difference 'd' we can reduce
                long long take = min((long long)freq[d], k);
                
                // Move 'take' elements from diff 'd' to diff 'd-1'
                freq[d] -= take;
                freq[d - 1] += take;
                k -= take;
            }
        }

        // Step 3: Calculate the final sum of squares
        long long result = 0;
        for (long long d = 1; d <= 100000; ++d) {
            if (freq[d] > 0) {
                result += (long long)freq[d] * d * d;
            }
        }

        return result;
    }
};

/**
 * Complexity Analysis:
 * Time Complexity: O(N + M), where N is the length of arrays and M is the max difference (10^5).
 * Space Complexity: O(M) to store the frequency of differences.
 */