from typing import List, Optional, Dict, Set

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        # Algorithmic Strategy: Graph/Tree reconstruction with validation.
        # 1. Map each root value to its corresponding tree root for quick lookup.
        # 2. Count the occurrences of all leaf node values across all trees.
        # 3. The true root of the combined tree cannot be a leaf of any other tree. 
        #    Thus, the root candidate must have a root value with a leaf count of 0.
        # 4. Traverse the combined tree from the candidate root, stitching leaves 
        #    to matching roots dynamically, and ensuring it forms a valid BST.
        # 5. Finally, verify that all original trees were successfully merged into one.

        # Map root value to its root node
        roots: Dict[int, TreeNode] = {tree.val: tree for tree in trees}
        
        # Track frequencies of leaf values across all trees
        leaf_counts: Dict[int, int] = {}
        for tree in trees:
            if tree.left:
                leaf_counts[tree.left.val] = leaf_counts.get(tree.left.val, 0) + 1
            if tree.right:
                leaf_counts[tree.right.val] = leaf_counts.get(tree.right.val, 0) + 1

        # The root of the merged tree must not appear as a leaf in any tree
        root_candidate = None
        for tree in trees:
            if tree.val not in leaf_counts:
                if root_candidate is not None:
                    # More than one root candidate means the trees cannot be fully merged into a single component
                    return None
                root_candidate = tree

        if not root_candidate:
            return None

        # Track visited root nodes to prevent infinite loops / cycles during traversal
        visited_roots: Set[int] = set()

        # In-order traversal to stitch trees and validate the BST property simultaneously
        # We pass lower and upper bounds to enforce strict BST properties
        def traverse(node: Optional[TreeNode], low: float, high: float) -> bool:
            if not node:
                return True
            
            # Check if current node violates BST constraints
            if not (low < node.val < high):
                return False

            # If it's a leaf and matches another tree's root, stitch it
            if not node.left and not node.right and node.val in roots:
                if node.val in visited_roots:
                    return False # Cycle detected
                
                child_root = roots[node.val]
                visited_roots.add(node.val)
                
                # Attach the children of the matching root to the current leaf
                node.left = child_root.left
                node.right = child_root.right

            # Recursively validate left and right subtrees with updated bounds
            return (traverse(node.left, low, node.val) and 
                    traverse(node.right, node.val, high))

        # Mark the main root as visited
        visited_roots.add(root_candidate.val)

        # Run validation and check if all given trees were successfully merged
        # Since the problem states each BST has at most 3 nodes, the total number of operations 
        # required to merge n trees is exactly n-1. Therefore, we must visit all n roots.
        if traverse(root_candidate, float('-inf'), float('inf')) and len(visited_roots) == len(trees):
            return root_candidate
        
        return None