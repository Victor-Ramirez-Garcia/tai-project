class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map to store the value and its corresponding index
        # Time Complexity: O(n) - Single pass through the list
        # Space Complexity: O(n) - In the worst case, storing all elements in the hash map
        seen = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in the map, we found our pair
            if complement in seen:
                return [seen[complement], index]
            
            # Otherwise, store the current number and its index
            seen[num] = index
            
        return []  # Guaranteed to have exactly one solution, so this line is theoretically unreachable