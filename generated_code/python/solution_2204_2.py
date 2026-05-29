from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Pair each element with its original index to preserve order later
        # Time: O(N) to create the indexed array
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        
        # Sort by value in descending order and pick the top k elements
        # Time: O(N log N) for sorting, or O(N log k) if using a heap/quickselect. 
        # Given N <= 1000, standard sort is extremely fast and well within limits.
        indexed_nums.sort(key=lambda x: x[0], reverse=True)
        top_k = indexed_nums[:k]
        
        # Sort the chosen k elements by their original indices to maintain subsequence order
        # Time: O(k log k)
        top_k.sort(key=lambda x: x[1])
        
        # Extract the values from the sorted pairs
        # Time: O(k)
        return [num for num, i in top_k]