from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Time Complexity: O(N) where N is the length of nums, as we iterate through the array once.
        Space Complexity: O(1) auxiliary space, as we only use a single variable to track the total operations.
        
        Algorithm Explanation:
        The operation allows us to decrement any element by 1. To make the total sum divisible by k,
        the most optimal way using only decrements is to reduce the overall sum to the nearest 
        multiple of k that is less than or equal to the current sum. 
        
        Equivalently, for each element `nums[i]`, the number of decrements needed to remove its 
        contribution to the remainder of the total sum modulo k is simply `nums[i] % k`. 
        Summing `nums[i] % k` for all elements gives the minimum operations required.
        """
        ans = 0
        for num in nums:
            ans += num % k
        return ans