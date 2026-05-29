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

        // Track the last occurrence index of each character 'a' through 'z'
        vector<int> last_pos(26, -1);
        for (int i = 0; i < n; ++i) {
            last_pos[s[i] - 'a'] = i;
        }

        // We can use a greedy approach with a sliding window/interval merging strategy.
        // If we decide a substring starts with character C, this substring MUST extend 
        // at least until the very last occurrence of C in the entire string.
        // Furthermore, any other character introduced inside this substring will also 
        // have its last occurrence included, potentially expanding the boundary.
        
        int ans = 0;
        int i = 0;
        
        while (i < n) {
            int boundary = last_pos[s[i] - 'a'];
            int j = i;
            
            // Expand the current substring boundary to include the last occurrences
            // of all characters encountered within this substring.
            while (j <= boundary) {
                boundary = max(boundary, last_pos[s[j] - 'a']);
                j++;
            }
            
            // We found a valid independent block [i, boundary]
            ans++;
            // Move to the start of the next possible substring
            i = j;
        }
        
        return ans;
    }
};