from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        """
        Algorithm Explanation:
        1. The absolute differences between nums1[i] and nums2[i] are what matter. 
           Modifying an element in nums1 or nums2 is equivalent to reducing the absolute 
           difference |nums1[i] - nums2[i]| by 1. 
        2. We have a total budget of k = k1 + k2 operations to reduce these absolute differences.
        3. To minimize the sum of squares, we should greedily reduce the largest differences first 
           because squaring penalizes larger numbers much more harshly.
        4. Since the maximum possible difference is 10^5, we can use a bucket sort / frequency array 
           approach instead of a max-heap to achieve an O(N + MAX_DIFF) time complexity.
        """
        # Calculate the total number of operations we can perform
        k = k1 + k2
        
        # Max possible difference is bounded by the constraints (0 <= nums1[i], nums2[i] <= 10^5)
        max_diff = 100000
        # frequency[d] will store the number of pairs with an absolute difference of d
        frequency = [0] * (max_diff + 1)
        
        total_diff_sum = 0
        for n1, n2 in zip(nums1, nums2):
            diff = abs(n1 - n2)
            frequency[diff] += 1
            total_diff_sum += diff
            
        # If the total allowable operations can reduce all differences to 0, return 0
        if total_diff_sum <= k:
            return 0
            
        # Process differences from largest to smallest
        for d in range(max_diff, 0, -1):
            if frequency[d] == 0:
                continue
                
            # Count how many items have the current maximum difference `d`
            count = frequency[d]
            
            # If our operations `k` can completely reduce all elements of size `d` to `d - 1`
            if k >= count:
                k -= count
                frequency[d - 1] += count
                frequency[d] = 0
            else:
                # Otherwise, we can only reduce `k` of these elements to `d - 1`
                frequency[d - 1] += k
                frequency[d] -= k
                k = 0
                break # No more operations left
                
        # Calculate the final minimum sum of squared differences
        ans = 0
        for d in range(1, max_diff + 1):
            if frequency[d] > 0:
                ans += frequency[d] * (d * d)
                
        return ans