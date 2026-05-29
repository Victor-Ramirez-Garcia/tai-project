from typing import List

class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # Track the number of violations where nums[i-1] >= nums[i]
        count = 0
        
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                count += 1
                # If more than one violation is found, it's impossible by removing just one element
                if count > 1:
                    return False
                
                # We have a violation at index i. We need to decide whether to "remove" nums[i-1] or nums[i].
                # To make the array strictly increasing, the remaining elements must satisfy the condition.
                # If we remove nums[i-1], then nums[i-2] must be less than nums[i].
                # If this condition fails, our only alternative is to remove nums[i] instead.
                # Removing nums[i] means its value effectively becomes the previous valid element (nums[i-1]) 
                # so that the next iteration compares correctly.
                if i > 1 and nums[i - 2] >= nums[i]:
                    nums[i] = nums[i - 1]
                    
        return True