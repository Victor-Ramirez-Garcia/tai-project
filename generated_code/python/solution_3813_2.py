from typing import List, Dict
from collections import Counter
import math

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        counts = Counter(s)
        
        # Step 2: Validate if a palindrome can be formed
        # At most one character can have an odd count
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        # Determine the middle character if it exists
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Step 3: Construct the pool of characters for the first half
        # Sorting ensures we can build the palindrome lexicographically
        half_chars = []
        for char in sorted(counts.keys()):
            half_chars.extend([char] * (counts[char] // 2))
            
        n = len(half_chars)
        
        # Precompute frequencies of characters in the first half to calculate permutations
        half_counts = Counter(half_chars)
        
        # Helper to compute total unique permutations for a given remaining frequency map
        def get_total_permutations(f_map: Dict[str, int], total_len: int) -> int:
            if total_len == 0:
                return 1
            ans = math.factorial(total_len)
            for count in f_map.values():
                if count > 1:
                    ans //= math.factorial(count)
            return ans

        # Step 4: Digit-by-digit (or character-by-character) construction of the first half
        # We try to place the smallest available character at the current position.
        # If the number of permutations possible with that choice is less than k, 
        # we skip all those permutations, subtract the count from k, and try the next character.
        first_half = []
        remaining_len = n
        
        # Track unique sorted keys available for correct ordering during iteration
        unique_sorted_chars = sorted(half_counts.keys())
        
        for i in range(n):
            placed = False
            for char in unique_sorted_chars:
                if half_counts[char] == 0:
                    continue
                
                # Try placing 'char' at index i
                half_counts[char] -= 1
                
                # Calculate how many permutations can be formed with the remaining characters
                perms = get_total_permutations(half_counts, remaining_len - 1)
                
                if k <= perms:
                    # The k-th permutation lies within this character's branch
                    first_half.append(char)
                    remaining_len -= 1
                    placed = True
                    break
                else:
                    # Skip all permutations starting with this character
                    k -= perms
                    half_counts[char] += 1  # Backtrack
            
            # If we couldn't place any character, k is out of bounds
            if not placed:
                return ""
        
        # If after placing all characters, k is still greater than 1, then k is out of bounds
        if k > 1:
            return ""
            
        # Step 5: Reconstruct the full palindrome from the first half
        first_half_str = "".join(first_half)
        return first_half_str + mid_char + first_half_str[::-1]