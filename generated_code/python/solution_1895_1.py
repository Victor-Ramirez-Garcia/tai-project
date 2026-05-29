from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Algorithm: Linear Scan (Prefix and Suffix passes)
        Time Complexity: O(n) - We make two passes over the array of length n.
        Space Complexity: O(1) - Excluding the output array, we use constant extra space.
        
        The core idea is that as we move from left to right, each ball to our left
        contributes 1 additional operation for every step we take. Similarly for right to left.
        """
        n = len(boxes)
        answer = [0] * n
        
        # Pass 1: Left-to-Right
        # Calculate operations needed to bring all balls on the left to index i
        left_balls = 0
        left_ops = 0
        for i in range(n):
            answer[i] += left_ops
            # If the current box has a ball, it will count towards the operations of subsequent boxes
            if boxes[i] == '1':
                left_balls += 1
            # Moving to the next index increases the cost by the number of balls seen so far
            left_ops += left_balls
            
        # Pass 2: Right-to-Left
        # Calculate operations needed to bring all balls on the right to index i
        right_balls = 0
        right_ops = 0
        for i in range(n - 1, -1, -1):
            answer[i] += right_ops
            if boxes[i] == '1':
                right_balls += 1
            right_ops += right_balls
            
        return answer