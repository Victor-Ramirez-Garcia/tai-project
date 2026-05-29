#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool equalFrequency(string word) {
        vector<int> count(26, 0);
        for (char c : word) {
            count[c - 'a']++;
        }

        // Try removing one instance of each possible character
        for (int i = 0; i < 26; ++i) {
            if (count[i] > 0) {
                count[i]--; // Simulate removal
                
                // Check if all remaining frequencies are equal
                int common_freq = -1;
                bool matches = true;
                for (int j = 0; j < 26; ++j) {
                    if (count[j] > 0) {
                        if (common_freq == -1) {
                            common_freq = count[j];
                        } else if (count[j] != common_freq) {
                            matches = false;
                            break;
                        }
                    }
                }
                
                if (matches) return true;
                
                count[i]++; // Restore original state
            }
        }
        
        return false;
    }
};