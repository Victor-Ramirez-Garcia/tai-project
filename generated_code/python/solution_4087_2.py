from typing import List

class Solution:
    def maxDistinct(self, s: str) -> int:
        # Time Complexity: O(N) where N is the length of the string 's'.
        # Space Complexity: O(1) auxiliary space, as the bitmask and alphabet tracking 
        # take constant space (at most 26 characters).
        #
        # Strategy: Greedy / Bit Manipulation
        # To maximize the number of substrings, we want each substring to be as short 
        # as possible. A substring must start with a character that hasn't been used 
        # as a starting character yet. 
        # The ultimate constraint is that there are at most 26 unique characters in the 
        # entire string, so we can never have more substrings than the number of unique 
        # characters present in 's'.
        # Since we can always choose to group the remaining suffix of the string into 
        # the final substring, the maximum number of valid substrings is exactly equal 
        # to the number of unique characters present in the string 's'.
        
        seen_chars = 0
        for char in s:
            # Map 'a'-'z' to 0-25 and set the corresponding bit
            seen_chars |= (1 << (ord(char) - 97))
            
        # The total number of set bits represents the number of unique characters.
        # This count matches the maximum possible valid split.
        return bin(seen_chars).count('1')