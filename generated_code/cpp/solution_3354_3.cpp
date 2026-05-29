#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    string minimizeStringValue(string s) {
        // Track the frequency of each lowercase letter in the string
        vector<int> counts(26, 0);
        int q_count = 0;
        
        for (char c : s) {
            if (c == '?') {
                q_count++;
            } else {
                counts[c - 'a']++;
            }
        }
        
        // Min-heap to always pick the character with the minimum frequency.
        // Pair structure: {frequency, character_index}
        // Greater comparison ensures we pick the smallest frequency, and 
        // lexicographically smallest character in case of ties.
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        for (int i = 0; i < 26; ++i) {
            pq.push({counts[i], i});
        }
        
        // Collect the characters that will replace the '?' marks
        vector<char> replacements;
        replacements.reserve(q_count);
        
        for (int i = 0; i < q_count; ++i) {
            auto [freq, ch_idx] = pq.top();
            pq.pop();
            
            replacements.push_back('a' + ch_idx);
            
            // Increment frequency and push back into the heap
            pq.push({freq + 1, ch_idx});
        }
        
        // To make the final string lexicographically smallest, 
        // we must sort the replacement characters.
        sort(replacements.begin(), replacements.end());
        
        // Place the sorted replacements back into the '?' positions
        int rep_idx = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '?') {
                s[i] = replacements[rep_idx++];
            }
        }
        
        return s;
    }
};