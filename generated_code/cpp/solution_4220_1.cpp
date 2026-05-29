#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minOperations(string s) {
        // If the string is already sorted, 0 operations are needed.
        if (is_sorted(s.begin(), s.end())) {
            return 0;
        }

        // Keep track of the frequency of each character to determine the target sorted string.
        int count[26] = {0};
        for (char c : s) {
            count[c - 'a']++;
        }

        // Find the absolute minimum and maximum characters present in the string.
        char min_char = 'z', max_char = 'a';
        for (int i = 0; i < 26; ++i) {
            if (count[i] > 0) {
                if ((char)('a' + i) < min_char) min_char = (char)('a' + i);
                if ((char)('a' + i) > max_char) max_char = (char)('a' + i);
            }
        }

        // If the first character is already the global minimum, we can sort the rest 
        // of the string (from index 1 to n-1), which is a valid proper substring.
        // Similarly, if the last character is the global maximum, we can sort the 
        // prefix from index 0 to n-2. In either case, 1 operation is sufficient.
        if (s.front() == min_char || s.back() == max_char) {
            return 1;
        }

        // If the first character is the global maximum AND the last character is the global minimum,
        // we cannot fix both in a single proper substring operation. However, we can achieve it in 2:
        // Op 1: Sort the substring s[0...n-2]. This moves the max element away from the front.
        // Op 2: Now the last element is the global max, so we can sort s[0...n-2] or similar to finish,
        // or the first element becomes min_char, allowing us to sort s[1...n-1].
        // 
        // For all other cases (e.g., front is not min, back is not max, but they aren't cross-matched),
        // we can also do it in 2 operations. For instance, sort s[1...n-1] to place the max at the back,
        // then sort s[0...n-2] to place the min at the front.
        return 2;
    }
};