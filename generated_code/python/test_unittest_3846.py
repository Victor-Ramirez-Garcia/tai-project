import os
import importlib.util
import unittest

# Dynamic loading of the solution module as required by the guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestMinOperationsToDivisibleSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_already_divisible(self):
        """Test where the initial sum is already divisible by k, requiring 0 operations."""
        nums = [2, 4, 6]
        k = 3  # Sum = 12, 12 % 3 == 0
        self.assertEqual(self.sol.minOperations(nums, k), 0)

    def test_example_requires_decrement(self):
        """Test a standard case where decrementing elements minimizes operations to reach divisibility."""
        nums = [1, 2, 3]
        k = 5  # Sum = 6, need to decrement by 1 to get 5
        self.assertEqual(self.sol.minOperations(nums, k), 1)

    def test_single_element_exact_multiple(self):
        """Test with a single element that is already a multiple of k."""
        nums = [10]
        k = 5
        self.assertEqual(self.sol.minOperations(nums, k), 0)

    def test_single_element_requires_decrement(self):
        """Test with a single element that needs to be decremented to become a multiple of k."""
        nums = [8]
        k = 5  # 8 % 5 = 3, so 3 decrements needed to reach 5
        self.assertEqual(self.sol.minOperations(nums, k), 3)

    def test_large_k_values(self):
        """Test where the sum of the array is smaller than k, requiring reduction to 0."""
        nums = [1, 2, 1]
        k = 10  # Sum = 4, must be reduced to 0
        self.assertEqual(self.sol.minOperations(nums, k), 4)

    def test_all_zeros(self):
        """Test where all elements are zero. Sum is 0, which is divisible by any k."""
        nums = [0, 0, 0]
        k = 7
        self.assertEqual(self.sol.minOperations(nums, k), 0)

    def test_large_array_elements(self):
        """Test with larger integer constraints to ensure proper modulo arithmetic handling."""
        nums = [100000, 200000, 300005]
        k = 100
        # Sum = 600005. 600005 % 100 = 5. Operations needed = 5.
        self.assertEqual(self.sol.minOperations(nums, k), 5)


if __name__ == "__main__":
    unittest.main()