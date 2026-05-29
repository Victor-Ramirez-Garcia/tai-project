#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minOperations(string s) {
        // If the string is already sorted, no operations are needed.
        if (is_sorted(s.begin(), s.end())) {
            return 0;
        }
        
        int n = s.length();
        
        // Find the minimum and maximum characters in the entire string.
        char min_char = s[0];
        char max_char = s[0];
        for (char c : s) {
            if (c < min_char) min_char = c;
            if (c > max_char) max_char = c;
        }
        
        // Case 1: The smallest character is already at the beginning OR
        // the largest character is already at the end.
        // We can sort the remaining suffix (excluding index 0) or prefix (excluding index n-1)
        // in 1 operation, because the target substring is not the entire string.
        if (s[0] == min_char || s[n - 1] == max_char) {
            return 1;
        }
        
        // Case 2: The largest character is at the beginning AND the smallest character is at the end.
        // We cannot fix both in 1 operation since any valid operation must exclude at least one element.
        // First operation: sort s[0...n-2] -> brings min_char to the front. Now s[0] == min_char.
        // Second operation: sort s[1...n-1] -> sorts the rest and moves max_char to the end.
        // This always takes exactly 2 operations.
        if (s[0] == max_char && s[n - 1] == min_char) {
            return 2;
        }
        
        // Case 3: Neither boundary character is in its ideal position, but they aren't completely swapped either.
        // We can do it in 1 operation by finding a substring that excludes either the first or last character,
        // but wait: if s[0] != min_char and s[n-1] != max_char, any single operation excluding s[0] cannot move
        // the true min_char to s[0]. Similarly, any operation excluding s[n-1] cannot move max_char to s[n-1].
        // Thus, 1 operation is impossible, and it will always take 2 operations.
        return 2;
    }
};