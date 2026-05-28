class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Calculates the score of a string, defined as the sum of the absolute
        differences between the ASCII values of adjacent characters.
        
        Time Complexity: O(N) where N is the length of the string s.
        Space Complexity: O(1) as we only use a few integer variables.
        """
        score = 0
        # Iterate through the string, comparing each character with the next one
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
            
        return score