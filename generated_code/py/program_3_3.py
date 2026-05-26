class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Map to store the last seen index of each character
        char_map = {}
        max_len = 0
        left = 0
        
        # Sliding window approach: right pointer expands the window
        for right, char in enumerate(s):
            # If the character is already in the window, shrink the window from the left
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Update the last seen position of the character
            char_map[char] = right
            
            # Update the maximum length found so far
            max_len = max(max_len, right - left + 1)
            
        return max_len