from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # A greedy approach works optimally here. We traverse the flowerbed
        # and plant a flower wherever we find an available empty plot 
        # that satisfies the non-adjacent condition.
        
        count = 0
        length = len(flowerbed)
        
        for i in range(length):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left plot is empty or out of bounds.
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the right plot is empty or out of bounds.
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                # If both adjacent spots are empty, we can plant a flower here.
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    count += 1
                    
                    # Early exit condition if we have already planted enough flowers.
                    if count >= n:
                        return True
                        
        return count >= n