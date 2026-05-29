from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # Total operations available across both arrays. 
        # Modifying nums1[i] or nums2[i] has the same impact on reducing the absolute difference.
        k = k1 + k2
        
        # Calculate the absolute differences between nums1 and nums2.
        # Track the maximum possible difference to set up our frequency array buckets.
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        max_diff = max(diffs)
        
        if max_diff == 0:
            return 0
            
        # Frequency array where counts[v] stores the number of elements with absolute difference v.
        counts = [0] * (max_diff + 1)
        for d in diffs:
            counts[d] += 1
            
        # Greedy reduction: Start from the largest difference and reduce elements down.
        for v in range(max_diff, 0, -1):
            if counts[v] == 0:
                continue
                
            # Number of operations needed to reduce all current differences of value 'v' by 1.
            needed = counts[v]
            
            if k >= needed:
                # We have enough operations to shift all elements from value 'v' to 'v - 1'.
                k -= needed
                counts[v - 1] += counts[v]
                counts[v] = 0
            else:
                # We can only shift 'k' elements from value 'v' to 'v - 1'.
                counts[v - 1] += k
                counts[v] -= k
                k = 0
                break # All operations exhausted.
                
        # Calculate the final minimum sum of squared differences.
        ans = 0
        for v in range(1, max_diff + 1):
            if counts[v] > 0:
                ans += counts[v] * (v * v)
                
        return ans