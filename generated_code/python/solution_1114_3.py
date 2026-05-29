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
        Since the tree is a Binary Search Tree (BST), the nodes visited in a standard 
        in-order traversal would be sorted in ascending order. By reversing the 
        traversal order to Right -> Node -> Left, we visit the nodes in descending order.
        
        As we traverse, we maintain a running total (`self.total_sum`) of all values seen 
        so far. For each node, we add its original value to the running total and then 
        update the node's value with this total.
        
        Complexity:
        - Time Complexity: O(N) where N is the number of nodes in the tree, as we visit each node exactly once.
        - Space Complexity: O(H) where H is the height of the tree, representing the recursion stack space.
          In the worst case (skewed tree), H = O(N); in the best case (balanced tree), H = O(log N).
        """
        self.total_sum = 0
        
        def traverse(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            # 1. Traverse the right subtree (contains greater values)
            traverse(node.right)
            
            # 2. Update the running sum and the current node's value
            self.total_sum += node.val
            node.val = self.total_sum
            
            # 3. Traverse the left subtree (contains smaller values)
            traverse(node.left)
            
        traverse(root)
        return root