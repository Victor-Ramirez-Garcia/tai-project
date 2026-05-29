import os
import importlib.util
import unittest

# Dynamic loading of the solution module via environment variable
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise ImportError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestPivotArray(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        """Tests the first example from the problem statement."""
        nums = [9, 12, 5, 10, 14, 3, 10]
        pivot = 10
        expected = [9, 5, 3, 10, 10, 12, 14]
        self.assertEqual(self.sol.pivotArray(nums, pivot), expected)

    def test_example_2(self):
        """Tests the second example from the problem statement."""
        nums = [-3, 4, 3, 2]
        pivot = 2
        expected = [-3, 2, 4, 3]
        self.assertEqual(self.sol.pivotArray(nums, pivot), expected)

    def test_single_element_equal_to_pivot(self):
        """Tests the minimum constraints where the array has a single element equal to pivot."""
        nums = [5]
        pivot = 5
        expected = [5]
        self.assertEqual(self.sol.pivotArray(nums, pivot), expected)

    def test_single_element_less_than_pivot(self):
        """Tests a single element array where the element is less than the pivot."""
        nums = [1]
        pivot = 10
        expected = [1]
        self.assertEqual(self.sol.pivotArray(nums, pivot), expected)

    def test_single_element_greater_than_pivot(self):
        """Tests a single element array where the element is greater than the pivot."""
        nums = [20]
        pivot = 10
        expected = [20]
        self.assertEqual(self.sol.pivotArray(nums, pivot), expected)

    def test_all_elements_equal_to_pivot(self):
        """Tests an array where all elements are identical to the pivot."""
        nums = [7, 7, 7, 7]
        pivot = 7
        expected = [7, 7, 7, 7]
        self.assertEqual(self.sol.pivotArray(nums, pivot), expected)

    def test_all_elements_less_than_pivot(self):
        """Tests an array where all elements are strictly less than the pivot, maintaining relative order."""
        nums = [4, 1, 3, 2]
        pivot = 5
        expected = [4, 1, 3, 2]
        self.assertEqual(self.sol.pivotArray(nums, pivot), expected)

    def test_all_elements_greater_than_pivot(self):
        """Tests an array where all elements are strictly greater than the pivot, maintaining relative order."""
        nums = [8, 6, 9, 7]
        pivot = 3
        expected = [8, 6, 9, 7]
        self.assertEqual(self.sol.pivotArray(nums, pivot), expected)

    def test_negative_and_positive_mixed(self):
        """Tests mixed negative and positive numbers to ensure proper relative ordering across zero."""
        nums = [-10, 20, -5, 0, 15, -5]
        pivot = -5
        expected = [-10, -5, -5, 20, 0, 15]
        self.assertEqual(self.sol.pivotArray(nums, pivot), expected)


if __name__ == "__main__":
    unittest.main()