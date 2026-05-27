#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Map to store the value of an element and its corresponding index
        std::unordered_map<int, int> num_to_index;
        
        // Iterate through the array once: O(n) Time Complexity
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
            // Check if the complement exists in the map
            if (num_to_index.find(complement) != num_to_index.end()) {
                // If found, return the indices of the complement and the current element
                return {num_to_index[complement], i};
            }
            
            // Otherwise, store the current element and its index in the map
            // Space Complexity: O(n) to store elements in the worst case
            num_to_index[nums[i]] = i;
        }
        
        // The problem guarantees exactly one solution, so this line is theoretically unreachable.
        return {};
    }
};