#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool equalFrequency(string word) {
        // Step 1: Count frequencies of each character
        vector<int> char_counts(26, 0);
        for (char c : word) {
            char_counts[c - 'a']++;
        }

        // Step 2: Try removing one instance of each possible character
        for (int i = 0; i < 26; ++i) {
            if (char_counts[i] > 0) {
                // Simulate removal
                char_counts[i]--;

                // Check if all remaining non-zero frequencies are equal
                int target_freq = -1;
                bool is_equal = true;
                
                for (int count : char_counts) {
                    if (count > 0) {
                        if (target_freq == -1) {
                            target_freq = count; // Set the baseline frequency
                        } else if (count != target_freq) {
                            is_equal = false;    // Found a mismatch
                            break;
                        }
                    }
                }

                // If valid, return true immediately
                if (is_equal) {
                    return true;
                }

                // Backtrack for the next iteration
                char_counts[i]++;
            }
        }

        return false;
    }
};