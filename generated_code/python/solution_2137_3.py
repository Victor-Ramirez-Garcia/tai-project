from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Time Complexity: O(N) where N is the number of operations.
        # Space Complexity: O(1) as we only use a single variable for tracking the state.
        # Core logic: Checking the character at index 1 is sufficient because for 
        # "++X" and "X++", it's '+'. For "--X" and "X--", it's '-'.
        
        x = 0
        for op in operations:
            if op[1] == '+':
                x += 1
            else:
                x -= 1
        return x