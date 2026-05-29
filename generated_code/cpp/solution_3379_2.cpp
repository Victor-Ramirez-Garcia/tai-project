#include <string>
#include <cmath>
#include <numeric>

class Solution {
public:
    /**
     * Calculates the score of a string based on the sum of absolute differences 
     * between the ASCII values of adjacent characters.
     * * Time Complexity: O(n), where n is the length of the string. We traverse the string once.
     * Space Complexity: O(1), as we only use a single integer to accumulate the score.
     */
    int scoreOfString(std::string s) {
        int totalScore = 0;
        
        // Iterate from the first character to the second-to-last character
        for (size_t i = 0; i < s.length() - 1; ++i) {
            // Calculate absolute difference between ASCII values of adjacent chars
            // s[i] and s[i+1] are automatically treated as their integer ASCII values
            totalScore += std::abs(s[i] - s[i + 1]);
        }
        
        return totalScore;
    }
};