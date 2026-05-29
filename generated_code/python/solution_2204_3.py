from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair each element with its original index to preserve order later
        # Time: O(N) where N is the length of nums
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort by value in descending order and pick the top k largest elements
        # Time: O(N log N)
        top_k = sorted(indexed_nums, key=lambda x: x[0], reverse=True)[:k]
        
        # Sort the chosen top k elements by their original index to restore subsequence order
        # Time: O(k log k)
        top_k.sort(key=lambda x: x[1])
        
        # Extract and return the values
        # Time: O(k)
        return [num for num, i in top_k]