from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Algorithm: Post-order Traversal (DFS)
        
        For each node, we calculate the maximum path sum that can extend upwards 
        to its parent. This is determined by the node's value plus the maximum 
        of its left or right subtree contributions (only if they are positive).
        
        Simultaneously, we track the global maximum path sum where the current 
        node acts as the highest point (the "root") of the path, combining 
        both left and right subtree contributions.
        
        Time Complexity: O(N) - Each node is visited exactly once.
        Space Complexity: O(H) - Max recursion stack depth proportional to tree height.
        """
        # Initialize global maximum with negative infinity
        self.max_sum = float('-inf')
        
        def get_max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively get the max path sum from left and right subtrees.
            # If a subtree contribution is negative, we drop it (take 0).
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Price of a new path with the current node as the highest point (turnaround point)
            current_path_sum = node.val + left_gain + right_gain
            
            # Update the global maximum path sum found so far
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return the max gain the parent node can get by extending through this node
            return node.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        return self.max_sum