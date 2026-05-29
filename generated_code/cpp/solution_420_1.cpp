#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    int strongPasswordChecker(string password) {
        int n = password.length();
        
        // 1. Check missing type requirements (Lowercase, Uppercase, Digit)
        int has_lower = 0, has_upper = 0, has_digit = 0;
        for (char c : password) {
            if (islower(c)) has_lower = 1;
            if (isupper(c)) has_upper = 1;
            if (isdigit(c)) has_digit = 1;
        }
        int missing_types = 3 - (has_lower + has_upper + has_digit);
        
        // 2. Identify all repeating character sequences of length >= 3
        vector<int> arr;
        for (int i = 0; i < n; ) {
            int j = i;
            while (j < n && password[j] == password[i]) {
                j++;
            }
            int len = j - i;
            if (len >= 3) {
                arr.push_back(len);
            }
            i = j;
        }
        
        // --- CASE 1: Length is less than 6 ---
        // We only need insertions. Insertions can also break repeating sequences 
        // and cover missing types simultaneously.
        if (n < 6) {
            return max(6 - n, missing_types);
        }
        
        // --- CASE 2: Length is between 6 and 20 ---
        // We only need replacements. Each replacement can reduce a repeating sequence
        // length by 3 and also satisfy a missing type requirement.
        else if (n <= 20) {
            int replacements = 0;
            for (int len : arr) {
                replacements += len / 3;
            }
            return max(replacements, missing_types);
        }
        
        // --- CASE 3: Length is greater than 20 ---
        // We must delete exactly (n - 20) characters. We want to use these deletions
        // optimally to minimize the number of subsequent replacements needed.
        // A sequence of length L requires L / 3 replacements.
        // - Sequences where L % 3 == 0 benefit most: 1 deletion reduces replacements by 1.
        // - Sequences where L % 3 == 1 need 2 deletions to reduce replacements by 1.
        // - Sequences where L % 3 == 2 need 3 deletions to reduce replacements by 1.
        else {
            int deletions = n - 20;
            int num_deletions = deletions; // keep track of total deletions to perform
            
            // Round 1: Prioritize sequences where len % 3 == 0
            for (int& len : arr) {
                if (num_deletions > 0 && len % 3 == 0) {
                    len -= 1;
                    num_deletions -= 1;
                }
            }
            
            // Round 2: Prioritize sequences where len % 3 == 1 (requires 2 deletions)
            for (int& len : arr) {
                if (num_deletions >= 2 && len % 3 == 1) {
                    len -= 2;
                    num_deletions -= 2;
                }
            }
            
            // Round 3: Remaining deletions applied to sequences where len % 3 == 2 (each 3 deletions reduces replacements by 1)
            for (int& len : arr) {
                if (num_deletions > 0 && len >= 3) {
                    int can_delete = len - 2; // Keep at least 2 to not waste deletions
                    int actual_delete = min(num_deletions, can_delete);
                    len -= actual_delete;
                    num_deletions -= actual_delete;
                }
            }
            
            // Calculate remaining replacements needed after optimized deletions
            int replacements = 0;
            for (int len : arr) {
                if (len >= 3) {
                    replacements += len / 3;
                }
            }
            
            // Total operations = deletions made + max of remaining replacements needed or missing types
            return deletions + max(replacements, missing_types);
        }
    }
};