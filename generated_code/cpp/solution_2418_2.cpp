#include <vector>
#include <cmath>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    long long minSumSquareDiff(vector<int>& nums1, vector<int>& nums2, int k1, int k2) {
        int n = nums1.size();
        
        // Find the maximum possible difference to size our frequency bucket array.
        // Since 0 <= nums1[i], nums2[i] <= 10^5, the max difference is 10^5.
        int max_diff = 0;
        vector<int> diff_counts(100001, 0);
        
        long long total_diff = 0;
        for (int i = 0; i < n; ++i) {
            int diff = abs(nums1[i] - nums2[i]);
            if (diff > 0) {
                diff_counts[diff]++;
                if (diff > max_diff) {
                    max_diff = diff;
                }
                total_diff += diff;
            }
        }
        
        long long k = (long long)k1 + k2;
        
        // If the total operations allowed can reduce all differences to 0, return 0.
        if (k >= total_diff) {
            return 0;
        }
        
        // Process differences greedily from the largest down to 1.
        for (int d = max_diff; d > 0; --d) {
            if (diff_counts[d] == 0) continue;
            
            long long count = diff_counts[d];
            
            // If we can reduce all elements of current maximum difference 'd' to 'd - 1'
            if (k >= count) {
                k -= count;
                diff_counts[d - 1] += count;
                diff_counts[d] = 0;
            } else {
                // We can only reduce 'k' elements of difference 'd' to 'd - 1'
                diff_counts[d - 1] += k;
                diff_counts[d] -= k;
                k = 0;
                break; // No more operations left
            }
        }
        
        // Calculate the final minimum sum of squared differences.
        long long min_sum_sq = 0;
        for (long long d = 1; d <= max_diff; ++d) {
            if (diff_counts[d] > 0) {
                min_sum_sq += diff_counts[d] * d * d;
            }
        }
        
        return min_sum_sq;
    }
};