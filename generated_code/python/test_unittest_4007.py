import os
import importlib.util
import unittest

# Dynamic loading of the Solution class as mandated by the guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("Environment variable 'TEST_SOLUTION_FILE' is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

class TestMaxTotalValue(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_case(self):
        """Tests the example scenario described in the problem statement."""
        # Based on the problem text: nums = [1, 3, 2], k = 2
        # Chosen subarrays: nums[0..1] -> [1, 3] (val: 2), nums[0..2] -> [1, 3, 2] (val: 2)
        # Total value: 2 + 2 = 4
        nums = [1, 3, 2]
        k = 2
        expected = 4
        self.assertEqual(self.sol.maxTotalValue(nums, k), expected)

    def test_single_element_subarrays(self):
        """Tests when subarrays have a length of 1, yielding a value of 0."""
        nums = [5, 5, 5]
        k = 3
        # Any single element subarray [5] has max(5) - min(5) = 0
        expected = 0
        self.assertEqual(self.sol.maxTotalValue(nums, k), expected)

    def test_all_elements_same(self):
        """Tests an array where all elements are identical; any subarray value will be 0."""
        nums = [10, 10, 10, 10]
        k = 5
        expected = 0
        self.assertEqual(self.sol.maxTotalValue(nums, k), expected)

    def test_minimum_constraints(self):
        """Tests the absolute minimum bounds for the input constraints."""
        nums = [1]
        k = 1
        # Only one possible subarray: nums[0..0] -> [1], value = 1 - 1 = 0
        expected = 0
        self.assertEqual(self.sol.maxTotalValue(nums, k), expected)

    def test_strictly_increasing_array(self):
        """Tests a strictly increasing array where max and min are strictly determined by boundaries."""
        nums = [1, 2, 4, 7]
        k = 3
        # Highly valuable subarrays:
        # nums[0..3] -> [1, 2, 4, 7] (val: 7 - 1 = 6)
        # nums[1..3] -> [2, 4, 7]    (val: 7 - 2 = 5)
        # nums[0..2] -> [1, 2, 4]    (val: 4 - 1 = 3)
        # Total: 6 + 5 + 3 = 14
        nums = [1, 2, 4, 7]
        k = 3
        expected = 14
        self.assertEqual(self.sol.maxTotalValue(nums, k), expected)

    def test_strictly_decreasing_array(self):
        """Tests a strictly decreasing array where max and min are reversed in terms of indices."""
        nums = [10, 7, 4, 1]
        k = 2
        # Best 2 subarrays:
        # nums[0..3] -> [10, 7, 4, 1] (val: 10 - 1 = 9)
        # nums[0..2] -> [10, 7, 4]    (val: 10 - 4 = 6) or nums[1..3] -> [7, 4, 1] (val: 7 - 1 = 6)
        # Total: 9 + 6 = 15
        nums = [10, 7, 4, 1]
        k = 2
        expected = 15
        self.assertEqual(self.sol.maxTotalValue(nums, k), expected)

    def test_negative_and_positive_mixed(self):
        """Tests an array containing both negative and positive integers."""
        nums = [-5, 10, -2, 6]
        k = 2
        # Best 2 subarrays:
        # nums[0..3] -> [-5, 10, -2, 6] (val: 10 - (-5) = 15)
        # nums[0..1] -> [-5, 10]         (val: 10 - (-5) = 15)
        # Total: 15 + 15 = 30
        nums = [-5, 10, -2, 6]
        k = 2
        expected = 30
        self.assertEqual(self.sol.maxTotalValue(nums, k), expected)

    def test_large_k_choosing_all_possible_subarrays(self):
        """Tests when k is equal to the total number of non-empty subarrays possible."""
        nums = [1, 5, 2]
        # Total non-empty subarrays = (3 * 4) // 2 = 6
        # Subarrays and values:
        # [1] -> 0, [5] -> 0, [2] -> 0
        # [1, 5] -> 4, [5, 2] -> 3
        # [1, 5, 2] -> 4
        # Total sum of all values = 0 + 0 + 0 + 4 + 3 + 4 = 11
        k = 6
        expected = 11
        self.assertEqual(self.sol.maxTotalValue(nums, k), expected)

if __name__ == "__main__":
    unittest.main()