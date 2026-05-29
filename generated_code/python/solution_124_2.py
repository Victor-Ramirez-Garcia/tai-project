import sys
from typing import Optional

# Definition for a binary tree node if not already defined by the runner.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Algorithm: Post-order Depth First Search (DFS)
        
        For each node, we calculate the maximum contribution it can make to a parent path.
        A node's max contribution to its parent is: node.val + max(0, max_left_gain, max_right_gain).
        We ignore negative gains because a path can choose not to extend into that subtree.
        
        Simultaneously, we update the global maximum path sum (`self.max_sum`) at each node, 
        treating the current node as the highest point (the "root") of the path. 
        The path sum at this vertex would be: node.val + max_left_gain + max_right_gain.
        
        Time Complexity: O(N) where N is the number of nodes, as we visit each node once.
        Space Complexity: O(H) where H is the height of the tree, due to the recursion stack.
        """
        # Initialize global maximum with negative infinity
        self.max_sum = -sys.maxsize
        
        def get_max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively get the max gain from left and right subtrees.
            # If the gain is negative, we drop it (clamp to 0).
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Price of the new path containing the current node as the highest turn
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum if the current path sum is better
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # For the parent call, a path can only choose ONE branch (left or right)
            return node.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        return self.max_sum