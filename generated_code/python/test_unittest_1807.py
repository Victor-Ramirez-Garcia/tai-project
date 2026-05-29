import os
import unittest
import importlib.util

# Dynamically load the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

class TestMinPartitions(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_small_digits(self):
        # Example 1 from problem statement
        # Explanation: 10 + 11 + 11 = 32 (Max digit is 3)
        self.assertEqual(self.sol.minPartitions("32"), 3)

    def test_example_2_medium_digits(self):
        # Example 2 from problem statement
        # Max digit is 8
        self.assertEqual(self.sol.minPartitions("82734"), 8)

    def test_example_3_large_string_max_digit_nine(self):
        # Example 3 from problem statement
        # Large string containing the digit 9
        self.assertEqual(self.sol.minPartitions("27346209830709182346"), 9)

    def test_edge_case_minimum_length_single_digit_one(self):
        # Constraint lower bound: n.length = 1, minimum positive value "1"
        self.assertEqual(self.sol.minPartitions("1"), 1)

    def test_edge_case_single_digit_maximum(self):
        # Single digit with the highest possible value
        self.assertEqual(self.sol.minPartitions("9"), 9)

    def test_edge_case_all_ones(self):
        # A number composed entirely of 1s requires exactly 1 deci-binary number
        self.assertEqual(self.sol.minPartitions("111111"), 1)

    def test_edge_case_all_zeros_except_first(self):
        # A number like 100000 requires 1 deci-binary number
        self.assertEqual(self.sol.minPartitions("100000"), 1)

    def test_edge_case_maximum_length_all_nines(self):
        # Constraint upper bound: n.length = 10^5, filled with the maximum digit '9'
        large_input = "9" * 100000
        self.assertEqual(self.sol.minPartitions(large_input), 9)

    def test_edge_case_maximum_length_all_ones(self):
        # Constraint upper bound: n.length = 10^5, filled with '1's
        large_input = "1" * 100000
        self.assertEqual(self.sol.minPartitions(large_input), 1)

    def test_edge_case_maximum_length_trailing_max_digit(self):
        # Constraint upper bound: n.length = 10^5, where only the last digit dictates the maximum
        large_input = ("1" * 99999) + "9"
        self.assertEqual(self.sol.minPartitions(large_input), 9)

if __name__ == "__main__":
    unittest.main()