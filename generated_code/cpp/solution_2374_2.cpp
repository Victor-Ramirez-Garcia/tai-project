#include <vector>
#include <algorithm>
#include <stack>

using namespace std;

class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size();
        int maxSteps = 0;
        
        // The stack will store pairs of {value, steps_needed_to_be_eaten}
        // It acts as a monotonic decreasing stack based on the element values.
        stack<pair<int, int>> st;
        
        for (int i = n - 1; i >= 0; --i) {
            int steps = 0;
            
            // While the current element is strictly greater than the element 
            // at the top of the stack, it means the current element will 
            // eventually "eat" that element.
            while (!st.empty() && nums[i] > st.top().first) {
                // The current element needs to wait for the top element to finish 
                // eating its own dependents, or it takes 1 step if it eats it directly.
                steps = max(steps + 1, st.top().second);
                st.pop();
            }
            
            // Record the maximum steps seen across the entire array
            maxSteps = max(maxSteps, steps);
            
            // Push the current element and the total steps it takes to clear 
            // its right-hand dependents.
            st.push({nums[i], steps});
        }
        
        return maxSteps;
    }
};