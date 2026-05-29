from typing import List
from collections import defaultdict

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Step 1: Group the elements by their bitmask representation.
        # Since we want to maximize the product, for each unique bitmask, 
        # we only care about the largest number that produces that mask.
        mask_to_max_val = defaultdict(int)
        for num in nums:
            if num > mask_to_max_val[num]:
                mask_to_max_val[num] = num
                
        # Convert the map to a list of tuples for faster iteration.
        unique_masks = list(mask_to_max_val.items())
        n = len(unique_masks)
        
        max_product = 0
        
        # Step 2: Compare pairs of masks to find the maximum product 
        # where the bitwise AND between the two masks is 0.
        for i in range(n):
            mask1, val1 = unique_masks[i]
            for j in range(i + 1, n):
                mask2, val2 = unique_masks[j]
                
                # If they do not share any common set bits
                if (mask1 & mask2) == 0:
                    current_product = val1 * val2
                    if current_product > max_product:
                        max_product = current_product
                        
        return max_product