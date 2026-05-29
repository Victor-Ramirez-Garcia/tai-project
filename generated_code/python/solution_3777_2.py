from typing import List, Dict, Tuple

class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        """
        Problem approach:
        We need to find a subsequence of `nums` such that its alternating sum is equal to `k`,
        and the product of its elements is maximized while not exceeding `limit`.
        
        Since we need to maintain the relative order of elements for the "alternating sum" 
        (even index minus odd index within the chosen subsequence), this is a variant of 
        the Knapsack / Dynamic Programming problem.
        
        For each element, we can decide to:
        1. Skip it.
        2. Include it at an EVEN position in the subsequence (adds to the alternating sum, multiplies the product).
        3. Include it at an ODD position in the subsequence (subtracts from the alternating sum, multiplies the product).
        
        State representation:
        We can use a DP state or a set of reachable states: (current_alternating_sum, next_position_parity) -> max_product
        - `next_position_parity` = 0 means the next included element will be at an even index of the subsequence (so it's added).
        - `next_position_parity` = 1 means the next included element will be at an odd index of the subsequence (so it's subtracted).
        
        We start with an empty subsequence, so the next position is index 0 (even), sum is 0, product is 1.
        """
        # dp stores maps for parity 0 and parity 1: {alternating_sum: max_product}
        # Initially, before picking any element, we are looking for an element at an EVEN index (parity 0).
        # The current sum is 0, and the current product is 1.
        dp = {0: 1} # for parity 0
        dp_odd = {} # for parity 1
        
        for num in nums:
            next_dp = dp.copy()
            next_dp_odd = dp_odd.copy()
            
            # Case 1: Use `num` as an EVEN index element in the subsequence.
            # This is possible if we were expecting an even position (state in `dp`).
            for s, p in dp.items():
                new_s = s + num
                new_p = p * num
                if new_p <= limit:
                    # After picking an even element, the next element must be at an ODD index.
                    if new_s not in next_dp_odd or new_p > next_dp_odd[new_s]:
                        next_dp_odd[new_s] = new_p
                        
            # Case 2: Use `num` as an ODD index element in the subsequence.
            # This is possible if we were expecting an odd position (state in `dp_odd`).
            for s, p in dp_odd.items():
                new_s = s - num
                new_p = p * num
                if new_p <= limit:
                    # After picking an odd element, the next element must be at an EVEN index.
                    if new_s not in next_dp or new_p > next_dp[new_s]:
                        next_dp[new_s] = new_p
            
            dp = next_dp
            dp_odd = next_dp_odd
            
        # The subsequence can end at either an even length or an odd length.
        # This means the final required sum `k` could be found in either `dp` (if the next expected was even, 
        # meaning the subsequence had an odd length) or `dp_odd` (if the next expected was odd, meaning 
        # the subsequence had an even length).
        # Note: A non-empty subsequence ending at an even index means next is odd (so state is in dp_odd).
        # A non-empty subsequence ending at an odd index means next is even (so state is in dp).
        # However, we must ensure the subsequence is non-empty. The initial state (0, 1) in `dp` represents 
        # an empty subsequence, so we should filter it out if k == 0 and product == 1 comes from the empty state.
        
        ans = -1
        if k in dp:
            # If it's in dp and k == 0, we must ensure it's not the default empty state product 1
            # unless a valid non-empty subsequence also achieved sum 0 and product 1.
            # To be safe, we can track if a non-empty sequence achieved it, or just check values.
            ans = max(ans, dp[k])
            
        if k in dp_odd:
            ans = max(ans, dp_odd[k])
            
        # To strictly handle the "non-empty" condition cleanly:
        # Let's re-verify if ans == 1 and k == 0 is actually achievable by a non-empty subsequence.
        # We can run a quick check or just use a boolean flag in the DP state to track non-emptiness.
        
        # Let's refine the DP to track (sum) -> product, and separate initial state.
        # dp[0] = {sum: max_prod}, dp[1] = {sum: max_prod}
        # To avoid empty subsequence issues, we can initialize DP with actual single-element starts.
        
        dp_even = {}
        dp_odd = {}
        
        for num in nums:
            next_even = dp_even.copy()
            next_odd = dp_odd.copy()
            
            # Start a new subsequence with `num` at an even index (index 0 of the subsequence)
            if num <= limit:
                if num not in next_odd or num > next_odd[num]:
                    next_odd[num] = num
            
            # Extend existing subsequences where the next element should be EVEN
            for s, p in dp_even.items():
                new_s = s + num
                new_p = p * num
                if new_p <= limit:
                    if new_s not in next_odd or new_p > next_odd[new_s]:
                        next_odd[new_s] = new_p
                        
            # Extend existing subsequences where the next element should be ODD
            for s, p in dp_odd.items():
                new_s = s - num
                new_p = p * num
                if new_p <= limit:
                    if new_s not in next_even or new_p > next_even[new_s]:
                        next_even[new_s] = new_p
                        
            dp_even = next_even
            dp_odd = next_odd
            
        max_res = -1
        if k in dp_even:
            max_res = max(max_res, dp_even[k])
        if k in dp_odd:
            max_res = max(max_res, dp_odd[k])
            
        return max_res