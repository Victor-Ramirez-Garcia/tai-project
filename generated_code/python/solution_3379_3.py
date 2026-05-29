from typing import List

class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Calculates the score of a string defined as the sum of absolute 
        differences between the ASCII values of adjacent characters.
        
        Time Complexity: O(n), where n is the length of the string.
        Space Complexity: O(1), as we only store the running total.
        """
        score = 0
        
        # Iterate through the string from the first character to the second-to-last
        for i in range(len(s) - 1):
            # Calculate absolute difference between ASCII values of adjacent chars
            # ord() returns the Unicode/ASCII integer representation
            score += abs(ord(s[i]) - ord(s[i + 1]))
            
        return score