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
        Space Complexity: O(H_root) for the recursion stack, where H_root is the 
        height of the 'root' tree.
        """
        # If the main tree is empty, it cannot contain any non-empty subtree.
        # (Given constraints say subRoot has at least 1 node).
        if not root:
            return False
        
        # Check if the tree rooted at the current 'root' is identical to 'subRoot'
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, recursively check the left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, they are identical
        if not p and not q:
            return True
        # If one is null and the other isn't, or their values differ, they aren't identical
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check if left subtrees and right subtrees are identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)