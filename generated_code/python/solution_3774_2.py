import math
from typing import List

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """
        Calculates the final two remaining digits of a Pascal's triangle-like 
        reduction modulo 10.
        
        The problem reduces a sequence of length n down to 2 digits.
        The reduction operation is equivalent to a linear combination of the 
        original elements using binomial coefficients.
        
        Specifically, for a sequence of length n, the reduction down to 2 digits 
        means the first of the two final digits, num1, is formed by elements from 
        index 0 to n-2, and the second digit, num2, is formed by elements from 
        index 1 to n-1. Both use the binomial coefficients C(n-2, i).
        
        To compute C(n-2, i) % 10 efficiently:
        Since 10 = 2 * 5 (not a prime power), we compute C(n-2, i) % 2 and 
        C(n-2, i) % 5 independently using Lucas' Theorem, and then apply the 
        Chinese Remainder Theorem (CRT) via a fast lookup table.
        
        Time Complexity: O(n log n) or O(n) depending on Lucas' Theorem calls.
        Space Complexity: O(1) auxiliary storage.
        """
        n = len(s)
        num1 = 0
        num2 = 0
        m = n - 2  # The upper index for the binomial coefficients
        
        # Precomputed lookup table for CRT combining mod 2 and mod 5 answers to mod 10
        # lookup[mod2][mod5] -> maps to value in 0..9
        lookup = [
            [0, 6, 2, 8, 4], # mod2 == 0
            [5, 1, 7, 3, 9]  # mod2 == 1
        ]
        
        # Lucas' Theorem for prime 5 requires small factorials
        fact_mod5 = [1, 1, 2, 6, 24]
        
        def lucas_mod5(n: int, k: int) -> int:
            res = 1
            while n > 0 or k > 0:
                n_mod = n % 5
                k_mod = k % 5
                if k_mod > n_mod:
                    return 0
                # C(n_mod, k_mod) % 5
                # Simple computation for small n_mod, k_mod
                val = fact_mod5[n_mod] // (fact_mod5[k_mod] * fact_mod5[n_mod - k_mod])
                res = (res * val) % 5
                n //= 5
                k //= 5
            return res

        for i in range(n - 1):
            # Compute C(m, i) % 2 using Kummer's / Lucas' Theorem condition
            # For prime 2, C(m, i) % 2 is 1 if and only if (i & ~m) == 0
            mod2 = 1 if (i & ~m) == 0 else 0
            
            # Compute C(m, i) % 5 using Lucas' Theorem
            mod5 = lucas_mod5(m, i)
            
            # Combine via CRT lookup table
            coefficient = lookup[mod2][mod5]
            
            # Accumulate the contribution of each character
            num1 = (num1 + coefficient * int(s[i])) % 10
            num2 = (num2 + coefficient * int(s[i + 1])) % 10
            
        return num1 == num2