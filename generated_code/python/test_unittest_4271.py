import os
import importlib.util
import unittest

# Dynamic loading of the solution module via environment variable
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestFindDegrees(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_single_vertex_no_edges(self):
        """Tests a graph with a single vertex and no edges (1x1 matrix)."""
        matrix = [[0]]
        expected = [0]
        self.assertEqual(self.sol.findDegrees(matrix), expected)

    def test_single_vertex_self_loop(self):
        """Tests a graph with a single vertex that has a self-loop."""
        matrix = [[1]]
        expected = [1]
        self.assertEqual(self.sol.findDegrees(matrix), expected)

    def test_disconnected_graph(self):
        """Tests a multi-vertex graph where no vertices are connected."""
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected = [0, 0, 0]
        self.assertEqual(self.sol.findDegrees(matrix), expected)

    def test_fully_connected_graph_without_self_loops(self):
        """Tests a complete graph (every vertex connected to every other vertex except itself)."""
        matrix = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        expected = [2, 2, 2]
        self.assertEqual(self.sol.findDegrees(matrix), expected)

    def test_fully_connected_graph_with_self_loops(self):
        """Tests a complete graph where every vertex also connects to itself."""
        matrix = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        expected = [3, 3, 3]
        self.assertEqual(self.sol.findDegrees(matrix), expected)

    def test_asymmetric_degrees(self):
        """Tests a standard undirected graph with varying vertex degrees."""
        # Vertex 0 connected to 1, 2
        # Vertex 1 connected to 0
        # Vertex 2 connected to 0
        matrix = [[0, 1, 1], [1, 0, 0], [1, 0, 0]]
        expected = [2, 1, 1]
        self.assertEqual(self.sol.findDegrees(matrix), expected)

    def test_linear_path_graph(self):
        """Tests a graph forming a simple line path (0 - 1 - 2 - 3)."""
        matrix = [
            [0, 1, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 0],
        ]
        expected = [1, 2, 2, 1]
        self.assertEqual(self.sol.findDegrees(matrix), expected)


if __name__ == "__main__":
    unittest.main()