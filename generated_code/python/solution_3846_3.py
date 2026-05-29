from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # We can only perform operations where nums[i] = nums[i] - 1.
        # This means we can only decrease elements, reducing the overall sum.
        # To make the sum divisible by k with the minimum operations (decrements),
        # we need to reduce the current sum down to the largest multiple of k 
        # that is less than or equal to the current sum.
        #
        # Let S = sum(nums). We want to find a new sum S' such that S' <= S and S' % k == 0.
        # The number of operations will be S - S'.
        # Since S' is the largest multiple of k <= S, S' = S - (S % k).
        # Thus, the number of operations is exactly S % k.
        
        current_sum = sum(nums)
        return current_sum % k