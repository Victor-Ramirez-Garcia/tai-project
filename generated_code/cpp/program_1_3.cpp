#include <vector>
#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Use a hash map to store the value and its corresponding index.
        // This allows us to look up the complement in O(1) average time.
        std::unordered_map<int, int> num_to_index;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
            // Check if the complement already exists in the map
            auto it = num_to_index.find(complement);
            if (it != num_to_index.end()) {
                // If found, return the index of the complement and the current index
                return {it->second, i};
            }
            
            // Otherwise, store the current number and its index in the map
            num_to_index[nums[i]] = i;
        }
        
        // The problem guarantees exactly one solution, so this point is unreachable.
        return {};
    }
};