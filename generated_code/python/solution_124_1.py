import sys
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize the global maximum path sum to a very small integer
        self.max_sum = -sys.maxsize
        
        def get_max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively get the maximum path sum from left and right subtrees.
            # If a subtree path sum is negative, we ignore it by taking max(..., 0).
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Price of the new path would be the parent node value plus the contributions from both subtrees
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum if the current path is better
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # For the parent node call, we can only choose one child's path to maintain a valid tree path
            return node.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        return self.max_sum