#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool hasMatch(string s, string p) {
        // Find the single '*' wildcard character in pattern p
        size_t star_idx = p.find('*');
        
        // Split the pattern into prefix and suffix around the '*'
        string prefix = p.substr(0, star_idx);
        string suffix = p.substr(star_idx + 1);
        
        // Find the first occurrence of the prefix in string s
        size_t prefix_idx = s.find(prefix);
        if (prefix_idx == string::npos) {
            return false;
        }
        
        // Find the suffix in the remaining part of s after the prefix.
        // The '*' can match 0 or more characters, so the suffix must start
        // at or after the end of the matched prefix.
        size_t suffix_idx = s.find(suffix, prefix_idx + prefix.length());
        
        // If the suffix is also found sequentially, it's a valid match
        return suffix_idx != string::npos;
    }
};