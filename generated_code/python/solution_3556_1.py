from typing import List
import heapq

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Edge case: if multiplier is 1, operations don't change the values
        if multiplier == 1:
            return [x % 1000000007 for x in nums]
            
        MOD = 10**9 + 7
        n = len(nums)
        
        # Min-heap stores tuples of (value, original_index)
        # Python's heapq handles tuples by comparing elements from left to right,
        # which perfectly matches the requirement: sort by value, then by earliest index.
        heap = [(val, i) for i, val in enumerate(nums)]
        heapq.heapify(heap)
        
        # Step 1: Simulate operations until the maximum element in nums 
        # becomes less than or equal to the minimum element * multiplier.
        # This state ensures that all elements have entered a relative cycle where
        # operations will cycle through all elements uniformly.
        max_val = max(nums)
        
        while k > 0 and heap[0][0] * multiplier <= max_val:
            val, idx = heapq.heappop(heap)
            new_val = val * multiplier
            nums[idx] = new_val
            heapq.heappush(heap, (new_val, idx))
            k -= 1
            
        # Step 2: If there are still operations left, they can be distributed 
        # evenly across all elements using fast exponentiation.
        if k > 0:
            # Each element gets at least q additional multiplier applications
            q = k // n
            # The first r elements in the heap get one extra multiplier application
            r = k % n
            
            # Fast exponentiation for the multiplier powers
            pow_q = pow(multiplier, q, MOD)
            pow_q_plus_1 = (pow_q * multiplier) % MOD
            
            # Extract elements from the heap in their exact sorted order of simulation
            sorted_elements = []
            while heap:
                sorted_elements.append(heapq.heappop(heap))
                
            # Apply the calculated powers to the elements based on their cycle position
            for i, (val, idx) in enumerate(sorted_elements):
                if i < r:
                    nums[idx] = (val % MOD * pow_q_plus_1) % MOD
                else:
                    nums[idx] = (val % MOD * pow_q) % MOD
        else:
            # If k reached 0 during Step 1, just apply modulo to all elements
            for i in range(n):
                nums[i] %= MOD
                
        return nums