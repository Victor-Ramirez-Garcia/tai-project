import unittest
from typing import List

# Assume the solution is in the same file or imported
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Implementation placeholder for testing purposes
        # Standard O(n) hash map approach
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return [seen[remaining], i]
            seen[num] = i
        return []


class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def assertHelper(self, result: List[int], expected: List[int]):
        """Helper method to handle the 'any order' return constraint."""
        self.assertEqual(sorted(result), sorted(expected))

    def test_example_1(self):
        """Standard case with small positive integers."""
        nums = [2, 7, 11, 15]
        target = 9
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertHelper(result, expected)

    def test_example_2(self):
        """Standard case where indices are not the first two elements."""
        nums = [3, 2, 4]
        target = 6
        expected = [1, 2]
        result = self.solution.twoSum(nums, target)
        self.assertHelper(result, expected)

    def test_example_3(self):
        """Case with duplicate elements making up the target."""
        nums = [3, 3]
        target = 6
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertHelper(result, expected)

    def test_minimum_length_constraint(self):
        """Edge case where the array has exactly the minimum allowed length (2)."""
        nums = [10, -5]
        target = 5
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertHelper(result, expected)

    def test_negative_numbers(self):
        """Case involving purely negative integers and a negative target."""
        nums = [-1, -2, -3, -4, -5]
        target = -8
        expected = [2, 4]
        result = self.solution.twoSum(nums, target)
        self.assertHelper(result, expected)

    def test_mixed_sign_numbers(self):
        """Case involving a mix of positive, negative, and zero values."""
        nums = [-10, 0, 34, -5, 12]
        target = 7
        expected = [3, 4]
        result = self.solution.twoSum(nums, target)
        self.assertHelper(result, expected)

    def test_large_values_constraint(self):
        """Edge case verifying constraints near the maximum/minimum boundaries (-10^9 to 10^9)."""
        nums = [-10**9, 10**9, 0]
        target = 0
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertHelper(result, expected)

    def test_large_target_and_elements(self):
        """Edge case with extreme values summing up to a high constraint target."""
        nums = [10**9 - 5, 5, 20, 30]
        target = 10**9
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertHelper(result, expected)

    def test_target_is_zero(self):
        """Case where the target sum is exactly zero, involving complementary numbers."""
        nums = [25, -25, 14, 88]
        target = 0
        expected = [0, 1]
        result = self.solution.twoSum(nums, target)
        self.assertHelper(result, expected)


if __name__ == "__main__":
    unittest.main()