#include <vector>
#include <queue>
#include <utility>

using namespace std;

class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        // Pair structure: {value, original_index}
        // Custom comparator to mimic LeetCode's requirements:
        // 1. Prioritize smaller values.
        // 2. If values are equal, prioritize the smaller index (first occurrence).
        auto comp = [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.first != b.first) {
                return a.first > b.first; 
            }
            return a.second > b.second;
        };
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> minHeap(comp);
        
        // Push all elements with their initial indices into the min-heap
        for (int i = 0; i < nums.size(); ++i) {
            minHeap.push({nums[i], i});
        }
        
        // Perform the k operations
        while (k > 0) {
            auto [val, idx] = minHeap.top();
            minHeap.pop();
            
            // Multiply the minimum element
            val *= multiplier;
            
            // Update the state in the original array and push it back to the heap
            nums[idx] = val;
            minHeap.push({val, idx});
            
            k--;
        }
        
        return nums;
    }
};