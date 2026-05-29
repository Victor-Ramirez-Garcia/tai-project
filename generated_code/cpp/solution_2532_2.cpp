#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool equalFrequency(string word) {
        // Count frequencies of each character
        vector<int> char_counts(26, 0);
        for (char c : word) {
            char_counts[c - 'a']++;
        }

        // Try removing one instance of each possible character
        for (int i = 0; i < 26; ++i) {
            if (char_counts[i] > 0) {
                // Simulate removal
                char_counts[i]--;

                // Check if all remaining non-zero frequencies are equal
                int target_freq = -1;
                bool possible = true;
                
                for (int j = 0; j < 26; ++j) {
                    if (char_counts[j] > 0) {
                        if (target_freq == -1) {
                            target_freq = char_counts[j];
                        } else if (char_counts[j] != target_freq) {
                            possible = false;
                            break;
                        }
                    }
                }

                if (possible) {
                    return true;
                }

                // Restore count for next iteration
                char_counts[i]++;
            }
        }

        return false;
    }
};