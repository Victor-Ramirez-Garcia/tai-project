from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        # To simulate Alice and Bob repeatedly picking the smallest elements,
        # we can simply sort the array in ascending order.
        nums.sort()
        
        # In every round, Alice picks the smallest remaining (at index i) 
        # and Bob picks the next smallest (at index i + 1).
        # They append to 'arr' in reverse order: Bob first, then Alice.
        # This means we just need to swap adjacent elements at even indices.
        for i in range(0, len(nums), 2):
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            
        return nums