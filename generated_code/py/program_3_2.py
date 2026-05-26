class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_map = {}
        max_length = 0
        start = 0  # Left pointer of the sliding window
        
        # End pointer iterates through the string
        for end, char in enumerate(s):
            # If the character is already in the map and within the current window,
            # slide the start pointer to the right of its last occurrence
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            
            # Update the last seen position of the character
            char_map[char] = end
            
            # Update the maximum length found so far
            # Window length is calculated as (end - start + 1)
            max_length = max(max_length, end - start + 1)
            
        return max_length