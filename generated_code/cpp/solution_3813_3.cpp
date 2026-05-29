#include <string>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

class Solution {
public:
    string smallestPalindrome(string s, int k) {
        // Step 1: Count frequencies of each character
        vector<int> count(26, 0);
        for (char c : s) {
            count[c - 'a']++;
        }

        // Step 2: Validate if a palindrome can be formed
        int odd_count = 0;
        char mid_char = 0;
        string half = "";
        
        for (int i = 0; i < 26; ++i) {
            if (count[i] % 2 != 0) {
                odd_count++;
                mid_char = 'a' + i;
            }
            // Append half of the characters to build the base for permutations
            half.append(count[i] / 2, 'a' + i);
        }

        // A valid palindrome can have at most one character with an odd frequency
        if (odd_count > 1) {
            return "";
        }

        // Step 3: Find the k-th lexicographical permutation of the 'half' string
        // We use a combinatorial approach with factorials to skip blocks of permutations.
        int n = half.length();
        vector<long long> fact(n + 1, 1);
        for (int i = 1; i <= n; ++i) {
            fact[i] = fact[i - 1] * i;
            // Prevent potential overflow if n is large, though usually n <= 15 for such problems
            if (fact[i] < 0) fact[i] = Int64_MAX; 
        }

        // Count frequencies within the 'half' string to handle duplicates
        vector<int> half_count(26, 0);
        for (char c : half) {
            half_count[c - 'a']++;
        }

        // Total distinct permutations available
        long long total_perms = fact[n];
        for (int i = 0; i < 26; ++i) {
            total_perms /= fact[half_count[i]];
        }

        // If requested k is strictly greater than total available distinct permutations
        if (k > total_perms) {
            return "";
        }

        string half_res = "";
        long long current_k = k;

        // Construct the k-th permutation character by character
        for (int i = 0; i < n; ++i) {
            int remaining_len = n - 1 - i;
            
            for (int j = 0; j < 26; ++j) {
                if (half_count[j] > 0) {
                    // Calculate permutations if we choose character 'j' for the current position
                    half_count[j]--;
                    long long perms_with_j = fact[remaining_len];
                    for (int c = 0; c < 26; ++c) {
                        perms_with_j /= fact[half_count[c]];
                    }

                    if (current_k <= perms_with_j) {
                        // The k-th permutation lies within this block
                        half_res += (char)('a' + j);
                        break;
                    } else {
                        // Skip this block of permutations
                        current_k -= perms_with_j;
                        half_count[j]++; // Backtrack
                    }
                }
            }
        }

        // Step 4: Reconstruct the full palindromic string
        string rev_half = half_res;
        reverse(rev_half.begin(), rev_half.end());
        
        if (mid_char != 0) {
            return half_res + mid_char + rev_half;
        }
        return half_res + rev_half;
    }
};