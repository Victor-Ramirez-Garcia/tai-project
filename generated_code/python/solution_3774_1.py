from typing import List

class Solution:
    def hasSameDigits(self, s: str) -> bool:
        """
        The process of repeatedly taking adjacent sums modulo 10 is equivalent to 
        finding the coefficients of the digits using Pascal's triangle (combinations).
        For a string of length n, reducing it down to 2 digits means we perform the 
        operation n - 2 times.
        
        The first final digit (left) is a combination of the first n-1 digits:
        left = sum( C(n-2, i) * s[i] ) % 10 for i from 0 to n-2
        
        The second final digit (right) is a combination of the last n-1 digits:
        right = sum( C(n-2, i) * s[i+1] ) % 10 for i from 0 to n-2
        
        Since we need the results modulo 10, and 10 is not prime (10 = 2 * 5), 
        we can compute the binomial coefficients modulo 2 and modulo 5 separately 
        using Lucas' Theorem, and then combine them using the Chinese Remainder Theorem (CRT).
        
        Time Complexity: O(n) to iterate through the string and compute the combinations.
        Space Complexity: O(1) auxiliary space.
        """
        n = len(s)
        m = n - 2
        
        # Precompute small combinations for Lucas' Theorem
        # nCr % 2 table
        c2 = [[0] * 2 for _ in range(2)]
        for i in range(2):
            c2[i][0] = 1
            for j in range(1, i + 1):
                c2[i][j] = (c2[i-1][j-1] + c2[i-1][j]) % 2
                
        # nCr % 5 table
        c5 = [[0] * 5 for _ in range(5)]
        for i in range(5):
            c5[i][0] = 1
            for j in range(1, i + 1):
                c5[i][j] = (c5[i-1][j-1] + c5[i-1][j]) % 5

        def nCr_mod_p(n: int, r: int, p: int, table: List[List[int]]) -> int:
            # Lucas' Theorem: nCr % p = Product( n_i C r_i % p )
            ans = 1
            while n > 0 or r > 0:
                ni = n % p
                ri = r % p
                if ri > ni:
                    return 0
                ans = (ans * table[ni][ri]) % p
                n //= p
                r //= p
            return ans

        # Chinese Remainder Theorem for combining mod 2 and mod 5 to mod 10
        # x % 2 = r2, x % 5 = r5 -> x % 10
        # By inspection: x = (r2 * 5 * 1 + r5 * 2 * 3) % 10 = (5 * r2 + 6 * r5) % 10
        def crt_2_5(r2: int, r5: int) -> int:
            return (5 * r2 + 6 * r5) % 10

        left_sum = 0
        right_sum = 0
        
        # Calculate the contributions of each digit
        for i in range(m + 1):
            r2 = nCr_mod_p(m, i, 2, c2)
            r5 = nCr_mod_p(m, i, 5, c5)
            coeff = crt_2_5(r2, r5)
            
            left_sum = (left_sum + coeff * int(s[i])) % 10
            right_sum = (right_sum + coeff * int(s[i+1])) % 10
            
        return left_sum == right_sum