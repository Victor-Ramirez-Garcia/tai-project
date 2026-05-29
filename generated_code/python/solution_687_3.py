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
        Algorithm: Post-order traversal / Bottom-up Depth-First Search (DFS).
        
        For each node, we recursively calculate the longest univalue path extending 
        into its left and right subtrees.
        
        Time Complexity: O(N) where N is the number of nodes in the tree. We visit each node once.
        Space Complexity: O(H) where H is the height of the tree, representing the recursion stack.
        """
        self.max_path = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively find the longest univalue path from left and right children
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            # Variables to store the matching univalue path length from the current node
            left_arrow = right_arrow = 0
            
            # If the left child exists and has the same value, extend the path
            if node.left and node.left.val == node.val:
                left_arrow = left_len + 1
                
            # If the right child exists and has the same value, extend the path
            if node.right and node.right.val == node.val:
                right_arrow = right_len + 1
            
            # Update the global maximum path which can combine both left and right directions
            self.max_path = max(self.max_path, left_arrow + right_arrow)
            
            # Return the longest single-leg path extending upwards to the parent
            return max(left_arrow, right_arrow)

        dfs(root)
        return self.max_path