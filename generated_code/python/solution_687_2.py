from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        """
        Algorithm: Post-order Traversal (DFS)
        
        For each node, we recursively find the longest univalue path extending into 
        its left and right subtrees. 
        - If the child exists and has the same value as the current node, we extend 
          the path length from that child by 1. Otherwise, the path from that direction is 0.
        - The longest univalue path *passing through* the current node as the highest 
          point is the sum of the left and right extended paths.
        - We maintain a global maximum (`max_path`) to track the longest path found.
        - The function returns the maximum single-direction path (left or right) to 
          allow the parent node to extend it.
          
        Time Complexity: O(N) where N is the number of nodes, as we visit each node once.
        Space Complexity: O(H) where H is the height of the tree, due to the recursion stack.
        """
        self.max_path = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively find the longest univalue paths in left and right subtrees
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            # Variables to store the extended path from the current node
            left_arrow = right_arrow = 0
            
            # If left child exists and has the same value, extend the path
            if node.left and node.left.val == node.val:
                left_arrow = left_len + 1
                
            # If right child exists and has the same value, extend the path
            if node.right and node.right.val == node.val:
                right_arrow = right_len + 1
            
            # Update the global maximum with the combined path through the current node
            self.max_path = max(self.max_path, left_arrow + right_arrow)
            
            # Return the longest single-direction path to the parent
            return max(left_arrow, right_arrow)
        
        dfs(root)
        return self.max_path