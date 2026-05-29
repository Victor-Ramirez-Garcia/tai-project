from typing import Set

class Solution:
    def maxDistinct(self, s: str) -> int:
        # Time Complexity: O(N) where N is the length of the string s.
        # Space Complexity: O(1) auxiliary space because the set will hold at most 26 distinct characters.
        #
        # Greedy Strategy:
        # To maximize the number of substrings, we should make each substring as small as possible.
        # We iterate through the string and greedily start a new substring whenever we encounter
        # a character that has not yet been used to start any previous substring.
        # Once a character is used to start a substring, all subsequent characters belong to it
        # until we find a new, unused starting character.
        
        if not s:
            return 0
            
        seen_starts: Set[str] = set()
        
        for char in s:
            if char not in seen_starts:
                seen_starts.add(char)
                
        # The number of unique starting characters we encounter dictates the maximum 
        # number of valid substrings we can form.
        return len(seen_starts)