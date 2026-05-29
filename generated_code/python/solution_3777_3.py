from typing import List, Dict, Tuple

class Solution:
    def maxProduct(self, nums: List[int], k: int, limit: int) -> int:
        """
        Algorithm: Dynamic Programming with State Compression
        We want to find a subsequence with a specific alternating sum 'k' 
        that maximizes the product of its elements, such that the product <= limit.
        
        An alternating sum means:
        - Even-indexed elements of the subsequence are added (+).
        - Odd-indexed elements of the subsequence are subtracted (-).
        
        We can use DP where the state tracks:
        - The current alternating sign expected for the NEXT element to be added.
          Since we need a non-empty subsequence, it must start with an even index (index 0 of subsequence), 
          which means the first element is always added (+).
          State 0: Expecting an element to be ADDED (+), meaning the NEXT index in the subsequence will be even.
                   However, since the very first element must be added, we can think of it as:
                   State 0: Subsequence is currently empty, or last placed element was at an odd index. Next is (+).
                   State 1: Last placed element was at an even index. Next is (-).
        
        To maximize the product while strictly obeying `product <= limit`, and because 
        elements can be negative (which complicates standard maximization), we can map 
        (alternating_sum, state) -> set of possible products.
        Given the constraints of typical subsequence problems and limit bounds, we can 
        maintain a dictionary `dp` where key is (current_alternating_sum, state) and value 
        is a set of possible products achieved so far.
        
        Since we want to maximize the product <= limit, and all valid products must be positive 
        or negative integers, keeping a set of reachable products for each (sum, state) allows 
        us to transition cleanly.
        """
        # dp stores: (current_alternating_sum, next_sign_state) -> set of unique products
        # next_sign_state: 0 means we are looking to ADD the next element.
        #                  1 means we are looking to SUBTRACT the next element.
        dp: Dict[Tuple[int, int], set] = {}
        
        for num in nums:
            next_dp = {}
            # Copy over existing states
            for state, products in dp.items():
                if state not in next_dp:
                    next_dp[state] = set(products)
                else:
                    next_dp[state].update(products)
            
            # Case 1: Start a brand new subsequence with 'num' (must be added, so next state becomes 1)
            # The current alternating sum becomes 0 + num = num.
            if (num, 1) not in next_dp:
                next_dp[(num, 1)] = set()
            next_dp[(num, 1)].add(num)
            
            # Case 2: Extend existing subsequences
            for (curr_sum, state), products in dp.items():
                if state == 0:
                    # Current state expects ADDITION (+)
                    next_sum = curr_sum + num
                    next_state = 1
                    for p in products:
                        next_p = p * num
                        # We only track products if they don't exceed the limit or if they are negative
                        # (since negative products can potentially become valid positive ones later)
                        # However, to be safe and precise, we store all valid intermediate products.
                        if (next_sum, next_state) not in next_dp:
                            next_dp[(next_sum, next_state)] = set()
                        next_dp[(next_sum, next_state)].add(next_p)
                else:
                    # Current state expects SUBTRACTION (-)
                    next_sum = curr_sum - num
                    next_state = 0
                    for p in products:
                        next_p = p * num
                        if (next_sum, next_state) not in next_dp:
                            next_dp[(next_sum, next_state)] = set()
                        next_dp[(next_sum, next_state)].add(next_p)
            
            dp = next_dp
            
        max_prod = -1
        # A valid non-empty subsequence can end at any step. 
        # Its final state can be 0 (if it has an even number of elements) or 1 (if odd number of elements).
        for state in [0, 1]:
            if (k, state) in dp:
                for p in dp[(k, state)]:
                    if p <= limit and p > max_prod:
                        max_prod = p
                        
        return max_prod