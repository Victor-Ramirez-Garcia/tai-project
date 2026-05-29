from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # To make the sum of the array divisible by k using only decrement operations,
        # we need to find the current remainder of the sum when divided by k.
        # Since we can only subtract 1 from any element, each operation decreases the total sum by 1.
        # Therefore, the minimum number of operations required is exactly the total sum modulo k.
        
        total_sum = sum(nums)
        return total_sum % k