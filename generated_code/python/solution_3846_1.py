from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        Algorithm Choice: Greedy / Modular Arithmetic
        
        To make the total sum divisible by k, we can track the current remainder 
        of the sum modulo k. 
        
        Since we can only *decrease* elements (nums[i] = nums[i] - 1), each operation 
        reduces the overall sum by 1. Therefore, to reduce the sum to the nearest 
        smaller multiple of k, the minimum number of operations required is exactly 
        equal to (total_sum % k).
        
        Time Complexity: O(N) where N is the length of nums, to calculate the sum.
        Space Complexity: O(1) auxiliary space.
        """
        # Calculate the total sum of the array
        total_sum = sum(nums)
        
        # The number of operations needed is the remainder when total_sum is divided by k
        return total_sum % k