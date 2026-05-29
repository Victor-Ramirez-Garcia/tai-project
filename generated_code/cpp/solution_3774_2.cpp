#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    // Optimal O(N) solution using Lucas' Theorem and Combinatorics
    bool hasSameDigits(string s) {
        int n = s.length();
        int first_digit_sum = 0;
        int second_digit_sum = 0;
        
        // Precalculate nCr % 10 for all r up to n - 2
        // Using Chinese Remainder Theorem: mod 10 can be derived from mod 2 and mod 5
        // Lookup table where lookup[mod2][mod5] yields the value modulo 10
        static constexpr int lookup[2][5] = {
            {0, 6, 2, 8, 4}, // mod2 == 0
            {5, 1, 7, 3, 9}  // mod2 == 1
        };
        
        int m = n - 2; // The total number of reduction levels needed
        
        for (int i = 0; i <= m; ++i) {
            int mod2 = lucasTheorem(m, i, 2);
            int mod5 = lucasTheorem(m, i, 5);
            int coefficient = lookup[mod2][mod5];
            
            // The contribution of each element to the final two digits
            // follows the binomial coefficient distribution of Pascal's Triangle
            first_digit_sum = (first_digit_sum + coefficient * (s[i] - '0')) % 10;
            second_digit_sum = (second_digit_sum + coefficient * (s[i + 1] - '0')) % 10;
        }
        
        return first_digit_sum == second_digit_sum;
    }

private:
    // Lucas' Theorem allows evaluating (n choose k) % prime in O(log_prime(n)) time
    int lucasTheorem(int n, int k, int prime) {
        int res = 1;
        while (n > 0 || k > 0) {
            int n_digit = n % prime;
            int k_digit = k % prime;
            
            if (k_digit > n_digit) return 0;
            
            res = (res * nCr(n_digit, k_digit)) % prime;
            n /= prime;
            k /= prime;
        }
        return res;
    }

    // Standard nCr calculation for small values (n < prime)
    int nCr(int n, int k) {
        if (k > n) return 0;
        if (k == 0 || k == n) return 1;
        int res = 1;
        for (int i = 0; i < k; ++i) {
            res *= (n - i);
            res /= (i + 1);
        }
        return res;
    }
};