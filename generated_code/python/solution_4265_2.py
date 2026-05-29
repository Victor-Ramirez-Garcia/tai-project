from typing import List

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        total_zeros = s.count('0')
        total_ones = n - total_zeros
        
        # If the string is already completely balanced, no swap is needed.
        if total_zeros == total_ones:
            return n
            
        max_len = 0
        
        # Precompute the prefix balances.
        # balance[i] = (count of '1's in s[0...i-1]) - (count of '0's in s[0...i-1])
        # We store the first occurrence of each balance value to find the longest subarray.
        # Since balance values range from -n to n, we can use an array of size 2n + 1
        # shifted by n to avoid dictionary overhead.
        OFFSET = n
        
        # To handle the "at most one swap" condition efficiently, we can observe that 
        # a swap changes the counts of '0's and '1's in a substring by at most 2.
        # Alternatively, we can check for each possible balance value.
        # However, a robust approach for "at most one swap" to maximize a balanced substring:
        # A substring s[i...j] can be made balanced via at most one swap if:
        # 1. It is already balanced: zeros == ones
        # 2. It has excess of two '1's (ones == zeros + 2) AND there is a '0' inside and a '1' outside.
        # 3. It has excess of two '0's (zeros == ones + 2) AND there is a '1' inside and a '0' outside.
        
        # Let's track the first and last occurrence of each prefix balance.
        # balance = ones - zeros
        first_occ = [-1] * (2 * n + 1)
        first_occ[0 + OFFSET] = 0
        
        curr_bal = 0
        for i, ch in enumerate(s):
            curr_bal += 1 if ch == '1' else -1
            
            # Case 1: Already perfectly balanced substring ending at i
            # Target prefix balance matches curr_bal
            if first_occ[curr_bal + OFFSET] != -1:
                max_len = max(max_len, i + 1 - first_occ[curr_bal + OFFSET])
            else:
                first_occ[curr_bal + OFFSET] = i + 1
                
        # To account for a single swap, a substring can achieve balance if its initial
        # balance (ones - zeros) is +2 or -2, provided the required characters exist 
        # outside to swap with. 
        # Specifically, if balance is +2 (two extra 1s), we need at least one '0' inside 
        # and at least one '1' outside. If the whole string has at least one '1', 
        # and the substring has a '0', a swap is valid.
        
        # We can scan all pairs or use a sliding window/prefix approach. Given constraints 
        # are typically up to 10^5 for such string problems, an O(N) or O(N log N) is needed.
        # Let's find the max length for target balances: 0, 2, -2.
        
        # Track first occurrences again for flexible lookups
        first_bal = [-1] * (2 * n + 1)
        first_bal[0 + OFFSET] = 0
        
        curr_bal = 0
        for i, ch in enumerate(s):
            curr_bal += 1 if ch == '1' else -1
            
            # Check for target balance = curr_bal - 2 (meaning subarray has two extra 1s)
            # We want to find the earliest j such that curr_bal - balance[j] == 2 -> balance[j] = curr_bal - 2
            t1 = curr_bal - 2
            if 0 <= t1 + OFFSET <= 2 * n and first_bal[t1 + OFFSET] != -1:
                j = first_bal[t1 + OFFSET]
                # Subarray is s[j:i+1]. It has two extra '1's.
                # Valid swap if it contains at least one '0' and the outside contains at least one '1'.
                # Outside contains a '1' if total_ones > ones_inside.
                # Since ones_inside - zeros_inside == 2 and ones_inside + zeros_inside == i + 1 - j:
                # 2 * ones_inside = i + 1 - j + 2 -> ones_inside = (i + 1 - j + 2) // 2
                # zeros_inside = (i + 1 - j - 2) // 2
                if (i + 1 - j) >= 2:
                    zeros_inside = (i + 1 - j - 2) // 2
                    ones_inside = (i + 1 - j + 2) // 2
                    if zeros_inside > 0 and total_ones > ones_inside:
                        max_len = max(max_len, i + 1 - j)
                        
            # Check for target balance = curr_bal + 2 (meaning subarray has two extra 0s)
            # balance[j] = curr_bal + 2
            t2 = curr_bal + 2
            if 0 <= t2 + OFFSET <= 2 * n and first_bal[t2 + OFFSET] != -1:
                j = first_bal[t2 + OFFSET]
                if (i + 1 - j) >= 2:
                    ones_inside = (i + 1 - j - 2) // 2
                    zeros_inside = (i + 1 - j + 2) // 2
                    if ones_inside > 0 and total_zeros > zeros_inside:
                        max_len = max(max_len, i + 1 - j)
            
            if first_bal[curr_bal + OFFSET] == -1:
                first_bal[curr_bal + OFFSET] = i + 1

        # Corner case: If max_len is still 0 but we have both '0' and '1' in the string, 
        # the minimum balanced substring length we can always form is 2.
        if max_len == 0 and total_zeros > 0 and total_ones > 0:
            return 2
            
        return max_len