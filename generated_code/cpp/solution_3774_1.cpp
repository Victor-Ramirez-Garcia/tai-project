#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool hasSameDigits(string s) {
        int n = s.length();
        int num1 = 0;
        int num2 = 0;
        
        // This is equivalent to finding the contribution of each element to the 
        // final two digits. The transformation follows Pascal's triangle.
        // For a string of length n, the final two elements are sums of s[i] * C(n-2, i) mod 10.
        // We compute C(n-2, i) mod 10 using Lucas' Theorem for primes 2 and 5, then combine using CRT.
        for (int i = 0; i <= n - 2; ++i) {
            int coefficient = nCkMod10(n - 2, i);
            
            num1 = (num1 + coefficient * (s[i] - '0')) % 10;
            num2 = (num2 + coefficient * (s[i + 1] - '0')) % 10;
        }
        
        return num1 == num2;
    }

private:
    // Returns nCr % 10 using the Chinese Remainder Theorem (CRT) with Lucas' Theorem.
    int nCkMod10(int n, int k) {
        int mod2 = lucasTheorem(n, k, 2);
        int mod5 = lucasTheorem(n, k, 5);
        
        // Lookup table combining mod 2 and mod 5 answers via CRT
        // lookup[mod2][mod5]
        static constexpr int lookup[2][5] = {
            {0, 6, 2, 8, 4}, // mod2 == 0
            {5, 1, 7, 3, 9}  // mod2 == 1
        };
        
        return lookup[mod2][mod5];
    }

    // Lucas' Theorem computes (nCr) % prime in O(log_prime(n)) time
    int lucasTheorem(int n, int k, int prime) {
        int res = 1;
        while (n > 0 || k > 0) {
            int nMod = n % prime;
            int kMod = k % prime;
            
            if (kMod > nMod) return 0; // nCr is 0 if r > n
            
            res = (res * nCk(nMod, kMod)) % prime;
            
            n /= prime;
            k /= prime;
        }
        return res;
    }

    // Simple nCr for small values (since arguments are bounded by the prime base)
    int nCk(int n, int k) {
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