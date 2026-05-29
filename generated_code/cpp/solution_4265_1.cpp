#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestBalanced(string s) {
        int n = s.length();
        
        // Count total frequencies of '0' and '1' in the original string
        int cnt0 = 0;
        for (char c : s) {
            if (c == '0') cnt0++;
        }
        int cnt1 = n - cnt0;
        
        // Map to store all indices where each prefix sum occurs.
        // Prefix sum formula: +1 for '1', -1 for '0'.
        unordered_map<int, vector<int>> pos;
        pos[0].push_back(-1); // Base case for prefix sum 0 at index -1
        
        int ans = 0;
        int pre = 0;
        
        for (int i = 0; i < n; ++i) {
            pre += (s[i] == '1') ? 1 : -1;
            pos[pre].push_back(i);
            
            // Case 1: Already balanced without any swap.
            // Substring from pos[pre][0] + 1 to i has an equal number of '0's and '1's.
            ans = max(ans, i - pos[pre][0]);
            
            // Case 2: Substring has two more '1's than '0's (Diff = +2).
            // We can swap one '1' from inside with one '0' from outside to make it balanced.
            if (pos.find(pre - 2) != pos.end()) {
                auto& p = pos[pre - 2];
                // Check if the earliest start index leaves enough '0's outside the substring.
                // The current number of '0's inside this substring is (length - 2) / 2.
                if ((i - p[0] - 2) / 2 < cnt0) {
                    ans = max(ans, i - p[0]);
                } else if (p.size() > 1) {
                    // If the earliest start leaves no '0's outside, try the second earliest start.
                    ans = max(ans, i - p[1]);
                }
            }
            
            // Case 3: Substring has two more '0's than '1's (Diff = -2).
            // We can swap one '0' from inside with one '1' from outside to make it balanced.
            if (pos.find(pre + 2) != pos.end()) {
                auto& p = pos[pre + 2];
                // Check if the earliest start index leaves enough '1's outside the substring.
                // The current number of '1's inside this substring is (length - 2) / 2.
                if ((i - p[0] - 2) / 2 < cnt1) {
                    ans = max(ans, i - p[0]);
                } else if (p.size() > 1) {
                    // If the earliest start leaves no '1's outside, try the second earliest start.
                    ans = max(ans, i - p[1]);
                }
            }
        }
        
        return ans;
    }
};