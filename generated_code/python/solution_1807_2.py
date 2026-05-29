from typing import List

class Solution:
    def minPartitions(self, n: str) -> int:
        # The key insight is that a deci-binary number can contribute at most 1 to any digit position.
        # Therefore, to sum up to a specific digit 'd' at any position, we need at least 'd' 
        # deci-binary numbers. The maximum digit in the entire string dominates the minimum 
        # number of partitions required.
        #
        # Time Complexity: O(L) where L is the length of string n, since we must check every digit.
        # Space Complexity: O(1) auxiliary space.
        
        return int(max(n))