import os
import importlib.util
import unittest
from typing import List, Optional

# Dynamic Loading Setup as required by guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution
TreeNode = sol_module.TreeNode


class TestBstToGst(unittest.TestCase):

    def _build_tree_from_list(self, nodes: List[Optional[int]]) -> Optional[TreeNode]:
        """Helper method to construct a binary tree from a LeetCode-style level-order list."""
        if not nodes or nodes[0] is None:
            return None

        root = TreeNode(nodes[0])
        queue = [root]
        front = 0
        index = 1

        while index < len(nodes):
            node = queue[front]
            front += 1

            # Left child
            if index < len(nodes) and nodes[index] is not None:
                node.left = TreeNode(nodes[index])
                queue.append(node.left)
            index += 1

            # Right child
            if index < len(nodes) and nodes[index] is not None:
                node.right = TreeNode(nodes[index])
                queue.append(node.right)
            index += 1

        return root

    def _tree_to_list(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        """Helper method to serialize a binary tree into a LeetCode-style level-order list."""
        if not root:
            return []

        result = []
        queue = [root]

        while queue:
            curr = queue.pop(0)
            if curr:
                result.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                result.append(None)

        # Trim trailing None elements to match standard LeetCode representation
        while result and result[-1] is None:
            result.pop()

        return result

    def test_example_1_standard_bst(self):
        """Tests the comprehensive BST provided in Example 1."""
        input_list = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
        expected_list = [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]

        root = self._build_tree_from_list(input_list)
        sol = Solution()
        modified_root = sol.bstToGst(root)
        actual_list = self._tree_to_list(modified_root)

        self.assertEqual(actual_list, expected_list)

    def test_example_2_minimal_right_skewed(self):
        """Tests the right-skewed minimal tree provided in Example 2."""
        input_list = [0, None, 1]
        expected_list = [1, None, 1]

        root = self._build_tree_from_list(input_list)
        sol = Solution()
        modified_root = sol.bstToGst(root)
        actual_list = self._tree_to_list(modified_root)

        self.assertEqual(actual_list, expected_list)

    def test_edge_case_empty_tree(self):
        """Tests constraints regarding an empty tree input (root is None)."""
        root = self._build_tree_from_list([])
        sol = Solution()
        modified_root = sol.bstToGst(root)
        actual_list = self._tree_to_list(modified_root)

        self.assertEqual(actual_list, [])

    def test_edge_case_single_node(self):
        """Tests the minimum operational bounds where the tree contains exactly one node."""
        input_list = [5]
        expected_list = [5]

        root = self._build_tree_from_list(input_list)
        sol = Solution()
        modified_root = sol.bstToGst(root)
        actual_list = self._tree_to_list(modified_root)

        self.assertEqual(actual_list, expected_list)

    def test_edge_case_left_skewed_chain(self):
        """Tests a strictly left-skewed tree to ensure accumulation propagates correctly upward."""
        input_list = [3, 2, None, 1, None]
        expected_list = [3, 5, None, 6, None]

        root = self._build_tree_from_list(input_list)
        sol = Solution()
        modified_root = sol.bstToGst(root)
        actual_list = self._tree_to_list(modified_root)

        self.assertEqual(actual_list, expected_list)

    def test_edge_case_right_skewed_chain(self):
        """Tests a strictly right-skewed tree to ensure accumulation sequences accurately downward."""
        input_list = [1, None, 2, None, 3]
        expected_list = [6, None, 5, None, 3]

        root = self._build_tree_from_list(input_list)
        sol = Solution()
        modified_root = sol.bstToGst(root)
        actual_list = self._tree_to_list(modified_root)

        self.assertEqual(actual_list, expected_list)


if __name__ == "__main__":
    unittest.main()