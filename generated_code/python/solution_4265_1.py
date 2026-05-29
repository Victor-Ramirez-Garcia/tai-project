from typing import List

class Solution:
    def longestBalanced(self, s: str) -> int:
        """
        Intuition:
        A balanced string has an equal number of '0's and '1's. The length of a 
        balanced substring must be 2 * min(count('0'), count('1')) within that 
        substring, because we can always pair up '0's and '1's. 
        
        Since we can perform AT MOST ONE SWAP on the entire string, we can effectively:
        1. Keep the string as is.
        2. Move one '0' from outside our chosen substring to inside it (replacing a '1').
        3. Move one '1' from outside our chosen substring to inside it (replacing a '0').
        4. Swap two elements within the substring (which changes nothing about counts).
        5. Swap an element inside the substring with an identical element outside (changes nothing).
        
        Thus, for any window/substring, the maximum number of '0's we can achieve 
        inside it after at most one swap is:
            max_zeros = zeros_in_window + (1 if total_zeros > zeros_in_window and ones_in_window > 0 else 0)
        Similarly for '1's:
            max_ones = ones_in_window + (1 if total_ones > ones_in_window and zeros_in_window > 0 else 0)
            
        The actual balanceable length for a specific window is 2 * min(max_zeros, max_ones).
        However, the window itself cannot be smaller than this length. In fact, we can just 
        check all possible substrings (or use an optimized sliding window/two-pointer approach) 
        to find the maximum possible balanced length. Given the problem is typical for 
        O(N) or O(N^2), let's optimize using a sliding window or direct check.
        
        Actually, any valid balanced substring of length 2K can be formed if we can get 
        at least K '0's and K '1's in a window of length 2K. 
        Let's find the total counts of '0's and '1's first.
        """
        n = len(s)
        total_0 = s.count('0')
        total_1 = n - total_0
        
        # Max possible balanced length cannot exceed 2 * min(total_0, total_1)
        max_possible_len = 2 * min(total_0, total_1)
        
        # We can binary search the answer (only even lengths) or slide a window.
        # Since we want to maximize the balanced substring, let's check from largest possible even length downwards.
        for length in range(max_possible_len, -1, -2):
            if length == 0:
                return 0
                
            # Count 0s and 1s in the first window of this 'length'
            c0 = s[:length].count('0')
            c1 = length - c0
            
            # Slide the window across the string
            for i in range(n - length + 1):
                if i > 0:
                    # Update counts for the sliding window
                    if s[i - 1] == '0': c0 -= 1
                    else: c1 -= 1
                    if s[i + length - 1] == '0': c0 += 1
                    else: c1 += 1
                
                # Check if we can make this window balanced with at most 1 swap.
                # Case 1: Already balanced
                if c0 == c1:
                    return length
                
                # Case 2: We need one more '0' and we have an available '0' outside, 
                # and we can sacrifice a '1' inside.
                if c0 + 1 == c1 and total_0 > c0:
                    return length
                    
                # Case 3: We need one more '1' and we have an available '1' outside,
                # and we can sacrifice a '0' inside.
                if c1 + 1 == c0 and total_1 > c1:
                    return length
                    
        return 0