from typing import List

class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Algorithm: Lowest Common Ancestor (LCA) in a Binary Tree
        
        A complete binary tree has the property that the parent of a node with value `x` 
        is `x // 2`. To find the length of the cycle formed by adding an edge between 
        `a` and `b`, we can compute the distance between `a` and `b` in the original tree, 
        and then add 1 (for the newly added edge).
        
        The distance between `a` and `b` in the tree is equal to the number of steps 
        taken to climb from `a` and `b` to their Lowest Common Ancestor (LCA). 
        Since we divide by 2 to move up, we can repeatedly move the larger node up 
        until both nodes meet.
        
        Time Complexity: O(M * N) where M is the number of queries and N is the tree depth (n <= 30).
                         Since n is small, each query takes O(N) operations.
        Space Complexity: O(1) auxiliary space (excluding the output array).
        """
        ans = []
        
        for a, b in queries:
            cycle_len = 1  # Start with 1 to account for the newly added edge between a and b
            
            # Climb up the tree until a and b meet at their LCA
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                cycle_len += 1
                
            ans.append(cycle_len)
            
        return ans