#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
private:
    // Helper function to calculate combinations (n Choose r) safely up to 2*10^9
    long long nCr(int n, int r) {
        if (r < 0 || r > n) return 0;
        if (r == 0 || r == n) return 1;
        if (r > n / 2) r = n - r; // Optimize calculations
        
        long long res = 1;
        for (int i = 1; i <= r; ++i) {
            // Prevent potential overflows; checking bounds if necessary, 
            // though n will be small enough since max string length is typically small.
            res = res * (n - i + 1) / i;
        }
        return res;
    }

    // Computes the total number of unique permutations of a multinomial coefficient
    // total_permutations = (sum(counts)!) / (counts[0]! * counts[1]! * ...)
    long long get_permutations_count(const vector<int>& counts) {
        int total_elements = 0;
        for (int c : counts) total_elements += c;
        
        long long total_perms = 1;
        int current_n = total_elements;
        
        for (int c : counts) {
            if (c > 0) {
                total_perms *= nCr(current_n, c);
                current_n -= c;
            }
        }
        return total_perms;
    }

public:
    string smallestPalindrome(string s, int k) {
        vector<int> freq(26, 0);
        for (char c : s) {
            freq[c - 'a']++;
        }

        // Validate if a palindrome can be formed
        int odd_count = 0;
        char odd_char = 0;
        vector<int> half_freq(26, 0);
        int half_len = 0;

        for (int i = 0; i < 26; ++i) {
            if (freq[i] % 2 != 0) {
                odd_count++;
                odd_char = 'a' + i;
            }
            half_freq[i] = freq[i] / 2;
            half_len += half_freq[i];
        }

        // A palindrome can have at most one character with an odd frequency
        if (odd_count > 1) {
            return "";
        }

        // Check if the total possible palindromic permutations is less than k
        long long total_palindromes = get_permutations_count(half_freq);
        if (total_palindromes < k) {
            return "";
        }

        // Construct the first half of the k-th lexicographical palindrome using a digit-by-digit/character-by-character approach
        string first_half = "";
        long long target = k;

        for (int i = 0; i < half_len; ++i) {
            for (int j = 0; j < 26; ++j) {
                if (half_freq[j] > 0) {
                    // Try placing character 'a' + j at the current position
                    half_freq[j]--;
                    long long perms_with_this_char = get_permutations_count(half_freq);

                    if (target <= perms_with_this_char) {
                        // The k-th permutation lies within this block
                        first_half += (char)('a' + j);
                        break; // Move to the next position in the string
                    } else {
                        // The k-th permutation is further ahead, skip this block
                        target -= perms_with_this_char;
                        half_freq[j]++; // Backtrack and try the next character
                    }
                }
            }
        }

        // Form the complete palindrome using the first half, the odd character (if any), and the reversed first half
        string second_half = first_half;
        reverse(second_half.begin(), second_half.end());

        if (odd_count == 1) {
            return first_half + odd_char + second_half;
        } else {
            return first_half + second_half;
        }
    }
};