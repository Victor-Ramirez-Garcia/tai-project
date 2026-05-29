import os
import importlib.util
import unittest

# Dynamic loading of the Solution class as mandated by the guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestMinCostGridPath(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_multiple_modifications(self):
        """
        Tests Example 1: A grid requiring multiple directional changes 
        to snake down to the bottom-right destination.
        """
        grid = [
            [1, 1, 1, 1],
            [2, 2, 2, 2],
            [1, 1, 1, 1],
            [2, 2, 2, 2]
        ]
        expected_output = 3
        self.assertEqual(self.sol.minCost(grid), expected_output)

    def test_example_2_zero_cost(self):
        """
        Tests Example 2: The existing arrows already form a valid, 
        uninterrupted path to the destination without modifications.
        """
        grid = [
            [1, 1, 3],
            [3, 2, 2],
            [1, 1, 4]
        ]
        expected_output = 0
        self.assertEqual(self.sol.minCost(grid), expected_output)

    def test_example_3_small_grid_with_cost(self):
        """
        Tests Example 3: A minimal 2x2 grid requiring exactly one 
        modification to reach the bottom-right corner.
        """
        grid = [
            [1, 2],
            [4, 3]
        ]
        expected_output = 1
        self.assertEqual(self.sol.minCost(grid), expected_output)

    def test_edge_case_single_cell(self):
        """
        Tests the absolute minimum constraint: A 1x1 grid.
        Starting and ending positions are identical, so cost must be 0.
        """
        grid = [[1]]
        expected_output = 0
        self.assertEqual(self.sol.minCost(grid), expected_output)

    def test_edge_case_single_row_straight(self):
        """
        Tests a 1xN grid where all arrows naturally point right.
        No modifications should be required.
        """
        grid = [[1, 1, 1, 1, 1]]
        expected_output = 0
        self.assertEqual(self.sol.minCost(grid), expected_output)

    def test_edge_case_single_row_wrong_directions(self):
        """
        Tests a 1xN grid where arrows point away or down, 
        requiring corrections to move strictly right.
        """
        grid = [[2, 3, 4, 2, 1]]
        # (0,0)->(0,1) cost 1; (0,1)->(0,2) cost 1; (0,2)->(0,3) cost 1; (0,3)->(0,4) cost 1.
        # The last cell doesn't need modification. Total cost = 4.
        expected_output = 4
        self.assertEqual(self.sol.minCost(grid), expected_output)

    def test_edge_case_single_column_straight(self):
        """
        Tests an Mx1 grid where all arrows naturally point down.
        No modifications should be required.
        """
        grid = [[3], [3], [3], [3]]
        expected_output = 0
        self.assertEqual(self.sol.minCost(grid), expected_output)

    def test_edge_case_single_column_wrong_directions(self):
        """
        Tests an Mx1 grid where arrows point sideways or up, 
        requiring corrections to move strictly down.
        """
        grid = [[1], [2], [4], [3]]
        # (0,0)->(1,0) cost 1; (1,0)->(2,0) cost 1; (2,0)->(3,0) cost 1. Total cost = 3.
        expected_output = 3
        self.assertEqual(self.sol.minCost(grid), expected_output)

    def test_all_cells_pointing_away(self):
        """
        Tests a grid where every cell points in the worst possible direction 
        (e.g., pointing left or up), forcing modifications at almost every step.
        """
        grid = [
            [2, 2, 2],
            [4, 4, 4],
            [4, 4, 4]
        ]
        # One optimal path: (0,0)->(0,1)->(0,2)->(1,2)->(2,2)
        # Changes needed at: (0,0) to 1, (0,1) to 1, (0,2) to 3, (1,2) to 3. Total cost = 4.
        expected_output = 4
        self.assertEqual(self.sol.minCost(grid), expected_output)


if __name__ == "__main__":
    unittest.main()