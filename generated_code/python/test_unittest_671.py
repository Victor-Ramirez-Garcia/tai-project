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

# Retrieve TreeNode from the loaded module or define a compatible one if not exposed
if hasattr(sol_module, 'TreeNode'):
    TreeNode = sol_module.TreeNode
else:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

class TestFindSecondMinimumValue(unittest.TestCase):

    def test_example_1_has_second_minimum(self):
        """Test Example 1: Tree with distinct values where second minimum exists."""
        # Tree structure: [2, 2, 5, null, null, 5, 7]
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(7)
        
        sol = Solution()
        self.assertEqual(sol.findSecondMinimumValue(root), 5)

    def test_example_2_all_same_values(self):
        """Test Example 2: Tree where all node values are identical, returning -1."""
        # Tree structure: [2, 2, 2]
        root = TreeNode(2)
        root.left = TreeNode(2)
        root.right = TreeNode(2)
        
        sol = Solution()
        self.assertEqual(sol.findSecondMinimumValue(root), -1)

    def test_single_node_tree(self):
        """Test boundary case: A tree consisting of only a single root node."""
        root = TreeNode(10)
        
        sol = Solution()
        self.assertEqual(sol.findSecondMinimumValue(root), -1)

    def test_maximum_constraints_values(self):
        """Test constraints: Large node values near the 2^31 - 1 limit."""
        max_val = 2**31 - 1
        # Root holds the minimum of its children (42)
        root = TreeNode(42)
        root.left = TreeNode(42)
        root.right = TreeNode(max_val)
        
        sol = Solution()
        self.assertEqual(sol.findSecondMinimumValue(root), max_val)

    def test_skewed_value_distribution_left_branch(self):
        """Test deep tree scenario where the second minimum is on the left side."""
        root = TreeNode(3)
        root.left = TreeNode(3)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(3)
        
        sol = Solution()
        self.assertEqual(sol.findSecondMinimumValue(root), 4)

    def test_multiple_identical_second_minimums(self):
        """Test tree where the second minimum value appears in multiple independent leaf nodes."""
        root = TreeNode(10)
        root.left = TreeNode(10)
        root.right = TreeNode(10)
        root.left.left = TreeNode(20)
        root.left.right = TreeNode(10)
        root.right.left = TreeNode(10)
        root.right.right = TreeNode(20)
        
        sol = Solution()
        self.assertEqual(sol.findSecondMinimumValue(root), 20)