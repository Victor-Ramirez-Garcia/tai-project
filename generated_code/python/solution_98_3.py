from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is a valid Binary Search Tree (BST).
        
        Algorithm: Recursive Depth-First Search (DFS) with a valid range.
        - For each node, its value must be strictly greater than a minimum bound (`low`)
          and strictly less than a maximum bound (`high`).
        - When moving left, the upper bound updates to the current node's value.
        - When moving right, the lower bound updates to the current node's value.
        
        Complexity:
        - Time Complexity: O(N) since we visit every node exactly once.
        - Space Complexity: O(N) in the worst case (skewed tree) due to the recursion stack,
                            or O(log N) for a balanced tree.
        """
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # An empty tree/node is valid
            if not node:
                return True
            
            # The current node's value must strictly stay within the low and high boundaries
            if not (low < node.val < high):
                return False
            
            # Recursively validate the left and right subtrees with updated bounds
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # Initialize the boundaries with negative and positive infinity to handle all integer limits
        return validate(root, float('-inf'), float('inf'))