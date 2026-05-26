class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Dictionary to store the last seen index of each character
        char_map = {}
        max_length = 0
        start = 0  # Left pointer of the sliding window
        
        # Iterate through the string with the right pointer 'end'
        for end, char in enumerate(s):
            # If the character is already in the map and its last seen index
            # is within the current window, contract the window by moving
            # the start pointer to the right of the last seen position.
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            
            # Update the last seen position of the current character
            char_map[char] = end
            
            # Calculate the current window length and update max_length if larger
            max_length = max(max_length, end - start + 1)
            
        return max_length