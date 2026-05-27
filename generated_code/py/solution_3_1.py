class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_map = {}
        max_len = 0
        left = 0  # Left boundary of the sliding window
        
        # Iterate through the string with the right boundary
        for right, char in enumerate(s):
            # If the character is already in the window, shrink the window 
            # by moving the left pointer to the right of the last seen position
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Update the last seen position of the current character
            char_map[char] = right
            
            # Calculate the current window size and update max_len
            max_len = max(max_len, right - left + 1)
            
        return max_len