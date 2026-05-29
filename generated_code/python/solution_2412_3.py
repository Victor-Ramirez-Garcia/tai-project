from typing import List

class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Sort the array so that amount[2] is the largest element
        amount.sort()
        
        # If the sum of the two smaller amounts is less than or equal to the largest amount,
        # we can always pair each of the smaller elements with the largest element.
        # The remaining elements of the largest amount will then be filled one by one.
        # Thus, the total seconds will be determined strictly by the largest amount.
        if amount[0] + amount[1] <= amount[2]:
            return amount[2]
        
        # If the sum of the two smaller amounts is greater than the largest amount,
        # we can pair elements from amount[0] and amount[1] together until their sum
        # matches amount[2], allowing all cups to be filled perfectly in pairs with minimal waste.
        # The total seconds will be half of the total sum of all cups, rounded up.
        else:
            total_sum = sum(amount)
            return (total_sum + 1) // 2