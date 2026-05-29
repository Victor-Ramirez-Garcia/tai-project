from typing import Optional, Tuple

# Definition for a binary tree node if not already defined by the runner.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.matching_nodes_count = 0
        
        # Post-order traversal helper function.
        # Returns a tuple: (sum_of_subtree_values, number_of_nodes_in_subtree)
        def traverse(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0
            
            # Recurse on left and right subtrees
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            
            # Calculate current subtree metrics
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Check if the node value equals the integer division average of the subtree
            if current_sum // current_count == node.val:
                self.matching_nodes_count += 1
                
            return current_sum, current_count
        
        traverse(root)
        return self.matching_nodes_count