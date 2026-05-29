from typing import Optional, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        """
        Algorithm: Post-order Traversal (DFS)
        
        To calculate the average of each subtree, we need two pieces of information 
        from the left and right child subtrees:
        1. The sum of all node values in that subtree.
        2. The count of all nodes in that subtree.
        
        Using a post-order traversal (bottom-up approach) allows us to compute these 
        metrics for the current node efficiently in O(1) time once its children are processed.
        
        Time Complexity: O(N) where N is the number of nodes in the binary tree, 
                         as we visit each node exactly once.
        Space Complexity: O(H) where H is the height of the tree, representing the 
                          maximum memory consumed by the recursion stack.
        """
        self.matching_nodes_count = 0
        
        def calculate_subtree_metrics(node: Optional[TreeNode]) -> Tuple[int, int]:
            if not node:
                # Base case: (subtree_sum, subtree_count)
                return 0, 0
            
            # Recurse on left and right subtrees
            left_sum, left_count = calculate_subtree_metrics(node.left)
            right_sum, right_count = calculate_subtree_metrics(node.right)
            
            # Aggregate values for the current subtree
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1
            
            # Calculate the average rounded down to the nearest integer
            if current_sum // current_count == node.val:
                self.matching_nodes_count += 1
                
            return current_sum, current_count
        
        calculate_subtree_metrics(root)
        return self.matching_nodes_count