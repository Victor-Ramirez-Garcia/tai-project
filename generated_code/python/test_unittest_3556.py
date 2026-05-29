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

class TestGetFinalState(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        self.MOD = 10**9 + 7

    def test_example_1(self):
        # General case with mixed numbers
        nums = [2, 1, 3, 5, 6]
        k = 5
        multiplier = 2
        # Op 1: min is 1 at idx 1 -> [2, 2, 3, 5, 6]
        # Op 2: min is 2 at idx 0 -> [4, 2, 3, 5, 6]
        # Op 3: min is 2 at idx 1 -> [4, 4, 3, 5, 6]
        # Op 4: min is 3 at idx 2 -> [4, 4, 6, 5, 6]
        # Op 5: min is 4 at idx 0 -> [8, 4, 6, 5, 6]
        # Modulo applied to all elements: [8, 4, 6, 5, 6]
        expected = [8, 4, 6, 5, 6]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_example_2(self):
        # Case where multiplier is 1 (values shouldn't change)
        nums = [1, 2]
        k = 3
        multiplier = 1
        expected = [1, 2]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_duplicate_minimums_first_occurrence(self):
        # Multiple occurrences of the minimum value; the first one should be selected
        nums = [2, 2, 2]
        k = 2
        multiplier = 3
        # Op 1: min is 2 at idx 0 -> [6, 2, 2]
        # Op 2: min is 2 at idx 1 -> [6, 6, 2]
        expected = [6, 6, 2]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_single_element_array(self):
        # Minimum input size for array
        nums = [3]
        k = 4
        multiplier = 2
        # 3 * 2^4 = 48
        expected = [48]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_zero_operations(self):
        # Edge case where k is 0
        nums = [4, 8, 2]
        k = 0
        multiplier = 5
        expected = [4, 8, 2]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_modulo_overflow(self):
        # Ensure values exceeding 10^9 + 7 are correctly wrapped around
        nums = [1000000000]
        k = 2
        multiplier = 2
        # 1000000000 * 2 = 2000000000 -> 2000000000 % 1000000007 = 999999993
        # 999999993 * 2 = 1999999986 -> 1999999986 % 1000000007 = 999999979
        # (Alternatively, (10^9 * 4) % (10^9 + 7) = 4000000000 % 1000000007 = 3999999979 - 3000000021 = 999999979)
        expected = [(1000000000 * 4) % self.MOD]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

    def test_large_multiplier_and_k(self):
        # Stress test handling of big values and multiple operations
        nums = [5, 5]
        k = 3
        multiplier = 100000
        # Op 1: [500000, 5]
        # Op 2: [500000, 500000]
        # Op 3: [50000000000, 500000]
        # Modulo applied: [50000000000 % MOD, 500000 % MOD]
        # 50000000000 % 1000000007 = 50000000000 - 49 * 1000000007 = 50000000000 - 49000000343 = 999999657
        expected = [50000000000 % self.MOD, 500000 % self.MOD]
        self.assertEqual(self.sol.getFinalState(nums, k, multiplier), expected)

if __name__ == "__main__":
    unittest.main()