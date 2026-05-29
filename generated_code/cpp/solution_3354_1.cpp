#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    string minimizeStringValue(string s) {
        // Track the frequency of each character in the original string
        vector<int> freq(26, 0);
        int question_count = 0;
        
        for (char c : s) {
            if (c == '?') {
                question_count++;
            } else {
                freq[c - 'a']++;
            }
        }
        
        // If there are no '?' to replace, return the original string
        if (question_count == 0) {
            return s;
        }
        
        // Min-heap to always pick the character that introduces the minimum additional cost.
        // Pair structure: {frequency, character_index}
        // This ensures we prioritize the lowest frequency, and break ties lexicographically.
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (int i = 0; i < 26; ++i) {
            pq.push({freq[i], i});
        }
        
        // Collect the best characters to fill the '?' positions
        vector<char> replacements;
        replacements.reserve(question_count);
        
        for (int i = 0; i < question_count; ++i) {
            auto [f, ch_idx] = pq.top();
            pq.pop();
            
            replacements.push_back('a' + ch_idx);
            
            // Increment the frequency of this character and push it back into the heap
            pq.push({f + 1, ch_idx});
        }
        
        // To ensure the final string is lexicographically smallest, 
        // the chosen replacement characters must be sorted.
        sort(replacements.begin(), replacements.end());
        
        // Insert the sorted replacements back into the '?' positions of the string
        int rep_idx = 0;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '?') {
                s[i] = replacements[rep_idx++];
            }
        }
        
        return s;
    }
};