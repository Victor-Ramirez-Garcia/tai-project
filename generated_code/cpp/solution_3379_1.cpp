#include <string>
#include <cmath>
#include <numeric>

using namespace std;

class Solution {
public:
    /**
     * Algorithm: Linear Scan / One-pass
     * Time Complexity: O(n), where n is the length of string s. 
     *                  We traverse the string exactly once.
     * Space Complexity: O(1), as we only use a single integer to accumulate the score.
     */
    int scoreOfString(string s) {
        int score = 0;
        
        // Iterate from the first character to the second-to-last character
        // to compare adjacent pairs (s[i] and s[i+1]).
        for (size_t i = 0; i < s.length() - 1; ++i) {
            // Add the absolute difference of ASCII values of adjacent characters.
            // abs() handles the magnitude regardless of character order.
            score += abs(s[i] - s[i + 1]);
        }
        
        return score;
    }
};