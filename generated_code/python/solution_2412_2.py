from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        """
        Algorithm Explanation:
        This is a greedy problem that can be solved in O(1) time and O(1) space.
        
        Let the amounts of the three types of water be sorted such that x <= y <= z.
        There are two main scenarios:
        1. If the largest amount (z) is greater than or equal to the sum of the other two (x + y):
           Every time we fill a cup from z, we can pair it with one from x or y until x and y are empty.
           After x and y are depleted, we are forced to fill the remaining cups of z one by one.
           Therefore, the bottleneck is entirely z, and the minimum seconds needed is exactly z.
           
        2. If the largest amount (z) is less than the sum of the other two (x + y):
           We can always pair cups up optimally such that we rarely or never have to fill a single cup 
           until the very last step (if the total sum is odd). 
           In this case, the minimum seconds needed is ceil((x + y + z) / 2), which is equivalent to 
           (sum(amount) + 1) // 2.
        """
        # Sort the amounts to easily identify the maximum element
        amount.sort()
        
        # Scenario 1: The largest element is a bottleneck
        if amount[2] >= amount[0] + amount[1]:
            return amount[2]
        
        # Scenario 2: Elements are balanced enough to be paired optimally
        return (sum(amount) + 1) // 2