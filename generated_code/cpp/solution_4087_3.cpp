#include <string>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxDistinct(string s) {
        int n = s.length();
        if (n == 0) return 0;

        // last_pos[c] stores the last occurrence index of character c in string s.
        vector<int> last_pos(26, -1);
        for (int i = 0; i < n; ++i) {
            last_pos[s[i] - 'a'] = i;
        }

        // To maximize the number of valid substrings, we employ a greedy strategy.
        // We want to close a substring as early as possible.
        // However, if a character appears inside a substring, its *entire* range 
        // (from its first to its last occurrence) must be completely contained 
        // within that same substring. Otherwise, a subsequent substring would 
        // start with a character that has already appeared, violating the distinct starting character rule.
        
        int count = 0;
        int i = 0;
        while (i < n) {
            char start_char = s[i];
            int boundary = last_pos[start_char - 'a'];
            int j = i;
            
            // Expand the boundary of the current substring to include the last 
            // occurrence of any character that falls within the current segment.
            while (j <= boundary) {
                boundary = max(boundary, last_pos[s[j] - 'a']);
                j++;
            }
            
            // We found a valid independent block/substring.
            count++;
            // Move to the start of the next potential substring.
            i = j;
        }

        return count;
    }
};