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
        Time Complexity: O(N) where N is the number of nodes in the tree.
        Space Complexity: O(H) where H is the height of the tree for the recursion stack.
        
        Algorithm:
        The root node always holds the minimum value of the entire tree.
        We perform a DFS traversal. For any node, if its value is greater than the 
        root's value, it is a candidate for the second minimum value. Since all 
        descendants of this node will be greater than or equal to this node's value, 
        we don't need to traverse its subtree further. If its value is equal to the 
        root's value, we must check both its left and right subtrees to look for a 
        larger value.
        """
        if not root:
            return -1
        
        # The absolute minimum value in the tree is always at the root.
        min_val = root.val
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return -1
            
            # Found a value strictly greater than the minimum value.
            # This is a potential second minimum, no need to look deeper in this branch.
            if node.val > min_val:
                return node.val
            
            # If node.val == min_val, we search both subtrees.
            left_val = dfs(node.left)
            right_val = dfs(node.right)
            
            # If both subtrees returned valid second minimum values, choose the smaller one.
            if left_val != -1 and right_val != -1:
                return min(left_val, right_val)
            
            # If only one subtree returned a valid value, return that one.
            return left_val if left_val != -1 else right_val

        return dfs(root)