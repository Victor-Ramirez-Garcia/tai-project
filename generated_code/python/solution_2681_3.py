from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # The problem asks for the difference between the maximum and minimum score
        # when partitioning the array into k contiguous subarrays (bags).
        # Notice that for any valid partition, the first element (weights[0]) and the
        # last element (weights[-1]) will always contribute to the total score, regardless
        # of how we partition the remaining elements.
        #
        # Each split between two bags at index i and i+1 adds weights[i] + weights[i+1]
        # to the score because it forms the end of one bag and the start of the next.
        # To make k bags, we need to make exactly k - 1 splits.
        #
        # Therefore, the score maximization/minimization depends entirely on choosing
        # the largest or smallest k - 1 adjacent pairs (weights[i] + weights[i+1]).
        
        n = len(weights)
        if k == 1 or k == n:
            return 0
        
        # Calculate the costs of all possible splits
        pair_weights = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        # Sort the pairs to easily pick the smallest and largest splits
        pair_weights.sort()
        
        # The number of splits needed is k - 1
        num_splits = k - 1
        
        # The maximum score uses the largest k - 1 pairs.
        # The minimum score uses the smallest k - 1 pairs.
        # When finding the difference, the constant terms (weights[0] + weights[-1]) cancel out.
        min_score_splits = sum(pair_weights[:num_splits])
        max_score_splits = sum(pair_weights[len(pair_weights) - num_splits:])
        
        return max_score_splits - min_score_splits