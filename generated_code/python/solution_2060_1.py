from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # Map each root's value to its corresponding tree root node
        # Since all root values are unique, this mapping is 1-to-1
        nodes_by_val = {t.val: t for t in trees}
        
        # Count the occurrences of all leaf node values
        leaf_counts = {}
        for t in trees:
            if t.left:
                leaf_counts[t.left.val] = leaf_counts.get(t.left.val, 0) + 1
            if t.right:
                leaf_counts[t.right.val] = leaf_counts.get(t.right.val, 0) + 1
                
        # The ultimate root of the single merged BST cannot be a leaf of any other tree.
        # Find the root node whose value does not appear in the leaf_counts map.
        root = None
        for t in trees:
            if t.val not in leaf_counts:
                if root is not None:
                    # If there's more than one potential root, they cannot be merged into a single tree
                    return None
                root = t
                
        if not root:
            return None
            
        # Track the number of unique trees successfully attached/visited to ensure
        # all provided trees are part of the final merged structure.
        visited_count = 0
        
        # Traverse the trees and plug in the matching subtrees while validating BST property on-the-fly.
        # min_val and max_val maintain the strict boundaries required for a valid BST.
        def isValidBST(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True
                
            # Current node value must strictly be within the boundaries
            if not (min_val < node.val < max_val):
                return False
                
            # If this is a leaf node, check if we can expand it by attaching another tree root
            if not node.left and not node.right:
                if node.val in nodes_by_val and node != root:
                    # Replace leaf with the corresponding tree root
                    matched_tree = nodes_by_val[node.val]
                    node.left = matched_tree.left
                    node.right = matched_tree.right
                    nonlocal visited_count
                    visited_count += 1
                    
            # Recursively validate left and right subtrees with updated constraints
            return (isValidBST(node.left, min_val, node.val) and 
                    isValidBST(node.right, node.val, max_val))
                    
        # Start validation from the ultimate root with infinity bounds
        if isValidBST(root, float('-inf'), float('inf')) and visited_count == len(trees) - 1:
            return root
            
        return None