#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minPartitions(string n) {
        // Since each deci-binary number can contribute at most 1 to any digit position
        // in a single step (as its digits can only be 0 or 1), the minimum number of 
        // deci-binary numbers required to form the total sum is determined entirely 
        // by the maximum digit present in the string `n`.
        // Time Complexity: O(L) where L is the length of the string `n`.
        // Space Complexity: O(1) auxiliary space.
        
        char max_digit = '0';
        for (char c : n) {
            if (c > max_digit) {
                max_digit = c;
            }
            // Optimization: '9' is the maximum possible digit, so we can return early.
            if (max_digit == '9') {
                return 9;
            }
        }
        
        return max_digit - '0';
    }
};