class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // char_map stores the last seen index of each character.
        // Initializing with -1 to handle 0-indexed positions correctly.
        vector<int> char_map(128, -1);
        
        int max_len = 0;
        int start = 0; // Left pointer of the sliding window
        
        for (int end = 0; end < s.length(); ++end) {
            char current_char = s[end];
            
            // If the character is already in the window, shrink the window 
            // by moving the start pointer to the right of the previous duplicate.
            if (char_map[current_char] >= start) {
                start = char_map[current_char] + 1;
            }
            
            // Update the last seen position of the character
            char_map[current_char] = end;
            
            // Calculate the maximum length of the window so far
            max_len = max(max_len, end - start + 1);
        }
        
        return max_len;
    }
};