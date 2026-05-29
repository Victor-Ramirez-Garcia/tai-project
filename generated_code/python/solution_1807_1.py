from typing import List

class Solution:
    def minPartitions(self, n: str) -> int:
        # The key insight is that a deci-binary number can only contribute at most 1 
        # to any digit position in the sum. Therefore, to form a digit 'd' at any 
        # position, we need at least 'd' separate deci-binary numbers.
        # The overall minimum number of deci-binary numbers required is determined 
        # by the maximum digit present in the string 'n'.
        return int(max(n))