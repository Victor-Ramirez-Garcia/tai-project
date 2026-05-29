#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int strongPasswordChecker(string password) {
        int n = password.length();
        
        // Check for missing types: lowercase, uppercase, and digit
        bool has_lower = false, has_upper = false, has_digit = false;
        for (char c : password) {
            if (islower(c)) has_lower = true;
            if (isupper(c)) has_upper = true;
            if (isdigit(c)) has_digit = true;
        }
        int missing_types = (has_lower ? 0 : 1) + (has_upper ? 0 : 1) + (has_digit ? 0 : 1);
        
        // Count lengths of repeating character sequences
        vector<int> repeats;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && password[j] == password[i]) {
                j++;
            }
            int len = j - i;
            if (len >= 3) {
                repeats.push_back(len);
            }
            i = j;
        }
        
        // Case 1: Password is too short
        // We only need insertions. Insertions can also fix repetitions and missing types.
        if (n < 6) {
            return max(6 - n, missing_types);
        }
        
        // Case 2: Password has valid length [6, 20]
        // We only need replacements. Replacements can resolve both repetitions and missing types.
        if (n <= 20) {
            int replace_needed = 0;
            for (int len : repeats) {
                replace_needed += len / 3;
            }
            return max(replace_needed, missing_types);
        }
        
        // Case 3: Password is too long
        // Deletions are mandatory to reach length 20. 
        // We use deletions strategically to reduce the number of replacements needed.
        int delete_needed = n - 20;
        int overlength = delete_needed;
        
        // Priority 1: Reduce repeats where len % 3 == 0. (1 deletion saves 1 replacement)
        for (int& len : repeats) {
            if (overlength > 0 && len % 3 == 0) {
                len -= 1;
                overlength -= 1;
            }
        }
        
        // Priority 2: Reduce repeats where len % 3 == 1. (2 deletions save 1 replacement)
        for (int& len : repeats) {
            if (overlength > 0 && len % 3 == 1) {
                int rem = min(overlength, 2);
                len -= rem;
                overlength -= rem;
            }
        }
        
        // Priority 3: Reduce remaining repeats (3 deletions save 1 replacement)
        for (int& len : repeats) {
            if (overlength > 0 && len >= 3) {
                int max_del = len - 2; // Keep at least 2 characters to avoid creating new patterns
                int rem = min(overlength, max_del);
                len -= rem;
                overlength -= rem;
            }
        }
        
        // Calculate remaining replacements needed after optimal deletions
        int replace_needed = 0;
        for (int len : repeats) {
            if (len >= 3) {
                replace_needed += len / 3;
            }
        }
        
        // Total steps = required deletions + max of required replacements or missing types
        return delete_needed + max(replace_needed, missing_types);
    }
};