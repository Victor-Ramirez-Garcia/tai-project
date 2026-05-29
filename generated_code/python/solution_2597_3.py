from typing import List

class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        """
        Algorithm: Lowest Common Ancestor (LCA) in a Complete Binary Tree.
        
        The graph is initially a complete binary tree where the parent of node `x` 
        is `x // 2`. Adding an edge between `a` and `b` creates a single cycle.
        The cycle consists of the added edge plus the unique tree path between `a` and `b`.
        
        The length of the path between `a` and `b` in the tree can be found by moving 
        upwards towards their Lowest Common Ancestor (LCA). Since `parent = node // 2`, 
        we can continuously divide the larger node value by 2 until both nodes meet. 
        Each division corresponds to traversing one edge.
        
        Time Complexity: O(m * n) where m is the number of queries and n is the maximum depth.
        Space Complexity: O(1) auxiliary space (excluding the output array).
        """
        ans = []
        
        for a, b in queries:
            cycle_length = 1  # 1 accounts for the newly added edge between a and b
            
            # Move up the tree until a and b meet at their LCA
            while a != b:
                if a > b:
                    a //= 2
                else:
                    b //= 2
                cycle_length += 1
                
            ans.append(cycle_length)
            
        return ans