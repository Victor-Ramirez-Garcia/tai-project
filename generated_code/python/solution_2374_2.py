from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # ans tracks the maximum number of steps required overall
        ans = 0
        
        # Monotonic stack stores pairs of (value, steps_needed_to_be_eaten)
        # It is kept strictly decreasing based on the element value.
        stack = []
        
        # Iterate from right to left to determine how long each element 
        # survives relative to the larger elements to its left.
        for i in range(len(nums) - 1, -1, -1):
            cur_steps = 0
            
            # While the stack is not empty and the current element is strictly 
            # greater than the element at the top of the stack, it means the 
            # current element will eventually "eat" the stack's top element.
            while stack and nums[i] > stack[-1][0]:
                # The time required to eat the top element depends on how long 
                # that top element itself survived to eat elements to its right.
                # We need at least 1 step + the steps the top element took, 
                # or the cumulative steps calculated so far (whichever is larger).
                cur_steps = max(cur_steps + 1, stack[-1][1])
                stack.pop()
                
            # Update the global maximum steps encountered
            ans = max(ans, cur_steps)
            
            # Push the current element along with its calculated steps onto the stack
            stack.append((nums[i], cur_steps))
            
        return ans