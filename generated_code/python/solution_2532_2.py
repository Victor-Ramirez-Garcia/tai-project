from collections import Counter
from typing import List, Optional

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Count the frequency of each character in the word
        char_counts = Counter(word)
        
        # Try removing one occurrence of each unique character
        for char in char_counts:
            # Decrement the frequency of the current character
            char_counts[char] -= 1
            
            # If the character's count drops to 0, it's completely removed from the set
            if char_counts[char] == 0:
                del char_counts[char]
            
            # Check if all remaining characters have the exact same frequency
            # Using a set of the values gives the unique frequencies present
            if len(set(char_counts.values())) == 1:
                return True
            
            # Backtrack: restore the character's frequency for the next iteration
            char_counts[char] += 1
            
        return False