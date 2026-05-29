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
        
        Algorithm: Optimized DFS / BST Pruning
        Time Complexity: O(N) in the worst case (where N is the number of nodes), 
                         but practically O(H + K) where H is height and K is number of valid nodes,
                         as we prune subtrees that fall entirely outside the range.
        Space Complexity: O(H) for the recursive call stack, where H is the height of the tree.
        """
        if not root:
            return 0
        
        # Case 1: Current node's value is less than the low bound.
        # All values in the left subtree will also be strictly less than low due to BST properties.
        # Therefore, we prune the left subtree and only search the right subtree.
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
            
        # Case 2: Current node's value is greater than the high bound.
        # All values in the right subtree will also be strictly greater than high.
        # Therefore, we prune the right subtree and only search the left subtree.
        if root.val > high:
            return self.rangeSumBST(root.left, low, high)
            
        # Case 3: Current node's value is within [low, high].
        # It contributes to the sum, and we must explore both left and right subtrees.
        return root.val + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)