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
        Time Complexity: O(N * M) in the worst case, where N is the number of nodes 
        in 'root' and M is the number of nodes in 'subRoot'.
        Space Complexity: O(H_r + H_s) for the recursion stack, where H_r and H_s 
        are the heights of 'root' and 'subRoot' respectively.
        """
        # If the main tree is empty, it cannot contain any non-empty subRoot.
        # (Constraints specify subRoot has at least 1 node).
        if not root:
            return False
        
        # Check if the trees rooted at the current nodes are identical.
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, recursively check the left and right subtrees of 'root'.
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, the trees are identical.
        if not p and not q:
            return True
        # If only one of them is null, or their values don't match, they aren't identical.
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check if the left subtrees and right subtrees match.
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)