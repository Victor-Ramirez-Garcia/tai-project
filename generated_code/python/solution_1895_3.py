from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Algorithm: Linear Scan (Prefix and Suffix passes)
        Time Complexity: O(n) - Two passes over the array of length n.
        Space Complexity: O(1) auxiliary space (excluding the output array).
        
        Instead of a naive O(n^2) approach, we can track the cumulative operations 
        needed from left to right, and then right to left.
        
        As we move from one box to the next, every ball we have seen so far requires 
        exactly 1 additional step.
        """
        n = len(boxes)
        ans = [0] * n
        
        # Pass 1: Left to Right
        # Track the number of balls seen so far and the operations accumulated
        balls_count = 0
        ops = 0
        for i in range(n):
            ans[i] += ops
            if boxes[i] == '1':
                balls_count += 1
            ops += balls_count
            
        # Pass 2: Right to Left
        # Accumulate the operations from the right side
        balls_count = 0
        ops = 0
        for i in range(n - 1, -1, -1):
            ans[i] += ops
            if boxes[i] == '1':
                balls_count += 1
            ops += balls_count
            
        return ans