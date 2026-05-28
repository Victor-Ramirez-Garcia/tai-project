from typing import List

class Solution:
    def scoreOfString(self, s: str) -> int:
        # Time Complexity: O(n) where n is the length of the string s
        # Space Complexity: O(1) as we only use a few variables for accumulation
        
        score = 0
        
        # Iterate through the string up to the second to last character
        for i in range(len(s) - 1):
            # Add the absolute difference of ASCII values of adjacent characters
            score += abs(ord(s[i]) - ord(s[i + 1]))
            
        return score