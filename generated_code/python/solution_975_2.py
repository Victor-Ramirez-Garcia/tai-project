from typing import Optional

# Definition for a binary tree node if not already defined in the environment.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        """
        Calculates the sum of values of all nodes in a BST within the inclusive range [low, high].
        
        Algorithm: DFS with Pruning ( memanfaatkan sifat Binary Search Tree )
        - Time Complexity: O(N) in the worst case, where N is the number of nodes. 
          On average, it prunes subtrees that fall completely outside the range, making it highly efficient.
        - Space Complexity: O(H) where H is the height of the tree, representing the recursion stack.
          In the worst case (skewed tree), H = O(N); for a balanced tree, H = O(log N).
        """
        if not root:
            return 0
        
        current_sum = 0
        
        # If the current node's value is within the range, include it in the sum
        if low <= root.val <= high:
            current_sum += root.val
            
        # If current value is greater than 'low', the left subtree might contain valid nodes
        if root.val > low:
            current_sum += self.rangeSumBST(root.left, low, high)
            
        # If current value is less than 'high', the right subtree might contain valid nodes
        if root.val < high:
            current_sum += self.rangeSumBST(root.right, low, high)
            
        return current_sum