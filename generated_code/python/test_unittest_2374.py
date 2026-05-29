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

class TestTotalSteps(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        # Example 1 from problem statement
        nums = [5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11]
        self.assertEqual(self.sol.totalSteps(nums), 3)

    def test_example_2(self):
        # Example 2 from problem statement (already non-decreasing)
        nums = [4, 5, 7, 7, 13]
        self.assertEqual(self.sol.totalSteps(nums), 0)

    def test_minimum_length_constraint(self):
        # Constraint lower bound: nums.length == 1
        nums = [42]
        self.assertEqual(self.sol.totalSteps(nums), 0)

    def test_strictly_decreasing(self):
        # Strictly decreasing array where elements eat each other cascadingly
        nums = [5, 4, 3, 2, 1]
        self.assertEqual(self.sol.totalSteps(nums), 1)

    def test_all_elements_equal(self):
        # Array with identical elements (already non-decreasing)
        nums = [7, 7, 7, 7, 7]
        self.assertEqual(self.sol.totalSteps(nums), 0)

    def test_strictly_increasing(self):
        # Strictly increasing array (already non-decreasing)
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.totalSteps(nums), 0)

    def test_v_shaped_array(self):
        # Elements decreasing then increasing
        nums = [10, 3, 4, 5, 6, 7]
        self.assertEqual(self.sol.totalSteps(nums), 5)

    def test_pyramid_shaped_array(self):
        # Elements increasing then decreasing
        nums = [1, 3, 5, 4, 2]
        self.assertEqual(self.sol.totalSteps(nums), 1)

    def test_large_steps_cascading(self):
        # Flat start, then large decreasing chain acting as a long eating pipeline
        nums = [10, 1, 2, 3, 4, 5, 6]
        self.assertEqual(self.sol.totalSteps(nums), 6)

    def test_multiple_independent_peaks(self):
        # Multiple segments operating independently in parallel
        nums = [10, 1, 2, 20, 1, 2, 3]
        self.assertEqual(self.sol.totalSteps(nums), 3)

if __name__ == "__main__":
    unittest.main()