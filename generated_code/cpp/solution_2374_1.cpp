#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size();
        int max_steps = 0;
        
        // The stack will store pairs of {value, steps_needed_to_be_eaten}
        // It helps find the previous larger element and tracks how many steps
        // it takes for elements to be removed.
        stack<pair<int, int>> st;
        
        // Iterate backwards from the end of the array
        for (int i = n - 1; i >= 0; --i) {
            int current_steps = 0;
            
            // While the current element is strictly greater than the element at the top
            // of the stack, it means the current element will eventually "eat" (remove)
            // the element at the top of the stack.
            while (!st.empty() && nums[i] > st.top().first) {
                // The time to eat the top element depends on how long the top element 
                // itself took to eat elements after it, plus 1 for the current element 
                // to eat it. We take the maximum because elements can be processed in parallel.
                current_steps = max(current_steps + 1, st.top().second);
                st.pop();
            }
            
            // Record the total steps needed for the current element to eat its dependent elements
            max_steps = max(max_steps, current_steps);
            
            // Push the current element and its calculated steps onto the stack
            st.push({nums[i], current_steps});
        }
        
        return max_steps;
    }
};