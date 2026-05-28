from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Time Complexity: O(N) where N is the number of operations, as we iterate through the list once.
        # Space Complexity: O(1) as we only use a single integer variable to track the value.
        
        x = 0
        for op in operations:
            # Checking the middle character (index 1) of the string is sufficient.
            # If it's '+', the operation is either "++X" or "X++", so we increment.
            # Otherwise, it's '-', representing "--X" or "X--", so we decrement.
            if op[1] == '+':
                x += 1
            else:
                x -= 1
        return x