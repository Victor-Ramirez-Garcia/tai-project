from typing import List
import heapq

class Solution:
    def minimizeStringValue(self, s: str) -> str:
        # Count frequencies of existing characters in the string
        freq = [0] * 26
        question_count = 0
        for char in s:
            if char == '?':
                question_count += 1
            else:
                freq[ord(char) - ord('a')] += 1
        
        # If there are no '?' characters, return the string as is
        if question_count == 0:
            return s
        
        # Min-heap to choose characters that minimize the incremental cost.
        # Elements are tuples: (frequency, character_index)
        # This naturally prioritizes lower frequencies first, and breaks ties lexicographically.
        heap = [(freq[i], i) for i in range(26)]
        heapq.heapify(heap)
        
        # Determine which characters will replace the '?'s
        chosen_chars = []
        for _ in range(question_count):
            count, idx = heapq.heappop(heap)
            chosen_chars.append(chr(ord('a') + idx))
            # Push the updated frequency back into the heap
            heapq.heappush(heap, (count + 1, idx))
            
        # To make the final string lexicographically smallest, the chosen 
        # replacement characters must be sorted before inserting them back.
        chosen_chars.sort()
        
        # Reconstruct the string by replacing '?' with the sorted chosen characters
        result = []
        chosen_ptr = 0
        for char in s:
            if char == '?':
                result.append(chosen_chars[chosen_ptr])
                chosen_ptr += 1
            else:
                result.append(char)
                
        return "".join(result)