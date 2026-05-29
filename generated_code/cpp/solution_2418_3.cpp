#include <vector>
#include <cmath>
#include <numeric>
#include <algorithm>
#include <map>

using namespace std;

class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int n = nums1.size();
        long long total_k = (long long)k1 + k2;
        
        // Count frequencies of absolute differences
        // Since max value of nums1[i], nums2[i] is 10^5, the max difference is 10^5.
        // A frequency array (or bucket sort approach) yields O(N + MaxDiff) time complexity.
        vector<long long> diff_count(100001, 0);
        long long sum_diff = 0;
        
        for (int i = 0; i < n; ++i) {
            int diff = abs(nums1[i] - nums2[i]);
            diff_count[diff]++;
            sum_diff += diff;
        }
        
        // If the total operations we can perform is greater than or equal to 
        // the sum of all absolute differences, we can reduce all differences to 0.
        if (total_k >= sum_diff) {
            return 0;
        }
        
        // Process differences greedily from largest to smallest
        for (int d = 100000; d > 0; --d) {
            if (diff_count[d] == 0) continue;
            
            long long count = diff_count[d];
            // If we can reduce all elements of size 'd' to size 'd - 1'
            if (total_k >= count) {
                total_k -= count;
                diff_count[d - 1] += count;
                diff_count[d] = 0;
            } else {
                // We can only partially reduce some elements of size 'd' to 'd - 1'
                diff_count[d - 1] += total_k;
                diff_count[d] -= total_k;
                total_k = 0;
                break; // No more operations left
            }
        }
        
        // Calculate the minimum sum of squared differences
        long long ans = 0;
        for (long long d = 1; d <= 100000; ++d) {
            if (diff_count[d] > 0) {
                ans += diff_count[d] * d * d;
            }
        }
        
        return ans;
    }
};