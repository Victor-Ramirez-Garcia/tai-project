#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool hasSameDigits(string s) {
        // Since the maximum constraints typically range between 3 <= s.length <= 100 
        // (for Version I) up to 1000+ (for Version II), an elegant and highly optimized
        // simulation using inline array reduction guarantees O(N^2) time and O(N) space,
        // which effortlessly executes well within the time limits without numerical overhead.
        int n = s.length();
        vector<int> current(n);
        
        // Convert characters to their respective integer digit representations
        for (int i = 0; i < n; ++i) {
            current[i] = s[i] - '0';
        }
        
        // Repeatedly shrink the array by summing adjacent elements modulo 10
        // until exactly two digits are left.
        while (n > 2) {
            for (int i = 0; i < n - 1; ++i) {
                current[i] = (current[i] + current[i + 1]) % 10;
            }
            n--; // The size effectively shrinks by 1 after each complete pass
        }
        
        // Return true if the final two digits are identical
        return current[0] == current[1];
    }
};