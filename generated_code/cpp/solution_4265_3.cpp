#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int longestBalanced(string s) {
        int n = s.length();
        int cnt0 = 0, cnt1 = 0;
        for (char c : s) {
            if (c == '0') cnt0++;
            else cnt1++;
        }

        // pos stores the historical indices for each prefix sum value
        // Mapping: prefix_sum -> list of indices
        unordered_map<int, vector<int>> pos;
        pos[0].push_back(-1); // Base case for prefix sum 0 before the string starts

        int ans = 0;
        int pre = 0;

        for (int i = 0; i < n; ++i) {
            pre += (s[i] == '1') ? 1 : -1;
            pos[pre].push_back(i);

            // Case 1: Already balanced substring without any swap (sum = 0)
            // The longest substring is from the very first occurrence of the same prefix sum
            ans = max(ans, i - pos[pre][0]);

            // Case 2: Substring has an excess of two '1's (sum = +2)
            // It can be made balanced if we swap one '1' from inside with one '0' from outside.
            if (pos.count(pre - 2)) {
                const auto& p = pos[pre - 2];
                // Try the earliest occurrence first
                int len = i - p[0];
                int zeros_inside = (len - 2) / 2;
                if (zeros_inside < cnt0) {
                    ans = max(ans, len);
                } 
                // If the earliest occurrence fails (meaning all '0's in the string are inside it),
                // we can try the second earliest occurrence if it exists.
                else if (p.size() > 1) {
                    ans = max(ans, i - p[1]);
                }
            }

            // Case 3: Substring has an excess of two '0's (sum = -2)
            // It can be made balanced if we swap one '0' from inside with one '1' from outside.
            if (pos.count(pre + 2)) {
                const auto& p = pos[pre + 2];
                // Try the earliest occurrence first
                int len = i - p[0];
                int ones_inside = (len - 2) / 2;
                if (ones_inside < cnt1) {
                    ans = max(ans, len);
                } 
                // If the earliest occurrence fails (meaning all '1's in the string are inside it),
                // we can try the second earliest occurrence if it exists.
                else if (p.size() > 1) {
                    ans = max(ans, i - p[1]);
                }
            }
        }

        return ans;
    }
};