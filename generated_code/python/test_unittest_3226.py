import os
import importlib.util
import unittest

# Dynamic loading of the Solution class from environment variable
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestNumberGame(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_one(self):
        """Tests the first example provided in the problem statement."""
        nums = [5, 4, 2, 3]
        expected = [3, 2, 5, 4]
        self.assertEqual(self.sol.numberGame(nums), expected)

    def test_example_two(self):
        """Tests the second example provided in the problem statement (minimum length array)."""
        nums = [2, 5]
        expected = [5, 2]
        self.assertEqual(self.sol.numberGame(nums), expected)

    def test_already_sorted_input(self):
        """Tests an input array that is already sorted in ascending order."""
        nums = [1, 2, 3, 4, 5, 6]
        expected = [2, 1, 4, 3, 6, 5]
        self.assertEqual(self.sol.numberGame(nums), expected)

    def test_reverse_sorted_input(self):
        """Tests an input array that is sorted in descending order."""
        nums = [6, 5, 4, 3, 2, 1]
        expected = [2, 1, 4, 3, 6, 5]
        self.assertEqual(self.sol.numberGame(nums), expected)

    def test_duplicate_elements(self):
        """Tests an input array containing identical duplicate elements."""
        nums = [5, 5, 5, 5]
        expected = [5, 5, 5, 5]
        self.assertEqual(self.sol.numberGame(nums), expected)

    def test_mixed_duplicates(self):
        """Tests an input array where some elements are duplicated."""
        nums = [2, 2, 1, 1, 4, 3]
        # Sorted: [1, 1, 2, 2, 3, 4] -> Swapped pairs: [1, 1, 2, 2, 4, 3]
        expected = [1, 1, 2, 2, 4, 3]
        self.assertEqual(self.sol.numberGame(nums), expected)

    def test_negative_elements(self):
        """Tests correctness when the array contains negative numbers."""
        nums = [-3, -1, -4, -2]
        # Sorted: [-4, -3, -2, -1] -> Swapped pairs: [-3, -4, -1, -2]
        expected = [-3, -4, -1, -2]
        self.assertEqual(self.sol.numberGame(nums), expected)


if __name__ == "__main__":
    unittest.main()