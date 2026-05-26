class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map to store the value and its corresponding index
        # Time Complexity: O(N) since we traverse the list containing N elements only once.
        # Space Complexity: O(N) to store the elements in the hash map.
        seen = {}
        
        for i, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in the map, we found our pair
            if complement in seen:
                return [seen[complement], i]
            
            # Otherwise, store the current number with its index
            seen[num] = i
            
        return []