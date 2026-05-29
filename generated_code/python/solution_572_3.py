from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Time Complexity: O(N * M), where N is the number of nodes in 'root' and M is the number of nodes in 'subRoot'.
        Space Complexity: O(H_N), where H_N is the height of the 'root' tree, due to the recursion stack.
        Algorithm: DFS / Tree Traversal. We check if the current tree rooted at 'root' is identical to 'subRoot'.
        If not, we recursively check if 'subRoot' is a subtree of the left or right child.
        """
        # If root is None, subRoot cannot be a subtree of it (since subRoot has at least 1 node per constraints)
        if not root:
            return False
        
        # Check if the trees rooted at 'root' and 'subRoot' are identical
        if self.isSameTree(root, subRoot):
            return True
        
        # Recursively search in left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are None, the trees are identical
        if not p and not q:
            return True
        # If one of them is None or their values mismatch, they are not identical
        if not p or not q or p.val != q.val:
            return False
        
        # Check both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)