from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        """
        Time Complexity: O(k * log(N)) where N is the length of nums.
        Space Complexity: O(N) to store the heap elements.
        
        Algorithm: We use a Min-Heap to efficiently retrieve and update the minimum element.
        To handle duplicates properly and maintain the original order (first occurrence), 
        we store tuples of (value, index) in the heap.
        """
        # Create a min-heap with tuples of (value, original_index)
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)
        
        # Perform k operations
        for _ in range(k):
            val, i = heapq.heappop(heap)
            new_val = val * multiplier
            nums[i] = new_val
            heapq.heappush(heap, (new_val, i))
            
        return nums