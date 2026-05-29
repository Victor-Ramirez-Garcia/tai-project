from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # If multiplier is 1, operations don't change the array values.
        if multiplier == 1:
            return nums
        
        # Initialize a min-heap with tuples of (value, original_index)
        # This naturally handles tracking the minimum value and breaking ties
        # by selecting the smallest index (first occurrence).
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        
        # Perform the k operations
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            new_val = val * multiplier
            nums[idx] = new_val
            heapq.heappush(heap, (new_val, idx))
            
        return nums