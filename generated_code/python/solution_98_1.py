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
        
        Algorithm: Recursive Depth-First Search (DFS) with range constraints.
        Time Complexity: O(N) where N is the number of nodes, as we visit each node once.
        Space Complexity: O(H) where H is the height of the tree, representing the maximum 
                          depth of the recursion call stack (O(N) worst case, O(log N) best case).
        """
        def validate(node: Optional[TreeNode], low: float, high: float) -> bool:
            # An empty tree/node is valid
            if not node:
                return True
            
            # The current node's value must sit strictly between the low and high boundaries
            if not (low < node.val < high):
                return False
            
            # Recursively validate subtrees:
            # - Left subtree values must be strictly less than the current node's value (updates high boundary)
            # - Right subtree values must be strictly greater than the current node's value (updates low boundary)
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        
        # Initialize boundaries with -infinity and +infinity to handle standard integer limits
        return validate(root, float('-inf'), float('inf'))