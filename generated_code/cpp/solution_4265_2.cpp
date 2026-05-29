#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestBalanced(string s) {
        // Count total '0's and '1's in the entire string
        int cnt0 = count(s.begin(), s.end(), '0');
        int cnt1 = s.size() - cnt0;
        
        // To simplify, if there are fewer '0's than '1's, we invert the string
        // This ensures that we only need to worry about one direction of imbalance (e.g., extra '1's)
        if (cnt0 < cnt1) {
            swap(cnt0, cnt1);
            for (char &c : s) {
                c = (c == '1') ? '0' : '1';
            }
        }
        
        // lookup maps a prefix balance to its earliest occurrence indices.
        // We only ever need at most the first two occurrences for correctness.
        unordered_map<int, vector<int>> lookup;
        lookup[0] = {-1};
        
        int result = 0;
        int bal = 0;
        
        for (int i = 0; i < s.size(); ++i) {
            bal += (s[i] == '1') ? 1 : -1;
            
            // Keep at most 2 indices for the current balance value
            if (lookup[bal].size() < 2) {
                lookup[bal].push_back(i);
            }
            
            // Case 1: Already balanced substring without any swaps
            result = max(result, i - lookup[bal][0]);
            
            // Case 2: Substring has an excess of '1's (bal_right - bal_left == 2)
            // It needs one '0' from outside to swap with a '1' from inside.
            // A swap is valid if the number of '1's inside the substring is strictly less than cnt1
            // (i.e., there is at least one '1' remaining outside to swap with the '0' outside).
            // Length of substring = i - j. 
            // Total '1's inside = ((i - j) + 2) / 2 = (i - j + 2) / 2.
            // Since we need to swap one '1' inside with a '0' outside, we need at least one '1' inside, 
            // and the '0' outside requires that not all '1's in the entire string are inside.
            // Thus, we check if total '1's inside is less than the global cnt1.
            if (lookup.count(bal + 2)) {
                for (int j : lookup[bal + 2]) {
                    if ((i - j + 2) / 2 < cnt1) {
                        result = max(result, i - j);
                        break; // Since j is in increasing order, the first valid gives the max length
                    }
                }
            }
        }
        
        return result;
    }
};