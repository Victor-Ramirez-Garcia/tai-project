from typing import List
import heapq

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        # Count the current frequency of each character in the string
        freq = [0] * 26
        question_count = 0
        for ch in s:
            if ch == '?':
                question_count += 1
            else:
                freq[ord(ch) - ord('a')] += 1
        
        # If there are no '?' characters, return the original string
        if question_count == 0:
            return s
        
        # Min-heap to always pick the character with the minimum current frequency.
        # Elements are tuples: (frequency, character_index) to naturally prioritize
        # smaller frequencies first, and lexicographically smaller characters on ties.
        heap = [(freq[i], i) for i in range(26)]
        heapq.heapify(heap)
        
        # Collect the best characters to replace the '?' symbols
        chosen_chars = []
        for _ in range(question_count):
            count, idx = heapq.heappop(heap)
            chosen_chars.append(chr(ord('a') + idx))
            # Push the updated frequency back into the heap
            heapq.heappush(heap, (count + 1, idx))
            
        # To ensure the final string is lexicographically smallest overall,
        # the chosen characters must be placed in sorted order across the '?' positions.
        chosen_chars.sort()
        
        # Reconstruct the string by replacing '?' with the sorted chosen characters
        ans = []
        ptr = 0
        for ch in s:
            if ch == '?':
                ans.append(chosen_chars[ptr])
                ptr += 1
            else:
                ans.append(ch)
                
        return "".join(ans)