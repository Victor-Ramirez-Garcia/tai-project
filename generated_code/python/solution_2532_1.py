from typing import List
from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Since the constraint on word length is typically small (e.g., length <= 100),
        # a brute-force approach of trying to remove each character one by one is highly efficient.
        # Time Complexity: O(N * K), where N is len(word) and K is the number of unique characters (<= 26).
        # Space Complexity: O(K) to store frequencies.
        
        # Count the initial frequency of each character
        char_counts = Counter(word)
        
        # Try removing one instance of each unique character
        for char in char_counts:
            # Decrement the count of the current character
            char_counts[char] -= 1
            
            # Gather all frequencies that are greater than 0
            remaining_frequencies = [freq for freq in char_counts.values() if freq > 0]
            
            # If all remaining non-zero frequencies are equal, we found a valid removal
            # Using a set to check if there is only 1 unique frequency remaining
            if len(set(remaining_frequencies)) == 1:
                return True
                
            # Backtrack: restore the count for the next iteration
            char_counts[char] += 1
            
        return False