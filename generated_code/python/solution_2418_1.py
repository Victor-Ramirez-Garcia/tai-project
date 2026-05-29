from typing import List

class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        # Total operations we can perform to decrease the absolute differences.
        # Modifying nums1[i] by +1/-1 or nums2[i] by -1/+1 has the same effect 
        # on minimizing |nums1[i] - nums2[i]|.
        k = k1 + k2
        
        # Calculate the absolute differences for each pair
        diffs = [abs(n1 - n2) for n1, n2 in zip(nums1, nums2)]
        
        # Find the maximum possible difference to set the upper bound for the bucket size
        max_diff = max(diffs)
        if max_diff == 0 or k == 0:
            return sum(d * d for d in diffs)
            
        # Use a bucket/frequency array to count occurrences of each difference.
        # This allows O(max_diff) or O(N) processing instead of sorting/heap manipulation.
        counts = [0] * (max_diff + 1)
        for d in diffs:
            counts[d] += 1
            
        # Process differences from largest to smallest greedily
        for d in range(max_diff, 0, -1):
            if counts[d] == 0:
                continue
                
            # If total allowed operations k can reduce all elements of value `d` to `d - 1`
            if k >= counts[d]:
                k -= counts[d]
                counts[d - 1] += counts[d]
                counts[d] = 0
            else:
                # If k cannot reduce all elements, reduce as many as possible
                counts[d - 1] += k
                counts[d] -= k
                k = 0
                break # No more operations left
                
        # Calculate the final minimum sum of squared differences
        ans = 0
        for d in range(1, max_diff + 1):
            if counts[d] > 0:
                ans += counts[d] * (d * d)
                
        return ans