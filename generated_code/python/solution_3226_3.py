from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # Sort the array in ascending order to easily access the minimum elements.
        # Time Complexity: O(n log n) where n is the length of nums.
        # Space Complexity: O(1) if sorting in place, or O(n) depending on python's Timsort implementation.
        nums.sort()
        
        # In every round, Alice picks the smallest remaining element (nums[i]) 
        # and Bob picks the second smallest remaining element (nums[i+1]).
        # Bob appends his element first, followed by Alice. 
        # This is equivalent to swapping every adjacent pair of elements in the sorted array.
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            
        return nums