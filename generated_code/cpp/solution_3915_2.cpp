#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    long long maxProduct(vector<int>& nums) {
        // Map to store the maximum value for each unique bitmask representation.
        // Since nums[i] <= 10^6, masks will fit within a standard 20-bit integer.
        unordered_map<int, int> max_val_for_mask;
        
        for (int num : nums) {
            int mask = 0;
            int temp = num;
            // Construct the bitmask representing which bits are set in num
            while (temp > 0) {
                int bit = temp & -temp; // Get the lowest set bit
                mask |= bit;
                temp ^= bit;            // Clear the lowest set bit
            }
            // Retain only the maximum number for this specific bitmask
            max_val_for_mask[mask] = max(max_val_for_mask[mask], num);
        }
        
        long long max_product = 0;
        
        // Compare pairs of unique masks to find the maximum valid product
        for (auto it1 = max_val_for_mask.begin(); it1 != max_val_for_mask.end(); ++it1) {
            for (auto it2 = next(it1); it2 != max_val_for_mask.end(); ++it2) {
                // Check if the two masks share no common set bits
                if ((it1->first & it2->first) == 0) {
                    long long current_product = (long long)it1->second * it2->second;
                    max_product = max(max_product, current_product);
                }
            }
        }
        
        return max_product;
    }
};