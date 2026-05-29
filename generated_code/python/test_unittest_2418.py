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

class TestMinSumSquareDiff(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        """Verifies Example 1 from the problem description where k1=0 and k2=0."""
        nums1 = [1, 2, 3, 4]
        nums2 = [2, 10, 20, 19]
        k1 = 0
        k2 = 0
        expected = 579
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), expected)

    def test_example_2(self):
        """Verifies Example 2 from the problem description with small adjustments allowed."""
        nums1 = [1, 4, 10, 12]
        nums2 = [5, 8, 6, 9]
        k1 = 1
        k2 = 1
        expected = 43
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), expected)

    def test_minimum_constraints(self):
        """Tests the absolute minimum constraints: single element arrays and zero modifications."""
        nums1 = [5]
        nums2 = [5]
        k1 = 0
        k2 = 0
        expected = 0
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), expected)

    def test_k_exceeds_total_difference(self):
        """Tests the scenario where the total budget k1 + k2 is greater than or equal to the total difference sum."""
        nums1 = [1, 2, 3]
        nums2 = [4, 5, 6]  # absolute differences: 3, 3, 3 (Total = 9)
        k1 = 5
        k2 = 5             # Total budget = 10
        expected = 0       # All differences can be reduced to 0
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), expected)

    def test_exact_k_to_zero_difference(self):
        """Tests the scenario where total budget k1 + k2 perfectly reduces all differences to zero."""
        nums1 = [10, 20]
        nums2 = [15, 25]  # absolute differences: 5, 5 (Total = 10)
        k1 = 4
        k2 = 6            # Total budget = 10
        expected = 0
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), expected)

    def test_large_k_distribution(self):
        """Tests that the reduction budget is distributed optimally to minimize the maximum differences first."""
        nums1 = [1, 10]
        nums2 = [1, 1]   # absolute differences: 0, 9
        k1 = 2
        k2 = 1           # Total budget = 3
        # 9 should be reduced by 3 to become 6. Result: 0^2 + 6^2 = 36
        expected = 36
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), expected)

    def test_identical_arrays(self):
        """Tests identical arrays where initial differences are already zero, with non-zero k."""
        nums1 = [1, 2, 3, 4, 5]
        nums2 = [1, 2, 3, 4, 5]
        k1 = 100
        k2 = 100
        expected = 0
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), expected)

    def test_large_inputs_and_high_k(self):
        """Tests larger values for k within the constraint limit up to 10^9."""
        nums1 = [100000, 0]
        nums2 = [0, 100000] # absolute differences: 100000, 100000
        k1 = 50000
        k2 = 50000          # Total budget = 100000
        # Differences reduce uniformly. Both become 50000.
        # (50000)^2 + (50000)^2 = 2500000000 + 2500000000 = 5000000000
        expected = 5000000000
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), expected)

    def test_unequal_distribution_of_remainder(self):
        """Tests when the reduction doesn't divide evenly among the largest identical differences."""
        nums1 = [1, 1, 1]
        nums2 = [5, 5, 5] # absolute differences: 4, 4, 4
        k1 = 2
        k2 = 0            # Total budget = 2
        # Two of the 4s become 3. Remaining differences: 3, 3, 4
        # 3^2 + 3^2 + 4^2 = 9 + 9 + 16 = 34
        expected = 34
        self.assertEqual(self.sol.minSumSquareDiff(nums1, nums2, k1, k2), expected)

if __name__ == "__main__":
    unittest.main()