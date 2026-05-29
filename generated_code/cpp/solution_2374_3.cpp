#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int maxSteps = 0;
        // The stack stores pairs of {value, steps_needed_to_be_eaten}
        // It functions as a monotonic decreasing stack based on the element values.
        stack<pair<int, int>> st;

        for (int i = nums.size() - 1; i >= 0; --i) {
            int currentSteps = 0;
            
            // If the current element is strictly greater than the element at the top 
            // of the stack, it means the current element will eventually "eat" that element.
            while (!st.empty() && nums[i] > st.top().first) {
                // The time required to eat the top element depends on how long that top 
                // element took to eat its own subsequent elements, plus one extra step 
                // because they happen concurrently, bounded by the maximum steps in its chain.
                currentSteps = max(currentSteps + 1, st.top().second);
                st.pop();
            }
            
            // Update the global maximum steps encountered so far
            maxSteps = max(maxSteps, currentSteps);
            
            // Push the current element along with the number of steps it takes to eat 
            // its targets onto the stack.
            st.push({nums[i], currentSteps});
        }

        return maxSteps;
    }
};