from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Edge case: if multiplier is 1, operations don't change the values.
        if multiplier == 1:
            return [x % 1_000_000_007 for x in nums]
            
        MOD = 1_000_000_007
        n = len(nums)
        
        # Create a min-heap storing pairs of (value, original_index)
        # Python's heapq handles tuples by comparing the first element,
        # and if equal, comparing the second element (stable matching for earliest index).
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)
        
        # Step 1: Simulate using the heap until the minimum element has been 
        # multiplied enough to become >= the original maximum element.
        # This aligns the elements so they maintain a predictable cycle.
        max_val = max(nums)
        
        while k > 0 and heap[0][0] * multiplier <= max_val:
            val, i = heapq.heappop(heap)
            new_val = val * multiplier
            heapq.heappush(heap, (new_val, i))
            k -= 1
            
        # If there are still remaining operations, we can distribute them efficiently.
        # At this point, the heap elements are ordered such that simulating 
        # exactly n operations would multiply every element by the multiplier exactly once.
        if k > 0:
            # Sort the heap elements to find their relative order after alignment.
            # Elements are sorted by current value, then by index.
            sorted_elements = sorted(heap)
            
            # Each element will complete at least (k // n) full cycles of multiplication.
            cycles = k // n
            rem = k % n
            
            # Compute multiplier^cycles % MOD using fast exponentiation
            pow_cycles = pow(multiplier, cycles, MOD)
            # Compute multiplier^(cycles + 1) % MOD for the remaining elements
            pow_cycles_plus_one = (pow_cycles * multiplier) % MOD
            
            # The first 'rem' elements in the sorted order get one extra multiplication.
            for i in range(n):
                val, idx = sorted_elements[i]
                if i < rem:
                    nums[idx] = (val % MOD) * pow_cycles_plus_one % MOD
                else:
                    nums[idx] = (val % MOD) * pow_cycles % MOD
        else:
            # If k reached 0 during the initial simulation, extract values from the heap.
            while heap:
                val, i = heapq.heappop(heap)
                nums[i] = val % MOD
                
        return nums