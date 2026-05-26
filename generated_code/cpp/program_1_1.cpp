#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        // Hash map to store the value and its corresponding index: { value -> index }
        // Time Complexity: O(N) - We traverse the list containing N elements only once.
        // Space Complexity: O(N) - In the worst case, we store up to N elements in the hash map.
        std::unordered_map<int, int> num_to_idx;
        
        for (int i = 0; i < nums.size(); ++i) {
            int complement = target - nums[i];
            
            // Check if the complement already exists in the map
            auto it = num_to_idx.find(complement);
            if (it != num_to_idx.end()) {
                return {it->second, i};
            }
            
            // If not found, insert the current number and its index into the map
            num_to_idx[nums[i]] = i;
        }
        
        // The problem guarantees exactly one solution, so this line is theoretically unreachable.
        return {};
    }
};