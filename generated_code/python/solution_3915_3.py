from typing import List
from collections import defaultdict

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Step 1: Map each unique bitmask to the maximum number that produces it.
        # Since nums[i] <= 10^6, its binary representation fits within 20 bits.
        # Grouping by mask optimizes the search space significantly.
        max_for_mask = defaultdict(int)
        for num in nums:
            if num > max_for_mask[num]:
                max_for_mask[num] = num
        
        # Step 2: Extract the unique masks and sort them by value descending
        # to maximize the chance of finding larger products early.
        masks = sorted(max_for_mask.keys(), key=lambda x: max_for_mask[x], reverse=True)
        
        max_product = 0
        n = len(masks)
        
        # Step 3: Compare pairs of masks.
        # If the product of the current pair's values cannot beat the global maximum,
        # we can prune the inner loop early because the values are sorted descending.
        for i in range(n):
            val_i = max_for_mask[masks[i]]
            
            # Pruning: if squaring the current largest value cannot exceed max_product,
            # no subsequent pairs can possibly beat it.
            if val_i * val_i <= max_product:
                break
                
            for j in range(i + 1, n):
                mask_i = masks[i]
                mask_j = masks[j]
                val_j = max_for_mask[mask_j]
                
                # Pruning: if the product with the current val_j is less than or
                # equal to max_product, further elements in the j loop will be even smaller.
                if val_i * val_j <= max_product:
                    break
                
                # Check if the two numbers share no common set bits
                if (mask_i & mask_j) == 0:
                    max_product = max(max_product, val_i * val_j)
                    
        return max_product