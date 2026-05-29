from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # If multiplier is 1, operations don't change the elements' values
        if multiplier == 1:
            return nums
            
        # Create a min-heap storing tuples of (value, index)
        # This handles finding the minimum value, and breaks ties by the smallest index
        heap = [(val, idx) for idx, val in enumerate(nums)]
        heapq.heapify(heap)
        
        # Perform k operations
        for _ in range(k):
            val, idx = heapq.heappop(heap)
            new_val = val * multiplier
            nums[idx] = new_val
            heapq.heappush(heap, (new_val, idx))
            
        return nums