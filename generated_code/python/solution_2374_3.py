from typing import List

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        """
        Algorithm: Monotonic Stack
        
        To find the total steps, we need to determine how many rounds it takes 
        for each element to be eaten by a strictly larger element to its left.
        An element `nums[i]` is eaten by the closest element to its left, say `nums[j]`, 
        such that `nums[j] > nums[i]`. 
        
        However, `nums[i]` can only be eaten after all elements between `nums[j]` 
        and `nums[i]` that are smaller than `nums[j]` have already been eaten.
        Therefore, the number of steps to eat `nums[i]` is:
        1 + max(steps to eat elements between j and i)
        
        If no such `nums[j]` exists (i.e., `nums[i]` is a new maximum from the left), 
        it will never be eaten, so its steps = 0.
        
        We use a strictly decreasing monotonic stack storing tuples of (value, steps_to_be_eaten).
        
        Time Complexity: O(N) - Each element is pushed and popped from the stack at most once.
        Space Complexity: O(N) - To store elements in the monotonic stack.
        """
        ans = 0
        # The stack will store pairs: (value, steps needed to remove this value)
        stack = []
        
        for num in nums:
            cur_steps = 0
            # Pop elements from the stack that are less than or equal to the current element.
            # The current element can only be eaten after these popped elements are eaten.
            while stack and stack[-1][0] <= num:
                cur_steps = max(cur_steps, stack.pop()[1])
            
            # If the stack is not empty, the top element is strictly greater than `num`.
            # This means `num` will eventually be eaten by `stack[-1][0]`.
            # It will take 1 more step than the maximum steps of the elements eaten between them.
            if stack:
                cur_steps += 1
            else:
                # If the stack is empty, `num` is the largest element seen so far.
                # It will never be eaten.
                cur_steps = 0
                
            ans = max(ans, cur_steps)
            stack.append((num, cur_steps))
            
        return ans