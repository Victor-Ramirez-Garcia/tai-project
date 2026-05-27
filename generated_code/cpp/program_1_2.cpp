#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Use a hash map to store the value and its corresponding index.
        // This allows us to check for the complement in O(1) average time.
        std::unordered_map<int, int> num_to_index;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
            // If the complement exists in the map, we found the pair.
            if (num_to_index.find(complement) != num_to_index.end()) {
                return {num_to_index[complement], i};
            }
            
            // Otherwise, store the current number and its index.
            num_to_index[nums[i]] = i;
        }
        
        // The problem guarantees exactly one solution, so this line is theoretically unreachable.
        return {};
    }
};