from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Calculates the sum of values of all nodes in a BST within the inclusive range [low, high].
        
        Algorithm: Optimized DFS (Pruning)
        - Since it's a BST, we can skip searching entire subtrees that fall completely out of bounds.
        - If root.val < low, all nodes in the left subtree are also < low, so we only search the right subtree.
        - If root.val > high, all nodes in the right subtree are also > high, so we only search the left subtree.
        - Otherwise, root.val is in range, so we add its value and search both subtrees.
        
        Time Complexity: O(N) in the worst case (where N is the number of nodes), but 
                         substantially faster on average due to pruning.
        Space Complexity: O(H) where H is the height of the tree, representing the recursion stack.
        """
        if not root:
            return 0
        
        # Case 1: Current node value is too small, prune the left subtree.
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
            
        # Case 2: Current node value is too large, prune the right subtree.
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
            
        # Case 3: Current node value is within range, include it and check both subtrees.
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)