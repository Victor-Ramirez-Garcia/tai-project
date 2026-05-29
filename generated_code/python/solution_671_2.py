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
        Algorithm: DFS with Pruning
        Time Complexity: O(N) where N is the number of nodes in the tree.
        Space Complexity: O(H) where H is the height of the tree for the recursion stack.
        
        The root node always holds the minimum value of the entire tree because
        root.val = min(root.left.val, root.right.val) holds everywhere.
        We can find the second minimum by scanning the tree. If a node's value is
        strictly greater than the root's value, it is a candidate for the second minimum,
        and we don't need to look into its subtrees (since all values below it will be >= it).
        """
        if not root:
            return -1
            
        # The absolute minimum value in the tree is always at the root.
        min_val = root.val
        self.second_min = float('inf')
        
        def dfs(node: Optional[TreeNode]) -> None:
            if not node:
                return
            
            # If the current node's value is strictly greater than the absolute minimum,
            # it's a potential second minimum candidate.
            if min_val < node.val < self.second_min:
                self.second_min = node.val
                
            # If a node's value equals the root value, its children might contain
            # the second minimum, so we continue exploring.
            # If a node's value is already greater than min_val, any value in its 
            # subtree will be >= node.val, which cannot be smaller than our current 
            # node.val candidate. Thus, we can safely prune and stop searching its subtree.
            if node.val == min_val:
                dfs(node.left)
                dfs(node.right)
                
        dfs(root)
        
        # If second_min was updated, return it; otherwise, return -1.
        return self.second_min if self.second_min != float('inf') else -1