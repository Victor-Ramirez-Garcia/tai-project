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
        Finds the length of the longest path where each node has the same value.
        Time Complexity: O(N) where N is the number of nodes in the tree.
        Space Complexity: O(H) where H is the height of the tree, due to recursion stack.
        """
        self.max_len = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively find the longest univalue path starting from left and right children
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            left_extend = 0
            right_extend = 0
            
            # If left child exists and has the same value, extend the path
            if node.left and node.left.val == node.val:
                left_extend = left_len + 1
                
            # If right child exists and has the same value, extend the path
            if node.right and node.right.val == node.val:
                right_extend = right_len + 1
            
            # Update the global maximum length with the path through the current node
            self.max_len = max(self.max_len, left_extend + right_extend)
            
            # Return the longest single-leg path extending from the current node to its parent
            return max(left_extend, right_extend)
        
        dfs(root)
        return self.max_len