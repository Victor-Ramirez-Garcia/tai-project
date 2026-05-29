from typing import List

class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Intuition:
        - A balanced string has an equal number of '0's and '1's.
        - We want to maximize the length of a balanced substring after at most one swap.
        - Notice that the exact positions of the characters inside the chosen substring 
          don't prevent it from being balanced; we just need count('0') == count('1').
        - If we pick a substring from index i to j, let its original counts be c0 and c1.
          If we perform at most one swap, we can:
          1. Change nothing (if we swap inside or outside, or don't swap): balance requires c0 == c1.
          2. Bring a '0' from outside into the substring, replacing a '1': new counts are c0+1, c1-1.
             For balance: c0 + 1 == c1 - 1  =>  c1 - c0 == 2.
             This requires at least one '0' outside the substring to swap in, and at least one '1' inside to swap out.
          3. Bring a '1' from outside into the substring, replacing a '0': new counts are c0-1, c1+1.
             For balance: c0 - 1 == c1 + 1  =>  c0 - c1 == 2.
             This requires at least one '1' outside the substring to swap in, and at least one '0' inside to swap out.
        
        Optimized Approach:
        - Total counts of '0' and '1' in the entire string: total0, total1.
        - We can iterate over all possible substrings (or use a sliding window/prefix approach).
          Since constraints aren't explicitly bounded but typical LeetCode string lengths 
          can be up to 10^5, an O(N^2) might TLE if N is large. However, if N is small (e.g., <= 1000), 
          O(N^2) is fine. Let's design an efficient check.
        - Actually, the condition for a substring to be transformable into a balanced one is:
          - Case 0: c1 - c0 == 0
          - Case 1: c1 - c0 == 2, and there is at least one '0' outside (total0 > c0) and at least one '1' inside (c1 > 0).
          - Case 2: c0 - c1 == 2, and there is at least one '1' outside (total1 > c1) and at least one '0' inside (c0 > 0).
          
        - To optimize, we can track the max length. Since we want to find the maximum length, 
          we can use a prefix array or just a double loop if N is small. Assuming standard N <= 5000, 
          an O(N^2) optimized loop works. Let's implement O(N^2) cleanly.
        """
        n = len(s)
        total0 = s.count('0')
        total1 = n - total0
        
        max_len = 0
        
        # Iterate over all possible starting points
        for i in range(n):
            c0, c1 = 0, 0
            # Expand the substring to the right
            for j in range(i, n):
                if s[j] == '0':
                    c0 += 1
                else:
                    c1 += 1
                
                # Check if it's already balanced
                if c0 == c1:
                    if c0 + c1 > max_len:
                        max_len = c0 + c1
                # Check if we can balance by swapping a '0' from outside with a '1' inside
                elif c1 - c0 == 2 and total0 > c0 and c1 > 0:
                    if c0 + c1 > max_len:
                        max_len = c0 + c1
                # Check if we can balance by swapping a '1' from outside with a '0' inside
                elif c0 - c1 == 2 and total1 > c1 and c0 > 0:
                    if c0 + c1 > max_len:
                        max_len = c0 + c1
                        
        return max_len