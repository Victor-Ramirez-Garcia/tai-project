from typing import List
from collections import defaultdict

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Map each bitmask to the maximum value that generates this mask.
        # Since multiple numbers can have the same bitmask, we only care about 
        # the maximum number for each distinct mask to maximize the product.
        mask_to_max = defaultdict(int)
        for num in nums:
            mask = 0
            temp = num
            # Compute the bitmask representing which bits are set in num
            while temp > 0:
                mask |= (temp & 1)
                temp >>= 1
            # Alternatively, since num fits within 10^6 (< 2^20), 
            # the mask is simply the number itself because its bit pattern is unique.
            # However, the problem specifies "binary representations do not share any common set bits".
            # The bitmask of a number IS the number itself in binary.
            mask_to_max[num] = max(mask_to_max[num], num)
        
        # Convert map to a list of tuples for efficient O(N^2) iteration over unique masks.
        # Since nums[i] <= 10^6, there are at most 10^6 unique numbers/masks, but practically 
        # bounded by min(N, 10^6). To optimize, we can sort or just iterate.
        masks = list(mask_to_max.items())
        max_prod = 0
        n = len(masks)
        
        # Prune and find the max product of two numbers with disjoint bitmasks
        for i in range(n):
            mask1, val1 = masks[i]
            # Optimization: If val1 multiplied by the largest possible value in the array 
            # cannot beat the current max_prod, we can skip further checks for this i if sorted,
            # or just rely on standard checking. 
            for j in range(i + 1, n):
                mask2, val2 = masks[j]
                # Check if the two bitmasks are disjoint (no common set bits)
                if (mask1 & mask2) == 0:
                    max_prod = max(max_prod, val1 * val2)
                    
        return max_prod