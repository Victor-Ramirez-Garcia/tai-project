from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Time Complexity: O(N) where N is the length of nums, as we do a single pass or linear extractions.
        # Space Complexity: O(N) to store the rearranged elements in the result list.
        # This approach guarantees a stable partition (maintaining relative order) efficiently.
        
        # We can simulate the process by collecting elements smaller, equal to, 
        # and greater than the pivot, then combining them.
        less = [x for x in nums if x < pivot]
        equal = [x for x in nums if x == pivot]
        greater = [x for x in nums if x > pivot]
        
        return less + equal + greater