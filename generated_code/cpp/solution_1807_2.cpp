#include <string>
#include <algorithm>

/**
 * Problem: Minimum Number of Deci-Binary Numbers
 * Time Complexity: O(L), where L is the length of the string n. We iterate through the string once.
 * Space Complexity: O(1), as we only store the maximum digit encountered.
 * 
 * Logic: 
 * A deci-binary number consists only of digits 0 and 1. To form a total sum 'n', 
 * the digit at any position 'i' in n must be the sum of the digits at that 
 * same position 'i' in the chosen deci-binary numbers.
 * 
 * Since a deci-binary number can contribute at most 1 to any specific digit position, 
 * if a position in 'n' has a digit 'd', we need at least 'd' deci-binary numbers 
 * to sum up to that digit. Consequently, the minimum number of deci-binary numbers 
 * required is determined by the largest digit present in the string 'n'.
 */

class Solution {
public:
    int minPartitions(std::string n) {
        // The answer is simply the maximum digit in the string.
        // We can use std::max_element or a simple loop.
        char max_digit = '0';
        for (char c : n) {
            if (c > max_digit) {
                max_digit = c;
            }
            // Optimization: If we find '9', we can stop early as it's the highest possible digit.
            if (max_digit == '9') return 9;
        }
        return max_digit - '0';
    }
};