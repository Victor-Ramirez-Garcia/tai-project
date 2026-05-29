from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # Track the number of drops (inversions where nums[i-1] >= nums[i])
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                count += 1
                # If we need to remove more than one element, it's impossible
                if count > 1:
                    return False
                
                # We have two choices to fix the strictly increasing property:
                # 1. Remove nums[i] -> requires nums[i-1] < nums[i+1]
                # 2. Remove nums[i-1] -> requires nums[i-2] < nums[i]
                #
                # If removing nums[i-1] is required because nums[i-2] >= nums[i],
                # we conceptually modify nums[i] to be nums[i-1] so the next 
                # iteration correctly compares with the "surviving" element.
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
                    
        return True