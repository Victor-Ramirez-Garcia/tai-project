from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(N) to find the min and max elements
        # Space Complexity: O(1) as we only keep track of the min and max values
        # 
        # Explanation: 
        # The problem requires choosing exactly k distinct non-empty subarrays to maximize the sum of their values.
        # The value of a subarray is max(nums[l..r]) - min(nums[l..r]).
        # The maximum possible value for *any* subarray in the entire array is simply (global_max - global_min).
        # We can always construct at least k distinct subarrays that span both the global maximum and the global minimum.
        # For instance, if the global minimum occurs at index i and the global maximum at index j (assuming i < j without loss of generality),
        # any subarray starting at l <= i and ending at r >= j will have the same maximum value of (global_max - global_min).
        # Since the total number of such valid subarrays is (i + 1) * (n - j), and the constraints guarantee that we can 
        # pick k distinct subarrays (k <= total available or just simple duplication of values across distinct intervals), 
        # each chosen subarray can achieve this optimal upper bound.
        # Therefore, the maximum possible total value is k * (global_max - global_min).
        
        if not nums or k == 0:
            return 0
            
        global_max = max(nums)
        global_min = min(nums)
        
        return k * (global_max - global_min)