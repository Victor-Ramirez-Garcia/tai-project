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
        - For each node, its value must be strictly greater than a `low` bound 
          and strictly less than a `high` bound.
        - When moving left, the upper bound updates to the current node's value.
        - When moving right, the lower bound updates to the current node's value.
        
        Complexity:
        - Time Complexity: O(N) where N is the number of nodes, as we visit each node exactly once.
        - Space Complexity: O(H) where H is the height of the tree, representing the recursion stack. 
                            In the worst case (skewed tree), H = O(N). In the best case, H = O(log N).
        """
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # An empty tree/node is a valid BST
            if not node:
                return True
            
            # The current node's value must stay strictly within the allowed range
            if not (low < node.val < high):
                return False
            
            # Recursively validate the left and right subtrees with updated bounds
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # Initialize the boundary limits with negative and positive infinity to handle potential integer boundaries
        return validate(root, float('-inf'), float('inf'))