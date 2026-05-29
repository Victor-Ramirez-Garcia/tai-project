from typing import List
from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Since the length of the word is small (typically <= 100 for this problem),
        # we can simulate the removal of each character one by one.
        # This brute-force approach is highly optimal, straightforward, and avoids complex edge cases.
        for i in range(len(word)):
            # Create a new string with the i-th character removed
            new_word = word[:i] + word[i+1:]
            
            # Count frequencies of the remaining characters
            counts = Counter(new_word)
            
            # If all remaining characters have the exact same frequency,
            # then the set of their unique frequencies will have a size of 1.
            if len(set(counts.values())) == 1:
                return True
                
        return False