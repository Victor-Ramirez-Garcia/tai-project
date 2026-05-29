#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        // Map to store the maximum value of nums[i] for each unique bitmask
        unordered_map<int, int> mask_to_max_val;
        
        for (int num : nums) {
            int mask = 0;
            int temp = num;
            // Generate the bitmask indicating which bits are set
            while (temp > 0) {
                mask |= (temp & 1) ? (1 << (temp & 1)) : 0; // Conceptual bit tracker
                temp >>= 1;
            }
            
            // Re-evaluating standard bitmask generation based on value:
            // Since 1 <= nums[i] <= 10^6, we can just use the number's actual binary mask.
            // Wait, "binary representations of nums[i] and nums[j] do not share any common set bits"
            // means (nums[i] & nums[j]) == 0. The mask is just the number itself!
        }
        
        // Since the bitmask of a number *is* the number itself for the condition (nums[i] & nums[j]) == 0,
        // we can find unique numbers and keep the maximum value. Since all elements are unique values in a map:
        unordered_map<int, long long> unique_nums;
        for (int num : nums) {
            unique_nums[num] = max(unique_nums[num], (long long)num);
        }
        
        // To optimize, we can sort the unique numbers in descending order.
        // This allows for early pruning during the nested loop search.
        vector<long long> val_list;
        for (auto& pair : unique_nums) {
            val_list.push_back(pair.first);
        }
        sort(val_list.rbegin(), val_list.rend());
        
        long long max_prod = 0;
        int n = val_list.size();
        
        for (int i = 0; i < n; ++i) {
            // If the square of the current largest element is less than or equal to max_prod, 
            // no subsequent pairs can beat max_prod.
            if (val_list[i] * val_list[i] <= max_prod) {
                break;
            }
            for (int j = i + 1; j < n; ++j) {
                long long current_prod = val_list[i] * val_list[j];
                // Pruning: if the product is already less than or equal to max_prod, 
                // continuing with smaller val_list[j] won't yield a larger product.
                if (current_prod <= max_prod) {
                    break;
                }
                // Check if they share no common set bits
                if ((val_list[i] & val_list[j]) == 0) {
                    max_prod = current_prod;
                }
            }
        }
        
        // If no distinct pair exists with 0 shared bits, or if nums size is handled, 
        // handle edge cases where nums could have duplicates of the same number that 
        // satisfies the condition (only possible if the number is 0, but 1 <= nums[i]).
        // Since we need distinct indices i and j, and (nums[i] & nums[j]) == 0,
        // two identical numbers > 0 will always share set bits, so they can't form a valid pair.
        // Thus, reducing to unique numbers is completely valid.
        
        return max_prod;
    }
};