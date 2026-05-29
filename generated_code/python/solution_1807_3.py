class Solution:
    def minPartitions(self, n: str) -> int:
        # The key insight is that a deci-binary number can contribute at most 1 
        # to any digit position in a single addition. Therefore, to form the largest 
        # digit in the string 'n', we need at least that many deci-binary numbers.
        # For instance, if 'n' contains the digit '9', we need at least 9 numbers 
        # because each can contribute at most 1 to that position. 
        # Since no digit can exceed 9, the answer is simply the maximum digit present in 'n'.
        # Time Complexity: O(L) where L is the length of string n, as we do a single pass.
        # Space Complexity: O(1) auxiliary space.
        return int(max(n))