from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # If no flowers need to be planted, we are automatically successful.
        if n == 0:
            return True
            
        length = len(flowerbed)
        
        # Greedy approach: Iterate through the flowerbed and place a flower 
        # whenever we encounter a valid empty plot.
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the left plot is empty or if it's the start of the bed.
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the right plot is empty or if it's the end of the bed.
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                # If both sides are clear, we can plant a flower here.
                if left_empty and right_empty:
                    flowerbed[i] = 1
                    n -= 1
                    
                    # Early exit if we have successfully planted all required flowers.
                    if n == 0:
                        return True
                        
        return n <= 0