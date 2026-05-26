import unittest
from solution_1_1 import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        """Standard case with small positive numbers (Example 1)."""
        nums = [2, 7, 11, 15]
        target = 9
        # The answer can be in any order, so we sort the result for assertion
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 1])

    def test_example_2(self):
        """Target is formed by the last two elements (Example 2)."""
        nums = [3, 2, 4]
        target = 6
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [1, 2])

    def test_example_3(self):
        """Array contains duplicate numbers forming the target (Example 3)."""
        nums = [3, 3]
        target = 6
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 1])

    def test_negative_numbers(self):
        """Verify handling of negative integers."""
        nums = [-3, 4, 3, 90]
        target = 0
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 2])

    def test_all_negative_numbers(self):
        """Verify handling when all numbers and target are negative."""
        nums = [-10, -1, -18, -7]
        target = -8
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [1, 3])

    def test_minimum_length_constraint(self):
        """Boundary test for the minimum array length constraint (length = 2)."""
        nums = [10, 20]
        target = 30
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 1])

    def test_large_values_constraint(self):
        """Boundary test for constraints approaching 10^9 and -10^9."""
        nums = [-1000000000, 1000000000]
        target = 0
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 1])

    def test_target_with_zero(self):
        """Verify handling when one of the components is zero."""
        nums = [0, 4, 3, 0]
        target = 0
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 3])

if __name__ == '__main__':
    unittest.main()