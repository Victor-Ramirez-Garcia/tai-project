from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # To make the sum of the array divisible by k, we can find the remainder 
        # of each element when divided by k. The number of decrements needed 
        # for an element to reach the nearest lower multiple of k is exactly 
        # equal to its remainder (nums[i] % k). Summing these remainders gives 
        # the minimum total operations required.
        return sum(num % k for num in nums)