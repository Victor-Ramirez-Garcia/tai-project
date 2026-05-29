import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestFillCups(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Example Test Cases ---

    def test_example_1(self):
        """Validates Example 1: Regular mix of cups where one is dominant but balanced by others."""
        self.assertEqual(self.sol.fillCups([1, 4, 2]), 4)

    def test_example_2(self):
        """Validates Example 2: Balanced high values where total sum determines the ceiling."""
        self.assertEqual(self.sol.fillCups([5, 4, 4]), 7)

    def test_example_3(self):
        """Validates Example 3: Only one type of cup is needed, others are zero."""
        self.assertEqual(self.sol.fillCups([5, 0, 0]), 5)

    # --- Edge Cases from Constraints ---

    def test_all_zeros(self):
        """Validates minimum constraint: No cups need to be filled."""
        self.assertEqual(self.sol.fillCups([0, 0, 0]), 0)

    def test_single_cup(self):
        """Validates scenario where exactly one total cup needs to be filled."""
        self.assertEqual(self.sol.fillCups([0, 1, 0]), 1)

    def test_maximum_values_balanced(self):
        """Validates maximum constraint (100) when all values are at their upper bound."""
        self.assertEqual(self.sol.fillCups([100, 100, 100]), 150)

    def test_maximum_values_one_dominant(self):
        """Validates maximum constraint where one value drastically outnumbers the others."""
        self.assertEqual(self.sol.fillCups([100, 1, 2]), 100)

    # --- Additional Boundary and Permutation Cases ---

    def test_order_permutations(self):
        """Ensures the algorithm handles different array orderings identically."""
        self.assertEqual(self.sol.fillCups([1, 2, 4]), 4)
        self.assertEqual(self.sol.fillCups([4, 1, 2]), 4)
        self.assertEqual(self.sol.fillCups([2, 4, 1]), 4)

    def test_two_types_equal(self):
        """Validates when two types of cups are equal and the third is zero."""
        self.assertEqual(self.sol.fillCups([10, 10, 0]), 10)

    def test_sum_is_odd(self):
        """Validates math ceiling division when the total sum of cups is odd."""
        self.assertEqual(self.sol.fillCups([3, 3, 3]), 5)


if __name__ == "__main__":
    unittest.main()