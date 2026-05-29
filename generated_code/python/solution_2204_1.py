from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair each element with its original index to preserve order later
        # e.g., nums = [2, 1, 3, 3] -> indexed_nums = [(2, 0), (1, 1), (3, 2), (3, 3)]
        indexed_nums = [(val, idx) for idx, val in enumerate(nums)]
        
        # Sort by value in descending order to identify the k largest elements.
        # Time Complexity for sorting: O(N log N), where N is the length of nums.
        indexed_nums.sort(key=lambda x: x[0], reverse=True)
        
        # Take the top k elements with the largest values
        top_k = indexed_nums[:k]
        
        # Sort these top k elements by their original indices to restore subsequence order
        # Time Complexity for sorting k elements: O(k log k)
        top_k.sort(key=lambda x: x[1])
        
        # Extract the original values to form the final result subsequence
        return [val for val, idx in top_k]