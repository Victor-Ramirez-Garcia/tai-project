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


class TestPutMarbles(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        # Example 1 from problem description
        weights = [1, 3, 5, 1]
        k = 2
        expected = 4
        self.assertEqual(self.sol.putMarbles(weights, k), expected)

    def test_example_2(self):
        # Example 2 from problem description
        weights = [1, 3]
        k = 2
        expected = 0
        self.assertEqual(self.sol.putMarbles(weights, k), expected)

    def test_single_bag(self):
        # When k = 1, there is only one way to distribute all marbles.
        # Max score and min score are identical, so difference is 0.
        weights = [1, 3, 5, 1, 9]
        k = 1
        expected = 0
        self.assertEqual(self.sol.putMarbles(weights, k), expected)

    def test_bags_equal_to_marbles(self):
        # When k == len(weights), every marble is in its own bag.
        # There is only one valid distribution, so difference is 0.
        weights = [4, 2, 7, 1, 5]
        k = 5
        expected = 0
        self.assertEqual(self.sol.putMarbles(weights, k), expected)

    def test_minimum_constraints(self):
        # Smallest possible valid input constraints
        weights = [5]
        k = 1
        expected = 0
        self.assertEqual(self.sol.putMarbles(weights, k), expected)

    def test_identical_weights(self):
        # All weights are the same. Any split yields the same pair sums.
        weights = [2, 2, 2, 2, 2]
        k = 3
        expected = 0
        self.assertEqual(self.sol.putMarbles(weights, k), expected)

    def test_large_values(self):
        # Ensure handling of larger values and proper sorting/difference mechanics
        weights = [10, 20, 30, 40, 50]
        k = 3
        # Pair sums: 10+20=30, 20+30=50, 30+40=70, 40+50=90
        # Sorted pair sums: [30, 50, 70, 90]
        # For k=3, we need to pick k-1 = 2 splits.
        # Max pair sums picked: 70 + 90 = 160
        # Min pair sums picked: 30 + 50 = 80
        # Expected difference: 160 - 80 = 80
        expected = 80
        self.assertEqual(self.sol.putMarbles(weights, k), expected)


if __name__ == "__main__":
    unittest.main()