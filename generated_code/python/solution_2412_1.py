from typing import List
import math

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        """
        Algorithm Explanation:
        This is a greedy matchmaking problem. We want to maximize the number of pairs 
        we can eliminate each second. 
        
        Let the total sum of elements be `total_sum` and the maximum element be `max_val`.
        There are two scenarios:
        1. If the largest element is greater than the sum of the other two elements 
           (i.e., max_val >= total_sum - max_val), we can pair the other elements with 
           the largest one as much as possible. Once the other two are depleted, we 
           fill the remaining of the largest element one by one. The total seconds 
           will simply be `max_val`.
        2. If the largest element is less than the sum of the other two, we can always 
           pair up elements perfectly (or leave at most 1 element unpaired at the end). 
           In this case, we can fill 2 cups every second as long as possible, resulting 
           in ceil(total_sum / 2) seconds.
           
        Complexity:
        - Time Complexity: O(1) as the input array size is fixed at 3.
        - Space Complexity: O(1) auxiliary space.
        """
        max_val = max(amount)
        total_sum = sum(amount)
        
        # Scenario 1: The largest element dominates
        if max_val >= total_sum - max_val:
            return max_val
        
        # Scenario 2: Elements are balanced enough to be paired efficiently
        return math.ceil(total_sum / 2)