import unittest
from program_1_1 import Solution

class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        # Example 1: Standard case with positive numbers
        nums = [2, 7, 11, 15]
        target = 9
        # The result can be in any order, so we sort it for verification
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 1])

    def test_example_2(self):
        # Example 2: Target is the sum of the last two elements
        nums = [3, 2, 4]
        target = 6
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [1, 2])

    def test_example_3(self):
        # Example 3: Duplicate values in the array
        nums = [3, 3]
        target = 6
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 1])

    def test_minimum_length_constraint(self):
        # Constraint: 2 <= nums.length
        # Testing the absolute minimum length array
        nums = [10, -5]
        target = 5
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 1])

    def test_negative_numbers(self):
        # Constraint: -10^9 <= nums[i] <= 10^9
        # Testing negative values and a negative target
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [2, 4])

    def test_mixed_signs(self):
        # Testing a mix of positive and negative integers with a zero target
        nums = [-10, 5, 20, 10]
        target = 0
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 3])

    def test_large_value_constraints(self):
        # Constraint: Large values near upper and lower bounds (-10^9 to 10^9)
        nums = [-1000000000, 1000000000, 5000, 0]
        target = 0
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 1])

    def test_large_target_with_large_values(self):
        # Constraint: High target value requiring large integers
        nums = [999999999, 1, 1000000000]
        target = 1000000000
        result = sorted(self.sol.twoSum(nums, target))
        self.assertEqual(result, [0, 1])

if __name__ == '__main__':
    unittest.main()