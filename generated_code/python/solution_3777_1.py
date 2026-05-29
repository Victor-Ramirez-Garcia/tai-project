from typing import List, Dict, Tuple

class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        """
        Algorithm: Dynamic Programming with State Compression
        
        Since we need to compute an alternating sum, each element we choose can either 
        be added (if it's at an even position in the chosen subsequence) or subtracted 
        (if it's at an odd position in the chosen subsequence).
        
        We can define a state dp[(current_alternating_sum, expected_sign)] = max_product
        where expected_sign is 1 if the next element taken will be at an even index (+), 
        and -1 if it will be at an odd index (-).
        
        Since we want to maximize the product without exceeding 'limit', and all nums[i] >= 1
        (implied by standard product maximization limits, or handles any positive integers), 
        we transition by either skipping