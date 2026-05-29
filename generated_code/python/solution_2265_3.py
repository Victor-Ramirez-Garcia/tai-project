from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Time Complexity: O(n) - Single pass using a two-pointer approach to fill the result array.
        # Space Complexity: O(n) - Auxiliary space for the output array (as required by the problem).
        
        n = len(nums)
        ans = [0] * n
        
        # Count the occurrences of elements smaller than the pivot and equal to the pivot
        # to determine the starting insertion points for each group.
        less_count = 0
        equal_count = 0
        for num in nums:
            if num < pivot:
                less_count += 1
            elif num == pivot:
                equal_count += 1
                
        # Initialize pointers for placing elements in the correct sections
        # less_ptr starts at 0
        # equal_ptr starts right after the 'less' elements
        # greater_ptr starts right after the 'equal' elements
        less_ptr = 0
        equal_ptr = less_count
        greater_ptr = less_count + equal_count
        
        # Iterate through the original array to maintain stable relative ordering
        for num in nums:
            if num < pivot:
                ans[less_ptr] = num
                less_ptr += 1
            elif num == pivot:
                ans[equal_ptr] = num
                equal_ptr += 1
            else:
                ans[greater_ptr] = num
                greater_ptr += 1
                
        return ans