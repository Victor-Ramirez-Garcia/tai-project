from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # Sort the array in ascending order to easily access the minimum elements.
        # Time Complexity: O(n log n) where n is the length of nums.
        # Space Complexity: O(1) if sorting in-place, or O(n) depending on Python's Timsort implementation.
        nums.sort()
        
        # In each round, Alice takes the smallest available (nums[i]), and Bob takes the next smallest (nums[i+1]).
        # Bob appends his element first, followed by Alice. This effectively swaps every adjacent pair.
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            
        return nums