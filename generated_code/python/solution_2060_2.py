from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        """
        Time Complexity: O(N) where N is the total number of nodes across all trees.
        Space Complexity: O(N) to store nodes, maps, and visited sets.
        
        Strategy:
        1. Every merged tree root (except the absolute root of the final tree) must match 
           exactly one leaf in another tree. Thus, any value that appears as a root *and* as a leaf is a connection point.
        2. Identify all leaf values across all trees.
        3. Find the unique tree root that does NOT appear as a leaf anywhere. This must 
           be the root of the single final BST. If there isn't exactly one such root, 
           it's impossible to form a single tree.
        4. Perform a DFS/traversal starting from this candidate root, stitching trees 
           together whenever a leaf matches another tree's root.
        5. Validate that the stitched tree covers all given trees and is a valid BST.
        """
        # Map root value to its corresponding TreeNode for O(1) lookup during merging
        root_map = {tree.val: tree for tree in trees}
        
        # Collect all leaf values across all trees
        leaves = set()
        for tree in trees:
            if tree.left:
                leaves.add(tree.left.val)
            if tree.right:
                leaves.add(tree.right.val)
                
        # The global root must be a root that is not a leaf of any tree
        global_root = None
        for tree in trees:
            if tree.val not in leaves:
                if global_root is not None:
                    # More than one root is not a leaf -> multiple components/roots
                    return None
                global_root = tree
                
        if not global_root:
            return None
            
        # Track visited root values to prevent infinite cycles during stitching
        visited_roots = set()
        
        def traverse_and_stitch(node: Optional[TreeNode]) -> bool:
            if not node:
                return True
            
            # Check if this node is a leaf and can be replaced by another tree's root
            if not node.left and not node.right:
                if node.val in root_map and node.val not in visited_roots:
                    root_to_merge = root_map[node.val]
                    visited_roots.add(node.val)
                    # Replace leaf with the children of the matching root
                    node.left = root_to_merge.left
                    node.right = root_to_merge.right
            
            # Recursively process children
            return traverse_and_stitch(node.left) and traverse_and_stitch(node.right)
            
        # Initialize visited with the global root
        visited_roots.add(global_root.val)
        traverse_and_stitch(global_root)
        
        # All individual trees must be merged into the single component
        if len(visited_roots) != len(trees):
            return None
            
        # Validate if the stitched tree is a valid BST
        def isValidBST(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return (isValidBST(node.left, min_val, node.val) and 
                    isValidBST(node.right, node.val, max_val))
                    
        if not isValidBST(global_root, float('-inf'), float('inf')):
            return None
            
        return global_root