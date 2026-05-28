import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("The environment variable 'TEST_SOLUTION_FILE' is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

class TestCanBeIncreasing(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Example Test Cases ---
    
    def test_example_1(self):
        # Explanation: Removing 10 results in [1, 2, 5, 7], which is strictly increasing.
        nums = [1, 2, 10, 5, 7]
        self.assertTrue(self.sol.canBeIncreasing(nums))

    def test_example_2(self):
        # Explanation: No single removal results in a strictly increasing array.
        nums = [2, 3, 1, 2]
        self.assertFalse(self.sol.canBeIncreasing(nums))

    def test_example_3(self):
        # Explanation: Removing any element results in [1, 1], which is not strictly increasing.
        nums = [1, 1, 1]
        self.assertFalse(self.sol.canBeIncreasing(nums))

    # --- Edge Cases & Constraints Test Cases ---

    def test_minimum_length_strictly_increasing(self):
        # Constraint: 2 <= nums.length. Already strictly increasing.
        nums = [1, 2]
        self.assertTrue(self.sol.canBeIncreasing(nums))

    def test_minimum_length_duplicate_elements(self):
        # Constraint: 2 <= nums.length. Removing one leaves a single element (always strictly increasing).
        nums = [5, 5]
        self.assertTrue(self.sol.canBeIncreasing(nums))

    def test_minimum_length_decreasing(self):
        # Constraint: 2 <= nums.length. Removing one leaves a single element.
        nums = [10, 2]
        self.assertTrue(self.sol.canBeIncreasing(nums))

    def test_already_strictly_increasing_large(self):
        # Array is already strictly increasing. No removal strictly necessary, but allowed.
        nums = [10, 20, 30, 40, 50, 60]
        self.assertTrue(self.sol.canBeIncreasing(nums))

    def test_remove_peak_at_start(self):
        # The anomaly is at the very beginning. Removing index 0 fixes it -> [2, 3, 4]
        nums = [10, 2, 3, 4]
        self.assertTrue(self.sol.canBeIncreasing(nums))

    def test_remove_valley_at_index_one(self):
        # The anomaly requires removing index 1 -> [2, 3, 4]
        nums = [2, 1, 3, 4]
        self.assertTrue(self.sol.canBeIncreasing(nums))

    def test_remove_peak_at_end(self):
        # The anomaly is at the very end. Removing the last element fixes it -> [1, 2, 3]
        nums = [1, 2, 3, 0]
        self.assertTrue(self.sol.canBeIncreasing(nums))

    def test_multiple_violating_peaks(self):
        # Requires more than one removal to fix.
        nums = [1, 5, 2, 8, 3]
        self.assertFalse(self.sol.canBeIncreasing(nums))

    def test_strictly_decreasing_large(self):
        # Completely decreasing array; removing one element won't make it strictly increasing.
        nums = [100, 90, 80, 70, 60]
        self.assertFalse(self.sol.canBeIncreasing(nums))

    def test_maximum_values_constraint(self):
        # Upper bounds of the constraints: nums[i] <= 1000
        nums = [999, 1000, 1000]
        self.assertTrue(self.sol.canBeIncreasing(nums))

if __name__ == "__main__":
    unittest.main()