from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity: O(N) in the worst case, where N is the number of nodes.
                         We prune subtrees where the root value is already greater 
                         than the current global minimum, avoiding unnecessary traversals.
        Space Complexity: O(H) where H is the height of the tree, representing the recursion stack.
        """
        if not root:
            return -1
        
        # The root of the tree always holds the absolute minimum value of the entire tree.
        min_val = root.val
        self.second_min = float('inf')
        
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            # If the current node's value is greater than the absolute minimum,
            # it is a candidate for the second minimum value.
            if min_val < node.val < self.second_min:
                self.second_min = node.val
                
            # Crucial Pruning: If a node's value is greater than or equal to the 
            # currently found second minimum, its children cannot yield a smaller 
            # second minimum due to the tree's heap-like property (root = min(left, right)).
            if node.val < self.second_min:
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        
        # If second_min was never updated, it means all nodes have the same value.
        return self.second_min if self.second_min != float('inf') else -1