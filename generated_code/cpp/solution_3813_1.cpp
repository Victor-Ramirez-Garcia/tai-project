#include <string>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

class Solution {
private:
    // Helper function to calculate factorials up to n safely.
    // Given string length constraints typically fit within standard limits, 
    // but using long long to prevent overflow during multinomial coefficient calculation.
    vector<long long> getFactorials(int n) {
        vector<long long> fact(n + 1, 1);
        for (int i = 2; i <= n; ++i) {
            // Cap at a large value if it exceeds maximum possible k to prevent overflow
            if (fact[i - 1] > 2e18 / i) {
                fact[i] = 2e18; 
            } else {
                fact[i] = fact[i - 1] * i;
            }
        }
        return fact;
    }

    // Counts the number of distinct permutations possible with the remaining character frequencies
    long long countPermutations(const vector<int>& counts, const vector<long long>& fact) {
        int total = 0;
        for (int c : counts) {
            total += c;
        }
        long long num = fact[total];
        for (int c : counts) {
            if (c > 1) {
                num /= fact[c];
            }
        }
        return num;
    }

public:
    string smallestPalindrome(string s, int k) {
        vector<int> counts(26, 0);
        for (char c : s) {
            counts[c - 'a']++;
        }

        // Validate if a palindrome can be formed
        int odd_count = 0;
        char odd_char = 0;
        for (int i = 0; i < 26; ++i) {
            if (counts[i] % 2 != 0) {
                odd_count++;
                odd_char = 'a' + i;
            }
        }

        // A palindrome can have at most one character with an odd frequency
        if (odd_count > 1) return "";

        // Reduce frequencies to represent only the first half of the palindrome
        vector<int> half_counts(26, 0);
        int half_len = 0;
        for (int i = 0; i < 26; ++i) {
            half_counts[i] = counts[i] / 2;
            half_len += half_counts[i];
        }

        vector<long long> fact = getFactorials(half_len);

        // Check if total possible palindromic permutations is less than k
        long long total_perms = countPermutations(half_counts, fact);
        if (total_perms < k) return "";

        // Construct the first half lexicographically using a next-candidate approach
        string first_half = "";
        long long current_k = k;

        for (int i = 0; i < half_len; ++i) {
            for (int j = 0; j < 26; ++j) {
                if (half_counts[j] > 0) {
                    // Try placing character 'a' + j at the current position
                    half_counts[j]--;
                    long long perms = countPermutations(half_counts, fact);
                    
                    if (current_k <= perms) {
                        // The k-th permutation lies within this character's branch
                        first_half += (char)('a' + j);
                        break;
                    } else {
                        // Skip all permutations starting with this character
                        current_k -= perms;
                        half_counts[j]++; // Backtrack
                    }
                }
            }
        }

        // Form the full palindrome from the first half, the odd middle character (if any),
        // and the reversed first half.
        string second_half = first_half;
        reverse(second_half.begin(), second_half.end());
        
        if (odd_count == 1) {
            return first_half + odd_char + second_half;
        }
        return first_half + second_half;
    }
};