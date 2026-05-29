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

# We assume TreeNode is either defined in the solution module or standardly structured.
# Providing a local definition/fallback for the test harness structure if needed.
if hasattr(sol_module, 'TreeNode'):
    TreeNode = sol_module.TreeNode
else:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class TestMaxPathSum(unittest.TestCase):

    def test_example_1(self):
        """Tests standard small tree: root = [1,2,3], Expected = 6"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        
        sol = Solution()
        self.assertEqual(sol.maxPathSum(root), 6)

    def test_example_2(self):
        """Tests tree with negatives: root = [-10,9,20,null,null,15,7], Expected = 42"""
        root = TreeNode(-10)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        
        sol = Solution()
        self.assertEqual(sol.maxPathSum(root), 42)

    def test_single_node_positive(self):
        """Tests constraint lower bound: Single node with positive value"""
        root = TreeNode(42)
        sol = Solution()
        self.assertEqual(sol.maxPathSum(root), 42)

    def test_single_node_negative(self):
        """Tests constraint lower bound: Single node with negative value"""
        root = TreeNode(-5)
        sol = Solution()
        self.assertEqual(sol.maxPathSum(root), -5)

    def test_all_negative_nodes(self):
        """Tests a tree where all node values are negative"""
        root = TreeNode(-10)
        root.left = TreeNode(-20)
        root.right = TreeNode(-3)
        
        sol = Solution()
        self.assertEqual(sol.maxPathSum(root), -3)

    def test_negative_root_positive_branches(self):
        """Tests a tree where root is negative but subtrees yield a higher path sum without root"""
        root = TreeNode(-10)
        root.left = TreeNode(15)
        root.right = TreeNode(20)
        
        sol = Solution()
        # Paths could be 15, 20, or 15 + (-10) + 20 = 25. Max is 25.
        self.assertEqual(sol.maxPathSum(root), 25)

    def test_negative_leaf_nodes(self):
        """Tests a tree where leaf nodes are highly negative and should be excluded"""
        root = TreeNode(10)
        root.left = TreeNode(-5)
        root.right = TreeNode(-2)
        
        sol = Solution()
        self.assertEqual(sol.maxPathSum(root), 10)

    def test_unbalanced_left_skewed(self):
        """Tests a long left-skewed chain of nodes"""
        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(3)
        root.left.left.left = TreeNode(-1)
        
        sol = Solution()
        self.assertEqual(sol.maxPathSum(root), 12)