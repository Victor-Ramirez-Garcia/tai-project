from collections import Counter
from typing import List

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        # Time Complexity: O(N) where N is the length of the string
        # Space Complexity: O(K) where K is the number of unique characters (K <= 62 for letters/digits)
        counts = Counter(s)
        
        # Step 2: Group characters by their frequency using bucket sort
        # Since the maximum frequency cannot exceed the length of the string,
        # we can use an array of lists where index represents the frequency.
        max_freq = len(s)
        buckets: List[List[str]] = [[] for _ in range(max_freq + 1)]
        
        for char, freq in counts.items():
            buckets[freq].append(char)
            
        # Step 3: Iterate through the buckets in reverse order (highest frequency first)
        # and reconstruct the result string.
        # Overall Time Complexity: O(N)
        # Overall Space Complexity: O(N) to store the output elements
        result = []
        for freq in range(max_freq, 0, -1):
            for char in buckets[freq]:
                result.append(char * freq)
                
        return "".join(result)