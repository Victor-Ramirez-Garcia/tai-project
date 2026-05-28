from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # Track the number of violations where nums[i-1] >= nums[i]
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                count += 1
                # If we encounter more than one violation, it's impossible 
                # to make it strictly increasing by removing just one element.
                if count > 1:
                    return False
                
                # We have a violation at index i. We need to decide whether to 
                # "remove" nums[i-1] or nums[i].
                # To simulate removing nums[i-1], we check if nums[i-2] < nums[i].
                # If it's not (meaning nums[i-2] >= nums[i]), then we must 
                # remove nums[i] instead. We do this by logically modifying 
                # nums[i] to match nums[i-1], ensuring the next iteration 
                # correctly checks against the old valid peak.
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
                    
        return True