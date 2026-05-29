#include <string>
#include <algorithm>

/**
 * Problem: Minimum Number of Deci-Binary Numbers
 * Time Complexity: O(N), where N is the length of string n. We iterate through the string once.
 * Space Complexity: O(1), as we only store the maximum digit found.
 * 
 * Logic:
 * A deci-binary number only contains digits 0 and 1. To form a digit 'd' at any 
 * position in the target number n, we need at least 'd' deci-binary numbers that 
 * have a '1' at that specific position. 
 * 
 * For example, to get a '9' in the units place, we need nine 1s (1+1+1+1+1+1+1+1+1).
 * Since we can't have a digit greater than 9 in decimal, the minimum number of 
 * deci-binary numbers required to sum up to n is simply the value of the 
 * largest digit present in the string n.
 */

class Solution {
public:
    int minPartitions(std::string n) {
        // The answer is the maximum digit in the string.
        // We initialize result to '0'.
        char max_digit = '0';
        
        for (char c : n) {
            if (c > max_digit) {
                max_digit = c;
            }
            // Optimization: If we find a '9', we can stop early as it's the 
            // highest possible digit in a decimal system.
            if (max_digit == '9') return 9;
        }
        
        // Convert char digit to integer
        return max_digit - '0';
    }
};