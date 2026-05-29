#include <string>
#include <cmath>

using namespace std;

class Solution {
public:
    int scoreOfString(string s) {
        int score = 0;
        // Iterate through the string up to the second-to-last character
        for (size_t i = 0; i < s.length() - 1; ++i) {
            // Accumulate the absolute difference between adjacent characters
            score += abs(s[i] - s[i + 1]);
        }
        return score;
    }
};