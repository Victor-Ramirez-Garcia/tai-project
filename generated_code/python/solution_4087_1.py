from typing import Set

class Solution:
    def maxDistinct(self, s: str) -> int:
        # Since each substring must start with a distinct character, the maximum 
        # possible number of substrings is bounded by the number of unique characters 
        # present in the string `s`. 
        #
        # Can we always achieve a split equal to the total number of unique characters?
        # Yes. If we iterate from left to right, the very first time we see a character, 
        # we can conceptually start a new substring with it. Any subsequent occurrences 
        # of already-seen characters can simply be appended to the current active 
        # substring without creating a new one. 
        #
        # Because we only create a new substring when we encounter a character for the 
        # first time, every created substring starts with a uniquely identified character. 
        # Thus, the problem reduces to finding the number of unique characters in `s`.
        
        unique_chars: Set[str] = set(s)
        return len(unique_chars)