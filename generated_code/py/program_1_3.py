class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map to store the value and its corresponding index: {value: index}
        # This allows us to achieve an optimal O(n) time complexity by trading O(n) space.
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in our map, we found the pair
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, store the current number and its index for future lookups
            seen[num] = index
            
        # The problem guarantees exactly one solution, so we should never reach here.
        return []