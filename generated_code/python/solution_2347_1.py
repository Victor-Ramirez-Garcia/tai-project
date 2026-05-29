from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.matching_nodes_count = 0
        
        # Helper function that performs post-order traversal.
        # It returns a tuple: (sum_of_subtree_values, number_of_nodes_in_subtree)
        def traverse(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                return 0, 0
            
            # Post-order traversal: collect info from left and right children first
            left_sum, left_count = traverse(node.left)
            right_sum, right_count = traverse(node.right)
            
            # Calculate total sum and total count for the current subtree
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1
            
            # Check if the current node's value matches the integer division average
            if total_sum // total_count == node.val:
                self.matching_nodes_count += 1
                
            return total_sum, total_count

        traverse(root)
        return self.matching_nodes_count