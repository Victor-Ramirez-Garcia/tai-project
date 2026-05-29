#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool hasMatch(string s, string p) {
        // Find the single '*' character in the pattern string p
        size_t star_idx = p.find('*');
        
        // Split the pattern into a prefix and a suffix around the '*'
        string prefix = p.substr(0, star_idx);
        string suffix = p.substr(star_idx + 1);
        
        // Find the first occurrence of the prefix in string s
        size_t prefix_idx = s.find(prefix);
        if (prefix_idx == string::npos) {
            return false;
        }
        
        // The suffix must appear after the end of the matched prefix.
        // Since '*' can match 0 or more characters, the suffix can start 
        // immediately where the prefix ends (prefix_idx + prefix.length()).
        size_t suffix_idx = s.find(suffix, prefix_idx + prefix.length());
        
        // If both prefix and suffix are found in the correct order, it's a match
        return suffix_idx != string::npos;
    }
};