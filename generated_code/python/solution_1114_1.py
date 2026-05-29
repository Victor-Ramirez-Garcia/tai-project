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
        Algorithm: Reverse In-Order Traversal (Right -> Root -> Left)
        
        Since it's a Binary Search Tree (BST), the rightmost nodes contain the largest values.
        By traversing the tree in reverse in-order, we visit nodes in strictly decreasing order.
        We maintain a running total `self.total_sum` of all nodes visited so far. For each node,
        we update its value by adding this cumulative sum to it, and then update the running total.
        
        Time Complexity: O(N) where N is the number of nodes, as we visit each node exactly once.
        Space Complexity: O(H) where H is the height of the tree, representing the recursion stack.
        """
        self.total_sum = 0
        
        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            # 1. Traverse the right subtree first (larger values)
            traverse(node.right)
            
            # 2. Process the current node
            self.total_sum += node.val
            node.val = self.total_sum
            
            # 3. Traverse the left subtree (smaller values)
            traverse(node.left)
            
        traverse(root)
        return root