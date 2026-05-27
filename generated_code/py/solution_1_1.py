class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map to store the value and its corresponding index
        # Time Complexity: O(N) since we traverse the list containing N elements only once.
        # Space Complexity: O(N) to store the elements in the hash map.
        num_to_index = {}
        
        for index, num in enumerate(nums):
            complement = target - num
            
            # If the complement exists in the map, we found our pair
            if complement in num_to_index:
                return [num_to_index[complement], index]
            
            # Otherwise, store the current number and its index in the map
            num_to_index[num] = index
            
        # The problem guarantees exactly one solution, so we don't need a fallback return