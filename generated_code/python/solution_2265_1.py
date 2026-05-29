from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Result array initialized with zeros of the same size
        n = len(nums)
        ans = [0] * n
        
        # We can solve this optimally in a single pass using two pointers.
        # 'left' tracks where the next element smaller than 'pivot' should go.
        # 'right' tracks where the next element greater than 'pivot' should go (from the end).
        left = 0
        right = n - 1
        
        # In a single pass, we can place elements smaller than pivot from the left,
        # and elements greater than pivot from the right.
        # To maintain stable relative ordering for elements greater than pivot, 
        # we iterate forward for 'left' elements and backward for 'right' elements.
        for i in range(n):
            if nums[i] < pivot:
                ans[left] = nums[i]
                left += 1
            if nums[n - 1 - i] > pivot:
                ans[right] = nums[n - 1 - i]
                right -= 1
                
        # Fill the remaining middle section with elements equal to pivot
        while left <= right:
            ans[left] = pivot
            left += 1
            
        return ans