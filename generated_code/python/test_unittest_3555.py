import os
import importlib.util
import unittest

# Dynamic loading of the solution module as mandated by guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("The environment variable 'TEST_SOLUTION_FILE' is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestGetFinalState(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1_standard_case(self):
        """Tests a standard mix of elements with a small number of operations."""
        # Equivalent to a standard LeetCode example case: nums = [2, 1, 3, 5, 6], k = 5, multiplier = 2
        # Op 1: min is 1 at idx 1 -> [2, 2, 3, 5, 6]
        # Op 2: min is 2 at idx 0 (first occurrence) -> [4, 2, 3, 5, 6]
        # Op 3: min is 2 at idx 1 -> [4, 4, 3, 5, 6]
        # Op 4: min is 3 at idx 2 -> [4, 4, 6, 5, 6]
        # Op 5: min is 4 at idx 0 -> [8, 4, 6, 5, 6]
        nums = [2, 1, 3, 5, 6]
        k = 5
        multiplier = 2
        expected = [8, 4, 6, 5, 6]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_example_2_tie_breaking(self):
        """Tests that the first occurrence of the minimum value is modified when duplicates exist."""
        # nums = [1, 1, 1], k = 2, multiplier = 3
        # Op 1: min is 1 at idx 0 -> [3, 1, 1]
        # Op 2: min is 1 at idx 1 -> [3, 3, 1]
        nums = [1, 1, 1]
        k = 2
        multiplier = 3
        expected = [3, 3, 1]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_minimum_constraints(self):
        """Tests the absolute minimum constraints: single element array and zero operations."""
        nums = [5]
        k = 0
        multiplier = 10
        expected = [5]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_single_element_multiple_operations(self):
        """Tests a single element array undergoing multiple multiplication operations."""
        nums = [2]
        k = 3
        multiplier = 5
        # 2 * 5 * 5 * 5 = 250
        expected = [250]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_multiplier_is_one(self):
        """Tests that the array remains unchanged if the multiplier is 1, regardless of k."""
        nums = [4, 2, 7, 1]
        k = 100
        multiplier = 1
        expected = [4, 2, 7, 1]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_zero_operations(self):
        """Tests that the array remains unchanged when k is 0."""
        nums = [1, 2, 3, 4]
        k = 0
        multiplier = 2
        expected = [1, 2, 3, 4]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_negative_values_in_nums(self):
        """Tests proper behavior and ordering when negative integers are present in the array."""
        # Op 1: min is -5 at idx 1 -> [-2, -10, 0, 3]
        # Op 2: min is -10 at idx 1 -> [-2, -20, 0, 3]
        nums = [-2, -5, 0, 3]
        k = 2
        multiplier = 2
        expected = [-2, -20, 0, 3]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_negative_multiplier(self):
        """Tests alternate sorting behavior when the multiplier itself is negative."""
        # Op 1: min is 1 at idx 0 -> [-2, 4, 3]
        # Op 2: min is -2 at idx 0 -> [4, 4, 3]
        # Op 3: min is 3 at idx 2 -> [4, 4, -6]
        nums = [1, 4, 3]
        k = 3
        multiplier = -2
        expected = [4, 4, -6]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)


if __name__ == "__main__":
    unittest.main()