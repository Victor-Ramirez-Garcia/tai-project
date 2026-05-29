import os
import importlib.util
import unittest
from typing import Optional, List

# Define TreeNode locally for the tests to construct the input trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestLongestUnivaluePath(unittest.TestCase):
    
    def _build_tree_from_list(self, nodes: List[Optional[int]]) -> Optional[TreeNode]:
        """Helper method to construct a binary tree from a LeetCode-style list."""
        if not nodes or nodes[0] is None:
            return None
        
        root = TreeNode(nodes[0])
        queue = [root]
        front = 0
        index = 1
        
        while index < len(nodes):
            node = queue[front]
            front += 1
            
            if index < len(nodes) and nodes[index] is not None:
                node.left = TreeNode(nodes[index])
                queue.append(node.left)
            index += 1
            
            if index < len(nodes) and nodes[index] is not None:
                node.right = TreeNode(nodes[index])
                queue.append(node.right)
            index += 1
            
        return root

    def test_example_1(self):
        # root = [5, 4, 5, 1, 1, null, 5] -> Output: 2
        root_list = [5, 4, 5, 1, 1, None, 5]
        root = self._build_tree_from_list(root_list)
        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(root), 2)

    def test_example_2(self):
        # root = [1, 4, 5, 4, 4, null, 5] -> Output: 2
        root_list = [1, 4, 5, 4, 4, None, 5]
        root = self._build_tree_from_list(root_list)
        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(root), 2)

    def test_empty_tree(self):
        # Constraint: The number of nodes can be 0.
        root = self._build_tree_from_list([])
        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(root), 0)

    def test_single_node(self):
        # Single node tree has 0 edges.
        root = TreeNode(1)
        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(root), 0)

    def test_all_nodes_same_value(self):
        # Balanced tree where all nodes have the same value.
        root_list = [1, 1, 1, 1, 1, 1, 1]
        root = self._build_tree_from_list(root_list)
        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(root), 4)

    def test_no_matching_values(self):
        # Tree where every node has a unique value.
        root_list = [1, 2, 3, 4, 5, 6, 7]
        root = self._build_tree_from_list(root_list)
        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(root), 0)

    def test_negative_values(self):
        # Constraint: -1000 <= Node.val <= 1000
        root_list = [-5, -5, -5, 1, -5, None, None]
        root = self._build_tree_from_list(root_list)
        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(root), 2)

    def test_skewed_tree_univalue(self):
        # Linear/skewed tree with all identical values.
        # 10 -> 10 -> 10 -> 10 (3 edges)
        root = TreeNode(10)
        curr = root
        for _ in range(3):
            curr.left = TreeNode(10)
            curr = curr.left
        sol = Solution()
        self.assertEqual(sol.longestUnivaluePath(root), 3)


if __name__ == "__main__":
    unittest.main()