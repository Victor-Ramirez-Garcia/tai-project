from typing import List
import heapq

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        # Count the frequency of each character already present in the string
        freq = [0] * 26
        for ch in s:
            if ch != '?':
                freq[ord(ch) - ord('a')] += 1
        
        # Count total number of '?' to be replaced
        q_count = s.count('?')
        if q_count == 0:
            return s
            
        # Min-heap to find the character that minimizes the incremental cost.
        # Priority is given by (frequency, character) to ensure we always pick
        # the lowest frequency, and break ties lexicographically.
        heap = [(freq[i], chr(ord('a') + i)) for i in range(26)]
        heapq.heapify(heap)
        
        # Collect the characters that will replace the '?' positions.
        # To minimize the overall value, we greedily pick the best character available.
        chosen_chars = []
        for _ in range(q_count):
            count, ch = heapq.heappop(heap)
            chosen_chars.append(ch)
            # Increment frequency of the chosen character and push it back
            heapq.heappush(heap, (count + 1, ch))
            
        # To guarantee the final string is lexicographically smallest, 
        # the chosen characters must be placed in sorted order across the '?' positions.
        chosen_chars.sort()
        
        # Reconstruct the string by replacing '?' with the sorted chosen characters
        res = list(s)
        idx = 0
        for i in range(len(res)):
            if res[i] == '?':
                res[i] = chosen_chars[idx]
                idx += 1
                
        return "".join(res)