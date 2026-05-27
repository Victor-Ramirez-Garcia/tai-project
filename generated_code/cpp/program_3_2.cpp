class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // We use an array to store the last seen position of each character.
        // Since the input consists of standard ASCII characters (letters, digits, symbols, spaces),
        // a size of 128 is sufficient. Initialize all positions to -1.
        int last_seen[128];
        std::fill_n(last_seen, 128, -1);
        
        int max_len = 0;
        int start = 0; // Left boundary of the sliding window
        
        // Expand the right boundary of the window
        for (int end = 0; end < s.length(); ++end) {
            char current_char = s[end];
            
            // If the character was seen inside the current window, 
            // shrink the window by moving 'start' past its previous occurrence.
            if (last_seen[current_char] >= start) {
                start = last_seen[current_char] + 1;
            }
            
            // Update the last seen position of the character
            last_seen[current_char] = end;
            
            // Calculate and track the maximum window size achieved
            max_len = std::max(max_len, end - start + 1);
        }
        
        return max_len;
    }
};