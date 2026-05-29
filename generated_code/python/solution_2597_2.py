from typing import List

class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Algorithm: Lowest Common Ancestor (LCA) in a Binary Tree
        
        Since the tree is a complete binary tree where the children of node `val` 
        are `2 * val` and `2 * val + 1`, the parent of any node `val` is simply `val // 2`.
        
        Adding an edge between `a` and `b` creates a unique cycle consisting of:
        1. The path from `a` to their Lowest Common Ancestor (LCA).
        2. The path from `b` to their LCA.
        3. The newly added edge between `a` and `b`.
        
        The length of the cycle is: (depth(a) - depth(LCA)) + (depth(b) - depth(LCA)) + 1.
        We can find this efficiently by moving the larger node value up to its parent 
        until both node pointers meet at the LCA, counting the steps along the way.
        
        Time Complexity: O(m * n) where m is the number of queries and n is the maximum depth.
                         Since n <= 30, each query takes O(log(val)) <= 30 steps, which is O(1).
                         Total Time Complexity: O(m).
        Space Complexity: O(1) auxiliary space (excluding the output array).
        """
        ans = []
        
        for a, b in queries:
            cycle_len = 1  # Start with 1 for the newly added edge between a and b
            
            # Move up the tree until the two nodes meet at their LCA
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                cycle_len += 1
            
            ans.append(cycle_len)
            
        return ans