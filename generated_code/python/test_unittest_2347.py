import unittest
import os
import importlib.util

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

# Helper for building trees in tests
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TestAverageOfSubtree(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_general_tree(self):
        """Tests the first example: root = [4,8,5,0,1,null,6] -> Output: 5"""
        # Construction:
        #        4
        #      /   \
        #     8     5
        #    / \     \
        #   0   1     6
        node6 = TreeNode(6)
        node1 = TreeNode(1)
        node0 = TreeNode(0)
        node5 = TreeNode(5, None, node6)
        node8 = TreeNode(8, node0, node1)
        root = TreeNode(4, node8, node5)
        
        self.assertEqual(self.sol.averageOfSubtree(root), 5)

    def test_example_2_single_node(self):
        """Tests the second example: root = [1] -> Output: 1"""
        root = TreeNode(1)
        self.assertEqual(self.sol.averageOfSubtree(root), 1)

    def test_minimum_node_value(self):
        """Tests a tree where all node values are 0 (minimum constraint)."""
        root = TreeNode(0, TreeNode(0), TreeNode(0))
        # All 3 nodes meet the criteria (0/1=0 or 0/3=0)
        self.assertEqual(self.sol.averageOfSubtree(root), 3)

    def test_rounding_down_behavior(self):
        """Tests if the floor division (rounding down) is handled correctly."""
        # Subtree sum: 10 + 1 = 11. Count: 2. Average: 11 // 2 = 5.
        # Root is 10, average is 5. Root != Average.
        # Leaf is 1, average is 1. Leaf == Average.
        root = TreeNode(10, TreeNode(1))
        self.assertEqual(self.sol.averageOfSubtree(root), 1)

    def test_unbalanced_skewed_tree(self):
        """Tests a right-skewed tree."""
        # [1, null, 2, null, 3]
        # Node 3: 3/1 = 3 (Match)
        # Node 2: (2+3)/2 = 2 (Match)
        # Node 1: (1+2+3)/3 = 2 (No Match)
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        self.assertEqual(self.sol.averageOfSubtree(root), 2)

    def test_large_values_sum(self):
        """Tests that the sum of nodes doesn't cause issues with large constraints."""
        # Assuming max node value is 1000 and max nodes is 1000.
        root = TreeNode(1000, TreeNode(1000), TreeNode(1000))
        self.assertEqual(self.sol.averageOfSubtree(root), 3)

    def test_no_matches(self):
        """Tests a case where only leaves can match, but internal nodes don't."""
        # Root 10, child 0. Avg = 5. No match for root.
        root = TreeNode(10, TreeNode(0))
        # Only the leaf 0 matches 0/1.
        self.assertEqual(self.sol.averageOfSubtree(root), 1)

if __name__ == "__main__":
    unittest.main()