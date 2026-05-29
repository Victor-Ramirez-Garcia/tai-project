from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # If no flowers need to be planted, we are already done.
        if n == 0:
            return True
            
        length = len(flowerbed)
        
        # Greedy Approach: Iterate through the flowerbed and place a flower 
        # whenever a spot and its adjacent spots are empty (0).
        for i in range(length):
            if flowerbed[i] == 0:
                # Check if the left plot is empty or out of bounds
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                # Check if the right plot is empty or out of bounds
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    # Plant a flower here
                    flowerbed[i] = 1
                    n -= 1
                    
                    # Early exit condition if all flowers are successfully planted
                    if n == 0:
                        return True
                        
        return n <= 0