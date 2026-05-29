#include <vector>
#include <queue>
#include <utility>

using namespace std;

class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        // Custom comparator for the min-heap.
        // Elements are compared primarily by their current value.
        // If values are equal, the element with the smaller original index comes first.
        auto comp = [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.first != b.first) {
                return a.first > b.first; // Min-heap based on value
            }
            return a.second > b.second;   // Min-heap based on index for ties
        };
        
        // Priority queue stores pairs of {value, original_index}
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> min_heap(comp);
        
        // Initialize the heap with all elements from nums
        for (int i = 0; i < nums.size(); ++i) {
            min_heap.push({nums[i], i});
        }
        
        // Perform k operations: always extract the minimum element,
        // multiply its value, and push it back into the heap.
        // Time Complexity per operation: O(log N)
        while (k > 0) {
            auto [val, idx] = min_heap.top();
            min_heap.pop();
            
            val *= multiplier;
            min_heap.push({val, idx});
            
            k--;
        }
        
        // Reconstruct the final state array using the original indices
        vector<int> result(nums.size());
        while (!min_heap.empty()) {
            auto [val, idx] = min_heap.top();
            min_heap.pop();
            result[idx] = val;
        }
        
        return result;
    }
};