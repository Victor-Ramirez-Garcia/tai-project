from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        counts = Counter(s)
        
        # Step 2: Create buckets where the index represents the frequency
        # The maximum possible frequency is the length of the string
        n = len(s)
        buckets = [[] for _ in range(n + 1)]
        
        for char, freq in counts.items():
            buckets[freq].append(char)
            
        # Step 3: Iterate backwards through the buckets to construct the result string
        # This ensures characters with higher frequencies are appended first
        result = []
        for freq in range(n, 0, -1):
            for char in buckets[freq]:
                result.append(char * freq)
                
        # Time Complexity: O(n) - We iterate through the string to count, then the buckets
        # Space Complexity: O(n) - To store the counts, buckets, and the final output
        return "".join(result)