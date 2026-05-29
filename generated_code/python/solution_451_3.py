from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        # Time Complexity: O(N) where N is the length of the string
        counts = Counter(s)
        
        # Step 2: Sort the unique characters based on their frequency in decreasing order
        # Since the alphabet size is bounded (at most 62 unique characters for letters/digits),
        # this sorting step takes O(K log K) where K <= 62, which is O(1) constant time.
        sorted_chars = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Reconstruct the string by repeating each character by its frequency
        # Time Complexity: O(N) to build and join the list of string fragments
        return "".join(char * freq for char, freq in sorted_chars)