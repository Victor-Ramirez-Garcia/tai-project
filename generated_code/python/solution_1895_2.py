from typing import List

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        """
        Time Complexity: O(n) - Two passes over the string of length n.
        Space Complexity: O(1) - Only allocating space for the output array.
        
        Algorithm: Prefix and Suffix Sums (Linear Scan)
        We can calculate the number of operations required for each box by spliting
        the movement into two independent directions: left-to-right and right-to-left.
        - In the first pass (left-to-right), we track how many balls are to the left 
          of the current box and accumulate their distances.
        - In the second pass (right-to-left), we do the same for balls to the right 
          of the current box, adding their contributions to the answer array.
        """
        n = len(boxes)
        answer = [0] * n
        
        # Pass 1: Left-to-right (accumulate operations from balls to the left)
        left_balls = 0
        left_operations = 0
        for i in range(n):
            answer[i] += left_operations
            if boxes[i] == '1':
                left_balls += 1
            # Moving to the next box means all existing balls on the left take 1 more step
            left_operations += left_balls
            
        # Pass 2: Right-to-left (accumulate operations from balls to the right)
        right_balls = 0
        right_operations = 0
        for i in range(n - 1, -1, -1):
            answer[i] += right_operations
            if boxes[i] == '1':
                right_balls += 1
            # Moving to the next box (leftwards) means all existing balls on the right take 1 more step
            right_operations += right_balls
            
        return answer