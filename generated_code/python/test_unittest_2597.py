import os
import importlib.util
import unittest

# Dynamic loading of the Solution class as mandated by the instructions
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("Environment variable 'TEST_SOLUTION_FILE' is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestCycleLengthQueries(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        """Validates Example 1 from the problem statement description."""
        n = 3
        queries = [[5, 3], [4, 7], [2, 3]]
        expected = [4, 5, 3]
        self.assertEqual(self.sol.cycleLengthQueries(n, queries), expected)

    def test_example_2(self):
        """Validates Example 2 from the problem statement description."""
        n = 2
        queries = [[1, 2]]
        expected = [2]
        self.assertEqual(self.sol.cycleLengthQueries(n, queries), expected)

    def test_same_node_query(self):
        """Validates behavior when a query connects a node to itself (forms a self-loop cycle of length 1)."""
        n = 3
        queries = [[3, 3], [1, 1]]
        expected = [1, 1]
        self.assertEqual(self.sol.cycleLengthQueries(n, queries), expected)

    def test_direct_parent_child_edge(self):
        """Validates when an edge is added between a direct parent and child, creating a cycle of length 2."""
        n = 4
        queries = [[2, 4], [3, 7], [1, 2]]
        expected = [2, 2, 2]
        self.assertEqual(self.sol.cycleLengthQueries(n, queries), expected)

    def test_siblings(self):
        """Validates when an edge is added between sibling nodes sharing the exact same parent."""
        n = 3
        queries = [[2, 3], [4, 5], [6, 7]]
        expected = [3, 3, 3]
        self.assertEqual(self.sol.cycleLengthQueries(n, queries), expected)

    def test_deep_tree_nodes_max_constraints(self):
        """Validates constraints approaching maximum deep paths in a large binary tree."""
        n = 30
        # Connecting deep leaf node to the root, and deep leaves across different subtrees
        queries = [
            [1, 536870912],      # 1 to 2^29 (deep left node) -> cycle length should be 30
            [536870912, 1073741823]  # 2^29 to 2^30 - 1 (deep left leaf to deep right leaf)
        ]
        expected = [30, 59]
        self.assertEqual(self.sol.cycleLengthQueries(n, queries), expected)

    def test_empty_queries(self):
        """Validates performance and correctness when the queries array is completely empty."""
        n = 5
        queries = []
        expected = []
        self.assertEqual(self.sol.cycleLengthQueries(n, queries), expected)


if __name__ == "__main__":
    unittest.main()