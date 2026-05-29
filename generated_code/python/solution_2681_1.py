from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # The problem asks us to partition the array into k contiguous subarrays (bags).
        # When we split the array at some index i (so one bag ends at i and the next starts at i+1),
        # the weights weights[i] and weights[i+1] will both contribute to the total score.
        # This is because weights[i] will be the last element of one bag, and weights[i+1] 
        # will be the first element of the next bag.
        #
        # Notice that the first element of the first bag (weights[0]) and the last element 
        # of the last bag (weights[-1]) are always included in the total score, regardless of 
        # how we partition the array.
        #
        # To partition the array into k bags, we need to choose exactly k - 1 split points.
        # Each split between index i and i + 1 adds weights[i] + weights[i+1] to the score.
        # Thus, maximizing/minimizing the score is equivalent to maximizing/minimizing the sum
        # of the k - 1 chosen adjacent pairs.
        
        n = len(weights)
        
        # If the number of bags equals the number of elements or we need 1 bag,
        # there's only one way to partition, so the max and min scores are identical.
        if k == 1 or k == n:
            return 0
            
        # Generate the costs of all possible splits.
        # pair_weights[i] represents the cost added if we split between i and i + 1.
        pair_weights = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        # Sort the pairs to easily pick the smallest and largest costs.
        pair_weights.sort()
        
        # To minimize the score, we choose the k - 1 smallest pair weights.
        # To maximize the score, we choose the k - 1 largest pair weights.
        # Since weights[0] and weights[-1] cancel out in the subtraction (max_score - min_score),
        # the answer is simply the difference between the sum of the top k-1 pairs and the bottom k-1 pairs.
        min_split_cost = sum(pair_weights[:k - 1])
        max_split_cost = sum(pair_weights[len(pair_weights) - (k - 1):])
        
        return max_split_cost - min_split_cost