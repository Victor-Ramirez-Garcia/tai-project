#include <string>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    string minimizeStringValue(string s) {
        // Frequency array to keep track of counts of each character already present in s
        vector<int> counts(26, 0);
        vector<int> question_mark_indices;
        
        // Count initial frequencies of fixed characters and locate '?' indices
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != '?') {
                counts[s[i] - 'a']++;
            } else {
                question_mark_indices.push_back(i);
            }
        }
        
        // If there are no '?' characters, return s as it is
        if (question_mark_indices.empty()) {
            return s;
        }
        
        // Min-heap to always pick the character with the minimum current frequency.
        // Pairs are stored as {frequency, char_index} to naturally handle 
        // the lexicographically smallest character tie-breaker.
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        for (int i = 0; i < 26; ++i) {
            pq.push({counts[i], i});
        }
        
        // Greedily collect the best characters to fill the '?' slots.
        // This minimizes the overall cost contribution regardless of the replacement order.
        string replacements = "";
        for (int i = 0; i < question_mark_indices.size(); ++i) {
            auto [freq, ch_idx] = pq.top();
            pq.pop();
            
            replacements += (char)('a' + ch_idx);
            
            // Increment the frequency and push back into the heap
            pq.push({freq + 1, ch_idx});
        }
        
        // To guarantee the lexicographically smallest final string, 
        // the chosen characters must be placed in sorted order across the '?' indices.
        sort(replacements.begin(), replacements.end());
        
        // Replace the '?' tokens in s with the sorted replacement characters
        for (int i = 0; i < question_mark_indices.size(); ++i) {
            s[question_mark_indices[i]] = replacements[i];
        }
        
        return s;
    }
};