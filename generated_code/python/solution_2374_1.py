from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        # We use a monotonic decreasing stack to keep track of elements and the number of 
        # steps required to remove them. 
        # Each element in the stack is a tuple: (value, steps_to_remove)
        stack = []
        max_steps = 0
        
        for num in nums:
            cur_steps = 0
            # If the current element is greater than or equal to the top of the stack,
            # it means the current element will "survive" longer or engulf the elements 
            # that were being removed by the stack's top. Thus, it inherits/accumulates 
            # the steps needed.
            while stack and stack[-1][0] <= num:
                cur_steps = max(cur_steps, stack.pop()[1])
            
            # If the stack is not empty, the current element is strictly smaller than 
            # the element remaining on the top of the stack. This means the top element 
            # will eventually eat the current element.
            if stack:
                cur_steps += 1
            else:
                # If the stack is empty, this element is the largest seen so far from the 
                # left, meaning it can never be removed.
                cur_steps = 0
                
            max_steps = max(max_steps, cur_steps)
            stack.append((num, cur_steps))
            
        return max_steps