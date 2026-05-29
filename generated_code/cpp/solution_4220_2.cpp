#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    int minOperations(string s) {
        // A string of length 0 or 1 is already sorted.
        if (s.length() <= 1) return 0;
        
        // Check if the string is already sorted.
        bool is_sorted = true;
        for (size_t i = 1; i < s.length(); ++i) {
            if (s[i] < s[i - 1]) {
                is_sorted = false;
                break;
            }
        }
        if (is_sorted) return 0;
        
        // Find the target sorted version of the string.
        string sorted_s = s;
        sort(sorted_s.begin(), sorted_s.end());
        
        // If the first character of s matches the smallest character,
        // we can sort the suffix s[1...n-1] to sort the whole string.
        // Since s is not the entire string, this takes 1 operation.
        if (s.front() == sorted_s.front()) return 1;
        
        // If the last character of s matches the largest character,
        // we can sort the prefix s[0...n-2] to sort the whole string.
        if (s.back() == sorted_s.back()) return 1;
        
        // If the first character of s is the largest and the last character is the smallest,
        // we cannot do it in 1 or 2 operations directly if we need to swap their roles,
        // but we can always do it in 3 operations:
        // 1. Sort s[0...n-2]: moves the smallest element away from the end.
        // 2. Sort s[1...n-1]: moves the largest element away from the front.
        // 3. Sort s[0...n-2]: finalizes the sort.
        // However, we must check if 2 operations are possible. 
        // 2 operations are possible if the first character is NOT the maximum character
        // AND the last character is NOT the minimum character. Since we already checked
        // front == min and back == max, 2 operations are possible if front != max OR back != min.
        if (s.front() == sorted_s.back() && s.back() == sorted_s.front()) {
            return 3;
        }
        
        // Otherwise, we can achieve it in 2 operations:
        // e.g., sort s[0...n-2] then sort s[1...n-1].
        return 2;
    }
};