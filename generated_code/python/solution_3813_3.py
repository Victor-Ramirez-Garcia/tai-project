from collections import Counter
from math import factorial
from typing import List

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        # Step 1: Count character frequencies
        counts = Counter(s)
        
        # Step 2: Validate if a palindrome can be formed
        odd_chars = [char for char, count in counts.items() if count % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        # Determine the middle character if it exists
        mid_char = odd_chars[0] if odd_chars else ""
        
        # Step 3: Construct the pool of characters for the first half
        half_chars = []
        for char in sorted(counts.keys()):
            half_chars.extend([char] * (counts[char] // 2))
            
        # Helper function to compute permutations with repetitions
        # Total permutations = N! / (c1! * c2! * ... * cm!)
        def count_permutations(char_list: List[str]) -> int:
            if not char_list:
                return 1
            total_len = len(char_list)
            freq = Counter(char_list)
            ans = factorial(total_len)
            for count in freq.values():
                ans //= factorial(count)
            return ans

        # Step 4: Reconstruct the k-th permutation element by element
        # We work on building the first half of the palindrome lexicographically
        first_half = []
        remaining_chars = half_chars[:]
        
        # We need to find the k-th permutation (1-indexed)
        target = k
        
        while remaining_chars:
            # Try to place each unique available character at the current position
            unique_chars = sorted(list(set(remaining_chars)))
            placed = False
            
            for char in unique_chars:
                # Create a temporary list mimicking the remaining pool if 'char' is picked
                next_remaining = remaining_chars[:]
                next_remaining.remove(char)
                
                # Count how many permutations can be formed with the remaining characters
                perms_with_char = count_permutations(next_remaining)
                
                if target <= perms_with_char:
                    # The target permutation lies within the branch starting with 'char'
                    first_half.append(char)
                    remaining_chars = next_remaining
                    placed = True
                    break
                else:
                    # Skip all permutations starting with this 'char'
                    target -= perms_with_char
            
            # If no character could be placed, it means k is out of bounds
            if not placed:
                return ""
                
        # If target is still greater than 1 after exhausting choices, k was too large
        if target > 1:
            return ""
            
        # Step 5: Construct the full palindrome from the first half
        first_half_str = "".join(first_half)
        return first_half_str + mid_char + first_half_str[::-1]