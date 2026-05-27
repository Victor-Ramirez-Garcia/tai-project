class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Optimality: Sliding Window approach with an array-based hash map.
        // Time Complexity: O(N) where N is the length of the string, as each character is visited at most twice.
        // Space Complexity: O(M) where M is the size of the alphabet/character set (O(1) auxiliary space since M <= 256).
        
        // Array to store the last seen index of each ASCII character. 
        // Initialized to -1 to signify that the character hasn't been seen yet.
        int last_seen[256];
        std::fill_n(last_seen, 256, -1);
        
        int max_len = 0;
        int start = 0; // Left boundary of the sliding window
        
        for (int end = 0; end < s.length(); ++end) {
            unsigned char current_char = s[end];
            
            // If the character was seen inside the current window, 
            // shrink the window by moving 'start' right after its last occurrence.
            if (last_seen[current_char] >= start) {
                start = last_seen[current_char] + 1;
            }
            
            // Update the last seen position of the current character
            last_seen[current_char] = end;
            
            // Calculate and update the maximum length found so far
            max_len = std::max(max_len, end - start + 1);
        }
        
        return max_len;
    }
};