#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int>& nums, int k, int limit) {
        int n = nums.size();
        
        // dp_even[j][p] stores the maximum product for a subsequence ending at an EVEN index
        // with alternating sum = j and product = p.
        // Since we want to maximize the product `p` for a specific target sum `k`,
        // and because tracking product as a DP state is inefficient or impossible due to continuous values,
        // we can instead invert the DP: find the max product directly if the constraints permit, 
        // or use standard DP if the constraints on k and nums are small.
        // Given the problem description is a placeholder without explicit numeric constraints,
        // we implement a robust 0-1 Knapsack style DP.
        
        // To handle arbitrary constraints optimally, we use a map-based or array-based DP 
        // depending on whether the alternating sum can be negative. 
        // Let's assume a standard coordinate shift or map for the alternating sum.
        // Since we want to maximize the product while keeping product <= limit,
        // we can define DP tables:
        // dp_even[sum] = max product <= limit ending at an even position of the subsequence
        // dp_odd[sum] = max product <= limit ending at an odd position of the subsequence
        
        // However, multiplying numbers can quickly exceed standard integer limits or decrease if numbers can be 0 or negative.
        // Assuming nums contains positive integers based on standard product maximization problems:
        // Initialize DP tables with -1 to signify unreachable sums.
        // We use long long internally to prevent overflow during transitions.
        
        // Since the alternating sum can be negative, we can use a map or a shifted array.
        // Let's use a dynamic approach or map for flexibility with constraints.
        // To optimize performance, we can use a flat vector with a large enough offset if we knew constraints,
        // or unordered_map. For maximum efficiency in competitive programming, we'll use an array with an offset.
        // Let's assume a reasonable maximum sum range (e.g., -2000 to 2000). If constraints are larger, 
        // unordered_map is safer. Let's use unordered_map for absolute safety across unknown constraint limits.
        
        // unordered_map<sum, max_product>
        // base case: empty subsequence has sum 0, product 1? No, subsequence must be non-empty.
        // But we can build from single elements (which are at even index 0 of the subsequence).
        
        // Instead of maps which have high overhead, let's use a shifted array assuming a reasonable max absolute sum of 10000.
        const int OFFSET = 20005; 
        const int MAX_SUM = 40010;
        
        vector<long long> dp_even(MAX_SUM, -1);
        vector<long long> dp_odd(MAX_SUM, -1);
        
        for (int num : nums) {
            // To prevent using the same element multiple times in the same step,
            // we create temporary copies or iterate backwards if it were a 1D DP.
            // Since transitions go from even->odd and odd->even, we can just compute next states.
            vector<long long> next_even = dp_even;
            vector<long long> next_odd = dp_odd;
            
            // 1. Start a new subsequence with 'num' at an even index (index 0 of the subsequence)
            if (num <= limit) {
                int next_sum = num + OFFSET;
                if (next_sum >= 0 && next_sum < MAX_SUM) {
                    next_even[next_sum] = max(next_even[next_sum], (long long)num);
                }
            }
            
            // 2. Transition from existing subsequences
            for (int s = 0; s < MAX_SUM; ++s) {
                // Transition from odd length to even length (adding to an even index: +num)
                if (dp_odd[s] != -1) {
                    long long next_prod = dp_odd[s] * num;
                    int next_sum = (s - OFFSET) + num + OFFSET;
                    if (next_prod <= limit && next_sum >= 0 && next_sum < MAX_SUM) {
                        next_even[next_sum] = max(next_even[next_sum], next_prod);
                    }
                }
                
                // Transition from even length to odd length (adding to an odd index: -num)
                if (dp_even[s] != -1) {
                    long long next_prod = dp_even[s] * num;
                    int next_sum = (s - OFFSET) - num + OFFSET;
                    if (next_prod <= limit && next_sum >= 0 && next_sum < MAX_SUM) {
                        next_odd[next_sum] = max(next_odd[next_sum], next_prod);
                    }
                }
            }
            
            dp_even = move(next_even);
            dp_odd = move(next_odd);
        }
        
        long long ans = -1;
        int target_idx = k + OFFSET;
        if (target_idx >= 0 && target_idx < MAX_SUM) {
            ans = max(dp_even[target_idx], dp_odd[target_idx]);
        }
        
        return ans;
    }
};