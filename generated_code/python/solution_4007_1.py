from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        """
        To find the maximum total value of exactly k distinct subarrays, we can 
        efficiently find the top k largest subarray values.
        
        The value of a subarray nums[l..r] is defined as max(nums[l..r]) - min(nums[l..r]).
        There are O(n^2) possible subarrays. Since n can be large, we can optimize the 
        process of finding the largest subarray values. 
        
        However, for a general constraint up to a reasonable limit, we can precompute or 
        generate subarray values. For each element nums[i], we can find the maximum and 
        minimum elements of subarrays starting at i and extending to the right.
        
        Using a Min-Heap of size k, we can maintain the k largest values. 
        Time Complexity: O(n^2 * log(k)) to iterate through all subarrays and maintain the heap.
        Space Complexity: O(k) for the min-heap.
        """
        n = len(nums)
        min_heap = []
        
        # Iterate over all possible subarrays
        for i in range(n):
            current_max = nums[i]
            current_min = nums[i]
            for j in range(i, n):
                if nums[j] > current_max:
                    current_max = nums[j]
                if nums[j] < current_min:
                    current_min = nums[j]
                
                val = current_max - current_min
                
                # Maintain exactly the k largest elements in the min-heap
                if len(min_heap) < k:
                    heapq.heappush(min_heap, val)
                elif val > min_heap[0]:
                    heapq.heappushpop(min_heap, val)
                    
        # The sum of the k largest elements is our answer
        return sum(min_heap)