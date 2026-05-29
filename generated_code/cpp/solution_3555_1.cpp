#include <vector>
#include <queue>
#include <utility>

using namespace std;

class Solution {
public:
    vector<int> getFinalState(vector<int>& nums, int k, int multiplier) {
        // We need to repeatedly find the minimum value, breaking ties by the earliest index.
        // A min-heap (priority queue) storing pairs of {value, index} is ideal for this.
        // Elements are compared first by value, then by index, which perfectly matches the requirements.
        
        // Define the comparator for the min-heap
        auto comp = [](const pair<int, int>& a, const pair<int, int>& b) {
            if (a.first == b.first) {
                return a.second > b.second; // Lesser index has higher priority
            }
            return a.first > b.first; // Lesser value has higher priority
        };
        
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(comp)> minHeap(comp);
        
        // Initialize the heap with all elements from nums
        for (int i = 0; i < nums.size(); ++i) {
            minHeap.push({nums[i], i});
        }
        
        // Perform k operations
        while (k > 0) {
            auto [val, idx] = minHeap.top();
            minHeap.pop();
            
            // Multiply the minimum element
            val *= multiplier;
            
            // Update the element in the original array
            nums[idx] = val;
            
            // Push the updated element back into the heap
            minHeap.push({val, idx});
            
            k--;
        }
        
        return nums;
    }
};