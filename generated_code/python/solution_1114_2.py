from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Algorithm: Reverse In-order Traversal (Right -> Node -> Left)
        Since this is a Binary Search Tree (BST), the nodes visited in a standard 
        in-order traversal are in ascending order. Doing a reverse in-order traversal 
        visits the nodes in descending order. 
        We maintain a running sum of all node values visited so far and add it to 
        the current node's value. This achieves O(N) time complexity and O(H) space 
        complexity, where H is the height of the tree.
        """
        running_sum = 0
        
        def traverse(node: Optional[TreeNode]) -> None:
            nonlocal running_sum
            if not node:
                return
            
            # Traverse the right subtree first (greater elements)
            traverse(node.right)
            
            # Update the running sum and the current node's value
            running_sum += node.val
            node.val = running_sum
            
            # Traverse the left subtree (smaller elements)
            traverse(node.left)
            
        traverse(root)
        return root