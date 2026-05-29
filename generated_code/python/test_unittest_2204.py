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

class TestMaxSubsequence(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        nums = [2, 1, 3, 3]
        k = 2
        # Expected maximum sum is 6, elements must be [3, 3]
        expected = [3, 3]
        self.assertEqual(self.sol.maxSubsequence(nums, k), expected)

    def test_example_2(self):
        nums = [-1, -2, 3, 4]
        k = 3
        # Expected maximum sum is 6, maintaining relative order gives [-1, 3, 4]
        expected = [-1, 3, 4]
        self.assertEqual(self.sol.maxSubsequence(nums, k), expected)

    def test_example_3(self):
        nums = [3, 4, 3, 3]
        k = 2
        # Multiple valid answers exist ([3, 4] or [4, 3]). 
        # We accept either valid subsequence that matches the maximum sum elements and order.
        result = self.sol.maxSubsequence(nums, k)
        self.assertIn(result, [[3, 4], [4, 3]])

    def test_min_constraints(self):
        # Minimum input size: nums.length == 1, k == 1
        nums = [42]
        k = 1
        expected = [42]
        self.assertEqual(self.sol.maxSubsequence(nums, k), expected)

    def test_k_equals_length(self):
        # When k equals the length of nums, the entire array should be returned
        nums = [1, -5, 2, 10, -3]
        k = 5
        expected = [1, -5, 2, 10, -3]
        self.assertEqual(self.sol.maxSubsequence(nums, k), expected)

    def test_all_negative_numbers(self):
        nums = [-10, -1, -3, -20, -2]
        k = 3
        # Largest sum comes from picking -1, -3, -2. Relative order is [-1, -3, -2]
        expected = [-1, -3, -2]
        self.assertEqual(self.sol.maxSubsequence(nums, k), expected)

    def test_duplicate_largest_elements_order_preservation(self):
        # Tests that among duplicate maximum values, the correct relative index order is maintained
        nums = [10, 2, 10, 3, 10]
        k = 3
        expected = [10, 10, 10]
        self.assertEqual(self.sol.maxSubsequence(nums, k), expected)

    def test_large_constraints_bounds(self):
        # Maximum and minimum constraint values within array
        nums = [-100000, 100000, 0, -500, 100000]
        k = 2
        expected = [100000, 100000]
        self.assertEqual(self.sol.maxSubsequence(nums, k), expected)