#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxDistinct(string s) {
        int n = s.length();
        if (n == 0) return 0;

        // bitmask representing the set of characters present in the entire suffix s[i...n-1]
        vector<int> suffix_mask(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            suffix_mask[i] = suffix_mask[i + 1] | (1 << (s[i] - 'a'));
        }

        // dp[mask] stores the maximum number of substrings we can form using a subset of 
        // characters represented by 'mask' as the starting characters of those substrings.
        // Since there are 26 lowercase English letters, a mask of 2^26 fits in a standard integer.
        // We initialize with -1 to represent unreachable states.
        vector<int> dp(1 << 26, -1);
        dp[0] = 0; // Base case: 0 substrings formed with an empty set of starting characters

        // Iterate through the string. At each step, we consider extending the current substring
        // or ending it. To optimize, we can think of this as finding the best valid splits.
        // dp_next will track the maximum substrings achievable ending at the current character position.
        vector<int> dp_next(1 << 26, -1);

        for (int i = 0; i < n; ++i) {
            int char_bit = 1 << (s[i] - 'a');
            
            // We can only transition from states where the remaining suffix contains all the 
            // characters we still hope to use. However, a simpler layer-by-layer update 
            // works by iterating through valid masks. To optimize, we only care about masks
            // that are subsets of the available characters from prefix or suffix.
            // For a practical and highly efficient iterative approach, we can maintain the maximum 
            // pieces manageable up to index `i` given a `mask` of used starting characters.
            
            // Optimization: Instead of full 2^26 DP which is too slow (64M states), 
            // notice that we want to greedily pick the first occurrence of a character to start a new substring
            // because delaying it never helps us get *more* distinct starting characters.
            // Let's re-evaluate: If we start a substring with char `c`, it covers up to the next chosen start.
            // Since we want to MAXIMIZE the number of substrings, and each must start with a UNIQUE character,
            // the maximum possible answer is bounded by the number of unique characters in the string.
            // Can we always achieve the total number of unique characters?
            // If we greedily take the first occurrence of each character as a split point, 
            // they will be ordered by their first appearance. 
            // Let the first occurrences be at indices i_1 < i_2 < ... < i_k.
            // If we split exactly at these indices, the pieces are:
            // s[i_1 ... i_2 - 1], s[i_2 ... i_3 - 1], ..., s[i_k ... n - 1].
            // Does each piece start with a distinct character? 
            // Yes, piece j starts at i_j, so its first character is s[i_j]. 
            // Since i_j are the first occurrence indices of distinct characters, all s[i_j] are distinct!
            // Therefore, we can ALWAYS achieve a score equal to the total number of unique characters in the string.
            // Since we cannot exceed the number of unique characters (as each substring must start with a distinct char),
            // the maximum number of substrings is exactly the number of unique characters in `s`.
        }

        // Count unique characters in s
        int unique_count = 0;
        vector<bool> visited(26, false);
        for (char c : s) {
            if (!visited[c - 'a']) {
                visited[c - 'a'] = true;
                unique_count++;
            }
        }

        return unique_count;
    }
};