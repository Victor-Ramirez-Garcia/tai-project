import os
import sys
import importlib.util
import unittest
from typing import Optional

# Dynamic loading of the solution module
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

# Reconstruct or reference TreeNode from the solution module if available,
# otherwise define a standard one to build the test cases.
if hasattr(sol_module, 'TreeNode'):
    TreeNode = sol_module.TreeNode
else:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right


class TestIsValidBST(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1_valid_bst(self):
        # Input: root = [2,1,3] -> True
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        self.assertTrue(self.sol.isValidBST(root))

    def test_example_2_invalid_bst(self):
        # Input: root = [5,1,4,null,null,3,6] -> False
        root = TreeNode(5)
        root.left = TreeNode(1)
        root.right = TreeNode(4)
        root.right.left = TreeNode(3)
        root.right.right = TreeNode(6)
        self.assertFalse(self.sol.isValidBST(root))

    def test_single_node_tree(self):
        # Single node tree is always a valid BST
        root = TreeNode(0)
        self.assertTrue(self.sol.isValidBST(root))

    def test_invalid_left_child_equal_to_parent(self):
        # BST requires keys to be strictly less/greater than parent
        root = TreeNode(10)
        root.left = TreeNode(10)
        self.assertFalse(self.sol.isValidBST(root))

    def test_invalid_right_child_equal_to_parent(self):
        # BST requires keys to be strictly less/greater than parent
        root = TreeNode(10)
        root.right = TreeNode(10)
        self.assertFalse(self.sol.isValidBST(root))

    def test_invalid_sub_child_violating_ancestor_constraint_right_side(self):
        # A node in the right subtree of the root must be strictly greater than the root
        # Tree: [10, 5, 15, null, null, 6, 20]
        # 6 is in the right subtree of 10, which violates the BST property.
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(20)
        self.assertFalse(self.sol.isValidBST(root))

    def test_invalid_sub_child_violating_ancestor_constraint_left_side(self):
        # A node in the left subtree of the root must be strictly less than the root
        # Tree: [10, 5, 15, 1, 11, null, null]
        # 11 is in the left subtree of 10, which violates the BST property.
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(11)
        self.assertFalse(self.sol.isValidBST(root))

    def test_extreme_values_valid(self):
        # Tree with large system values (simulating constraints limits)
        # Using 64-bit integer representation extreme values if handled properly
        root = TreeNode(0)
        root.left = TreeNode(-2147483648)
        root.right = TreeNode(2147483647)
        self.assertTrue(self.sol.isValidBST(root))


if __name__ == "__main__":
    unittest.main()