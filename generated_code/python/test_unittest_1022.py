import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

class TestUniquePathsIII(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        grid = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 2, -1]
        ]
        expected = 2
        self.assertEqual(self.sol.uniquePathsIII(grid), expected)

    def test_example_2(self):
        grid = [
            [1, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 2]
        ]
        expected = 4
        self.assertEqual(self.sol.uniquePathsIII(grid), expected)

    def test_example_3(self):
        grid = [
            [0, 1],
            [2, 0]
        ]
        expected = 0
        self.assertEqual(self.sol.uniquePathsIII(grid), expected)

    def test_minimal_grid_no_empty_squares_valid_path(self):
        # Only start and end squares, no 0s or obstacles. 
        # A valid path exists directly from 1 to 2.
        grid = [[1, 2]]
        expected = 1
        self.assertEqual(self.sol.uniquePathsIII(grid), expected)

    def test_minimal_grid_no_empty_squares_no_path(self):
        # Start and end squares are separated by an obstacle.
        grid = [[1, -1, 2]]
        expected = 0
        self.assertEqual(self.sol.uniquePathsIII(grid), expected)

    def test_no_possible_path_due_to_isolation(self):
        # The ending square is completely surrounded by obstacles and walls.
        grid = [
            [1,  0,  0],
            [-1, -1, -1],
            [2,  0,  0]
        ]
        expected = 0
        self.assertEqual(self.sol.uniquePathsIII(grid), expected)

    def test_dead_end_empty_square(self):
        # An empty square is trapped in a corner surrounded by obstacles,
        # making it impossible to visit all non-obstacle squares.
        grid = [
            [1,  0,  2],
            [-1, -1, 0]
        ]
        expected = 0
        self.assertEqual(self.sol.uniquePathsIII(grid), expected)

    def test_single_row_grid(self):
        grid = [[1, 0, 0, 2]]
        expected = 1
        self.assertEqual(self.sol.uniquePathsIII(grid), expected)

    def test_single_column_grid(self):
        grid = [
            [1],
            [0],
            [0],
            [2]
        ]
        expected = 1
        self.assertEqual(self.sol.uniquePathsIII(grid), expected)

if __name__ == "__main__":
    unittest.main()