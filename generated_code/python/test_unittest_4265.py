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


class TestLongestBalancedSubstring(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_case(self):
        # Covers the provided example: "100001" -> swap to "101000" -> balanced "1010" -> length 4
        self.assertEqual(self.sol.longestBalanced("100001"), 4)

    def test_minimum_constraints_all_zeros(self):
        # Minimum constraints or edge cases where no balanced substring can be formed
        self.assertEqual(self.sol.longestBalanced("0"), 0)
        self.assertEqual(self.sol.longestBalanced("0000"), 0)

    def test_minimum_constraints_all_ones(self):
        # Edge case with only '1's
        self.assertEqual(self.sol.longestBalanced("1"), 0)
        self.assertEqual(self.sol.longestBalanced("1111"), 0)

    def test_already_balanced_perfect_mix(self):
        # Already optimally balanced without needing a swap
        self.assertEqual(self.sol.longestBalanced("010101"), 6)
        self.assertEqual(self.sol.longestBalanced("000111"), 6)

    def test_single_swap_unites_disjoint_balanced_pieces(self):
        # Swapping allows two separate segments to merge into a larger balanced substring
        # "1100" (4) and "0011" (4) separated by a disruptive character
        # "11000011" -> swap index 3 ('0') with index 6 ('1') -> "11010001" -> "110100" (len 6)
        self.assertEqual(self.sol.longestBalanced("11000011"), 6)

    def test_swap_not_needed_but_allowed(self):
        # A case where a swap doesn't improve the maximum length
        self.assertEqual(self.sol.longestBalanced("10"), 2)

    def test_large_unbalanced_string(self):
        # Testing a longer string dominated by one character where a swap provides minimal help
        self.assertEqual(self.sol.longestBalanced("11111111011111"), 2)


if __name__ == "__main__":
    unittest.main()