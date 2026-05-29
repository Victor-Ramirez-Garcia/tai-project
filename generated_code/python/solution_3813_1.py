from typing import List, Dict
from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Count frequencies of each character
        counts = Counter(s)
        
        # A palindrome can have at most one character with an odd count
        odd_char = ""
        half_counts = {}
        for char, count in counts.items():
            if count % 2 != 0:
                if odd_char:
                    return "" # More than one odd character means no palindrome can be formed
                odd_char = char
            half_counts[char] = count // 2
            
        # Get the unique characters sorted lexicographically for the first half
        unique_chars = sorted(half_counts.keys())
        
        # Calculate the total number of permutations possible for the half-string
        # Formula: total_length! / (count1! * count2! * ...)
        half_length = sum(half_counts.values())
        
        def get_total_permutations(freq: Dict[str, int], total_len: int) -> int:
            ans = math.factorial(total_len)
            for count in freq.values():
                ans //= math.factorial(count)
            return ans
            
        total_perms = get_total_permutations(half_counts, half_length)
        if k > total_perms:
            return "" # Fewer than k distinct palindromic permutations exist
            
        # Reconstruct the first half lexicographically character by character (Digit DP / Combinatorics approach)
        first_half = []
        remaining_len = half_length
        k_remaining = k
        
        for i in range(half_length):
            for char in unique_chars:
                if half_counts[char] > 0:
                    # If we pick 'char' for the current position, calculate how many permutations 
                    # can be formed with the remaining characters
                    half_counts[char] -= 1
                    perms_with_char = get_total_permutations(half_counts, remaining_len - 1)
                    
                    if k_remaining <= perms_with_char:
                        # The k-th permutation lies within the combinations starting with 'char'
                        first_half.append(char)
                        remaining_len -= 1
                        break
                    else:
                        # Skip all permutations starting with 'char' and look into the next character
                        k_remaining -= perms_with_char
                        half_counts[char] += 1 # Backtrack
                        
        # Construct the final full palindrome
        first_half_str = "".join(first_half)
        return first_half_str + odd_char + first_half_str[::-1]