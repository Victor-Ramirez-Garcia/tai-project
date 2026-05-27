class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // Algorithm: Sliding Window / Two Pointers
        // Time Complexity: O(N) where N is the length of the string. Each character is visited at most twice.
        // Space Complexity: O(min(M, N)) where M is the size of the alphabet/character set (here, up to 128 for ASCII).
        
        // Use an array as a direct-address table to store the last seen index of each character.
        // Initialize all indices to -1.
        vector<int> last_seen(128, -1);
        
        int max_len = 0;
        int left = 0; // Left boundary of the current sliding window
        
        for (int right = 0; right < s.length(); ++right) {
            char current_char = s[right];
            
            // If the character was seen inside the current window, 
            // shrink the window by moving the left pointer past its previous occurrence.
            if (last_seen[current_char] >= left) {
                left = last_seen[current_char] + 1;
            }
            
            // Update the last seen position of the current character
            last_seen[current_char] = right;
            
            // Calculate the current window size and update max_len if it's larger
            max_len = max(max_len, right - left + 1);
        }
        
        return max_len;
    }
};