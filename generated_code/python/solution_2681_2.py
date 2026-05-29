from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        # Time Complexity: O(N log N) where N is the length of weights (due to sorting)
        # Space Complexity: O(N) to store the pair sums
        #
        # ALGORITHM EXPLANATION:
        # Dividing the array into k bags requires making k - 1 splits.
        # If we split between index i and i + 1, the right boundary of the current bag 
        # is weights[i] and the left boundary of the next bag is weights[i + 1].
        # Thus, each split contributes weights[i] + weights[i + 1] to the total score.
        # The first element weights[0] and the last element weights[-1] are always 
        # part of the score regardless of how we partition the array.
        # 
        # To find the maximum score, we pick the k - 1 largest adjacent pair sums.
        # To find the minimum score, we pick the k - 1 smallest adjacent pair sums.
        # The difference between the max and min scores is simply the difference 
        # between the sum of the top k - 1 pairs and the sum of the bottom k - 1 pairs.
        
        n = len(weights)
        if k == 1 or n == k:
            return 0
            
        # Calculate all possible adjacent pair sums
        pair_sums = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        # Sort the pair sums to easily pick the smallest and largest ones
        pair_sums.sort()
        
        # Elements to pick
        m = k - 1
        
        # Sum of the m largest pairs minus the sum of the m smallest pairs
        # This bypasses needing to track weights[0] and weights[-1] since they cancel out
        max_score_contribution = sum(pair_sums[-m:]) if m > 0 else 0
        min_score_contribution = sum(pair_sums[:m]) if m > 0 else 0
        
        return max_score_contribution - min_score_contribution