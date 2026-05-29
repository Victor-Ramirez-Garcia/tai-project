import os
import importlib.util
import unittest
from typing import Optional

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

# Since TreeNode definition might be inside or outside the module, 
# we handle it robustly or use a local definition that matches the structure.
if hasattr(sol_module, 'TreeNode'):
    TreeNode = sol_module.TreeNode
else:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class TestRangeSumBST(unittest.TestCase):

    def helper_build_tree_from_list(self, nodes_list) -> Optional[TreeNode]:
        """Helper method to construct a binary tree from a list (level-order)."""
        if not nodes_list or nodes_list[0] is None:
            return None
        
        root = TreeNode(nodes_list[0])
        queue = [root]
        front = 0
        index = 1
        
        while index < len(nodes_list):
            node = queue[front]
            front += 1
            
            # Left child
            if index < len(nodes_list) and nodes_list[index] is not None:
                node.left = TreeNode(nodes_list[index])
                queue.append(node.left)
            index += 1
            
            # Right child
            if index < len(nodes_list) and nodes_list[index] is not None:
                node.right = TreeNode(nodes_list[index])
                queue.append(node.right)
            index += 1
            
        return root

    def test_example_1(self):
        # Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
        # Output: 32
        nodes = [10, 5, 15, 3, 7, None, 18]
        root = self.helper_build_tree_from_list(nodes)
        sol = Solution()
        self.assertEqual(sol.rangeSumBST(root, 7, 15), 32)

    def test_example_2(self):
        # Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
        # Output: 23
        nodes = [10, 5, 15, 3, 7, 13, 18, 1, None, 6]
        root = self.helper_build_tree_from_list(nodes)
        sol = Solution()
        self.assertEqual(sol.rangeSumBST(root, 6, 10), 23)

    def test_single_node_in_range(self):
        # Single node that falls within the range
        root = TreeNode(10)
        sol = Solution()
        self.assertEqual(sol.rangeSumBST(root, 5, 15), 10)

    def test_single_node_out_of_range_low(self):
        # Single node below the range
        root = TreeNode(5)
        sol = Solution()
        self.assertEqual(sol.rangeSumBST(root, 10, 20), 0)

    def test_single_node_out_of_range_high(self):
        # Single node above the range
        root = TreeNode(25)
        sol = Solution()
        self.assertEqual(sol.rangeSumBST(root, 10, 20), 0)

    def test_all_nodes_in_range(self):
        # All nodes in the tree satisfy the condition
        nodes = [10, 8, 12]
        root = self.helper_build_tree_from_list(nodes)
        sol = Solution()
        self.assertEqual(sol.rangeSumBST(root, 5, 15), 30)

    def test_no_nodes_in_range(self):
        # Tree elements are completely outside the range
        nodes = [50, 40, 60]
        root = self.helper_build_tree_from_list(nodes)
        sol = Solution()
        self.assertEqual(sol.rangeSumBST(root, 5, 15), 0)

    def test_exact_boundary_match(self):
        # Range boundaries match existing elements exactly
        nodes = [10, 5, 15]
        root = self.helper_build_tree_from_list(nodes)
        sol = Solution()
        self.assertEqual(sol.rangeSumBST(root, 5, 15), 30)

    def test_maximum_constraints(self):
        # Testing max value constraints for node value, low, and high
        root = TreeNode(100000)
        sol = Solution()
        self.assertEqual(sol.rangeSumBST(root, 100000, 100000), 100000)


if __name__ == "__main__":
    unittest.main()