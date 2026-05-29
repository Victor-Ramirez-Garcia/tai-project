#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int strongPasswordChecker(string password) {
        int n = password.length();
        
        // 1. Calculate missing types (lowercase, uppercase, digit)
        int has_lower = 0, has_upper = 0, has_digit = 0;
        for (char c : password) {
            if (islower(c)) has_lower = 1;
            else if (isupper(c)) has_upper = 1;
            else if (isdigit(c)) has_digit = 1;
        }
        int missing_types = 3 - (has_lower + has_upper + has_digit);
        
        // 2. Count lengths of repeating character sequences
        vector<int> repeats;
        int i = 0;
        while (i < n) {
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
        
        // Case 1: Length is less than 6
        // We only need insertions. Insertions can fix missing types and break up repeats.
        if (n < 6) {
            return max(6 - n, missing_types);
        }
        
        // Case 2: Length is between 6 and 20
        // We only need replacements. Replacements can fix missing types and break up repeats.
        if (n <= 20) {
            int replace_needed = 0;
            for (int len : repeats) {
                replace_needed += len / 3;
            }
            return max(replace_needed, missing_types);
        }
        
        // Case 3: Length is greater than 20
        // We must use deletions to reach length 20.
        // Deletions should be chosen strategically to reduce the number of replacements needed.
        // A repeat length of len requires len / 3 replacements.
        // Modifying len dynamically via deletions:
        // - len % 3 == 0: 1 deletion reduces replacements by 1. (Highest priority)
        // - len % 3 == 1: 2 deletions reduce replacements by 1. (Medium priority)
        // - len % 3 == 2: 3 deletions reduce replacements by 1. (Lowest priority)
        int deletes_needed = n - 20;
        int over = deletes_needed;
        
        // Priority 1: len % 3 == 0 sequences (1 delete saves 1 replacement)
        for (int& len : repeats) {
            if (over > 0 && len % 3 == 0) {
                len -= 1;
                over -= 1;
            }
        }
        
        // Priority 2: len % 3 == 1 sequences (2 deletes save 1 replacement)
        for (int& len : repeats) {
            if (over >= 2 && len % 3 == 1) {
                len -= 2;
                over -= 2;
            }
        }
        
        // Priority 3: remaining sequences (3 deletes save 1 replacement)
        for (int& len : repeats) {
            if (over > 0) {
                int possible_deletes = len - 2; // Can't reduce below 2 as it stops repeating
                int actual_deletes = min(over, possible_deletes);
                len -= actual_deletes;
                over -= actual_deletes;
            }
        }
        
        // Calculate remaining replacements needed after all prioritized deletions
        int replace_needed = 0;
        for (int len : repeats) {
            if (len >= 3) {
                replace_needed += len / 3;
            }
        }
        
        // Total steps = deletions + max of remaining replacements or missing types
        return deletes_needed + max(replace_needed, missing_types);
    }
};