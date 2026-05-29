from itertools import pairwise

class Solution:
    def minOperations(self, s: str) -> int:
        # Time Complexity: O(N) where N is the length of s, as we only perform linear scans.
        # Space Complexity: O(1) auxiliary space.
        
        # Case 1: The string is already fully sorted.
        if all(a <= b for a, b in pairwise(s)):
            return 0
            
        n = len(s)
        # Case 2: If the string has length 2 and is not sorted, we cannot sort it
        # because the only valid operation requires selecting a proper substring (length < 2),
        # which means individual characters cannot be reordered.
        if n == 2:
            return -1
            
        # Identify the smallest and largest characters present in the entire string.
        mn = min(s)
        mx = max(s)
        
        # Case 3: If the first element is already the minimum character or the 
        # last element is already the maximum character, we can sort the remaining 
        # n-1 characters in a single operation.
        if s[0] == mn or s[-1] == mx:
            return 1
            
        # Case 5: If the absolute minimum element is stuck at the last position AND
        # the absolute maximum element is stuck at the first position, it takes 3 operations.
        # Example: s = "d...a" where 'a' is min and 'd' is max.
        # 1. Sort suffix excluding s[0] -> "da..."
        # 2. Sort prefix excluding s[-1] -> "ad..." (moves 'a' to front)
        # 3. Sort suffix excluding s[0] -> "a...d" (moves 'd' to end)
        # We check for this by tracking the first occurrence of min and last occurrence of max.
        min_idx = s.find(mn)
        max_idx = s.rfind(mx)
        if min_idx == n - 1 and max_idx == 0:
            return 3
            
        # Case 4: For all other configurations, we can always sort the string in 2 operations.
        return 2