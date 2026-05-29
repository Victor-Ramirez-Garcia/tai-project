import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per the guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

class TestMaxProductAlternatingSum(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_basic_valid_subsequence(self):
        # General case where a valid subsequence exists and product is within limits
        # E.g., nums=[4, 2, 5], k=7 (4 - 2 + 5 = 7), limit=50 -> product = 4 * 2 * 5 = 40
        nums = [4, 2, 5]
        k = 7
        limit = 50
        self.assertEqual(self.sol.maxProduct(nums, k, limit), 40)

    def test_example_2_no_valid_alternating_sum(self):
        # Case where no combination of elements can achieve the target alternating sum k
        nums = [1, 2, 3]
        k = 10
        limit = 100
        self.assertEqual(self.sol.maxProduct(nums, k, limit), -1)

    def test_example_3_product_exceeds_limit(self):
        # Case where a subsequence satisfies k but its product exceeds the limit
        nums = [10, 2, 10]
        k = 18 # 10 - 2 + 10 = 18
        limit = 50 # Product is 200, which is > 50
        self.assertEqual(self.sol.maxProduct(nums, k, limit), -1)

    def test_edge_single_element_matching_k(self):
        # Minimum input size: single element that matches k and is within limit
        nums = [5]
        k = 5
        limit = 10
        self.assertEqual(self.sol.maxProduct(nums, k, limit), 5)

    def test_edge_single_element_not_matching_k(self):
        # Minimum input size: single element that does not match k
        nums = [5]
        k = 3
        limit = 10
        self.assertEqual(self.sol.maxProduct(nums, k, limit), -1)

    def test_edge_single_element_exceeding_limit(self):
        # Single element matches k but exceeds the limit
        nums = [15]
        k = 15
        limit = 10
        self.assertEqual(self.sol.maxProduct(nums, k, limit), -1)

    def test_multiple_subsequences_pick_max_product(self):
        # Multiple subsequences satisfy k, the one maximizing product within limit must be chosen
        # Subsequence A: [5, 1, 4] -> 5 - 1 + 4 = 8, product = 20
        # Subsequence B: [9, 1, 0] -> 9 - 1 + 0 = 8, product = 0
        # Subsequence C: [8] -> 8 = 8, product = 8
        nums = [5, 9, 1, 4, 0, 8]
        k = 8
        limit = 25
        self.assertEqual(self.sol.maxProduct(nums, k, limit), 20)

    def test_zero_elements_handling(self):
        # Subsequence includes 0, which zeroes out the product but might be the only way to match k
        nums = [5, 0, 2]
        k = 7 # 5 - 0 + 2 = 7
        limit = 10
        self.assertEqual(self.sol.maxProduct(nums, k, limit), 0)

    def test_negative_target_k(self):
        # Target k is negative, requiring a larger sum at odd indices
        nums = [2, 8, 3]
        k = -3 # 2 - 8 + 3 = -3
        limit = 50
        self.assertEqual(self.sol.maxProduct(nums, k, limit), 48)

if __name__ == "__main__":
    unittest.main()