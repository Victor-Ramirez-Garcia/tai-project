from typing import List

class Solution:
    def minOperations(self, s: str) -> int:
        # Time Complexity: O(N log N) due to sorting, Space Complexity: O(N) for creating the sorted string
        
        # If the string is already sorted, 0 operations are required.
        sorted_s = "".join(sorted(s))
        if s == sorted_s:
            return 0
        
        # If the first character of the original string matches the first character of the sorted string,
        # or the last character matches the last character of the sorted string, we can sort the rest 
        # of the string (which is a valid proper substring) in exactly 1 operation.
        if s[0] == sorted_s[0] or s[-1] == sorted_s[-1]:
            return 1
            
        # If neither the first nor the last character matches their correct sorted positions, 
        # we can't do it in 1 operation because any proper substring must exclude either the 
        # first or the last character. However, we can always do it in 2 operations:
        # 1. Sort the prefix s[0 : n-1] -> this moves the smallest characters toward the front.
        # 2. Sort the suffix s[1 : n] -> this finishes sorting the entire string.
        return 2