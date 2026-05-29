#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        // Since multiple numbers can have the same bitmask representation,
        // we only need to keep track of the maximum value for each unique bitmask.
        // This optimizes the search space significantly.
        unordered_map<int, int> max_val_for_mask;
        for (int num : nums) {
            int mask = 0;
            int temp = num;
            // Construct the bitmask representing which bits are set in the number.
            // Since nums[i] <= 10^6, it fits within 20 bits (2^20 = 1,048,576).
            for (int bit = 0; bit < 20; ++bit) {
                if ((temp >> bit) & 1) {
                    mask |= (1 << bit);
                }
            }
            max_val_for_mask[mask] = max(max_val_for_mask[mask], num);
        }

        // Convert the map to a vector of pairs for faster iteration.
        vector<pair<int, int>> mask_val_pairs;
        for (auto& p : max_val_for_mask) {
            mask_val_pairs.push_back(p);
        }

        long long max_prod = 0;
        int n = mask_val_pairs.size();

        // Compare all pairs of unique masks to find two that don't share any set bits.
        for (int i = 0; i < n; ++i) {
            int mask1 = mask_val_pairs[i].first;
            long long val1 = mask_val_pairs[i].second;
            
            for (int j = i + 1; j < n; ++j) {
                int mask2 = mask_val_pairs[j].first;
                long long val2 = mask_val_pairs[j].second;

                // If the bitwise AND is 0, they do not share any common set bits.
                if ((mask1 & mask2) == 0) {
                    max_prod = max(max_prod, val1 * val2);
                }
            }
        }

        return max_prod;
    }
};