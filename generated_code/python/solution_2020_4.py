from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # Track the number of violations where nums[i-1] >= nums[i]
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                count += 1
                # If there's more than one violation, we can't fix it by removing just one element
                if count > 1:
                    return False
                
                # To resolve the violation at index 'i', we have two choices for removal:
                # 1. Remove nums[i-1]: This is valid if nums[i-2] < nums[i].
                # 2. Remove nums[i]: This is valid if nums[i-1] < nums[i+1].
                # If we cannot safely remove nums[i-1] because nums[i-2] >= nums[i],
                # we are forced to logically "remove" nums[i]. We simulate this by 
                # carrying the value of nums[i-1] forward into nums[i].
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
                    
        return True