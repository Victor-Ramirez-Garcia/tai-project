from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Edge case: If multiplier is 1, operations do not change the array values.
        if multiplier == 1:
            return [x % 1_000_000_007 for x in nums]
        
        MOD = 1_000_000_007
        n = len(nums)
        
        # Max value in the original array to find the threshold when all elements 
        # have been multiplied enough to preserve their relative order.
        max_val = max(nums)
        
        # Create a min-heap storing tuples of (value, index) to always extract the minimum element.
        # If values are equal, the smaller index is picked first.
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)
        
        # Phase 1: Simulate step-by-step until the smallest element reaches or exceeds max_val,
        # or we run out of the k operations.
        while k > 0 and heap[0][0] * multiplier <= max_val * multiplier:
            val, idx = heapq.heappop(heap)
            val *= multiplier
            nums[idx] = val
            heapq.heappush(heap, (val, idx))
            k -= 1
            
        # If we exhausted k during the simulation, nums matches the current heap state.
        if k == 0:
            return [x % MOD for x in nums]
            
        # Phase 2: Now the elements maintain their relative order.
        # Each element will undergo either q or q + 1 further multiplications.
        q, r = divmod(k, n)
        
        # Sort the elements based on their current values (and original indices for tie-breaking)
        # to determine which elements get the extra (q + 1)-th multiplication.
        sorted_elements = sorted(heap)
        
        # Fast exponentiation for multiplier^q % MOD
        pow_q = pow(multiplier, q, MOD)
        pow_q_plus_1 = (pow_q * multiplier) % MOD
        
        # Update the final values in the array
        for i, (val, idx) in enumerate(sorted_elements):
            # The first r elements in sorted order get multiplier^(q + 1)
            # The remaining elements get multiplier^q
            m = pow_q_plus_1 if i < r else pow_q
            nums[idx] = (val % MOD * m) % MOD
            
        return nums