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


class TestSmallestPalindrome(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_case(self):
        """Tests the example provided in the description: 'abba' with k=2."""
        self.assertEqual(self.sol.smallestPalindrome("abba", 2), "baab")

    def test_example_case_k1(self):
        """Tests the first lexicographical permutation for the example 'abba'."""
        self.assertEqual(self.sol.smallestPalindrome("abba", 1), "abba")

    def test_no_palindromic_permutation_possible(self):
        """Tests a string that cannot form any palindrome (e.g., more than one odd character count)."""
        self.assertEqual(self.sol.smallestPalindrome("abc", 1), "")

    def test_k_out_of_bounds_high(self):
        """Tests when k exceeds the total number of distinct palindromic permutations."""
        self.assertEqual(self.sol.smallestPalindrome("abba", 3), "")

    def test_single_character_string(self):
        """Tests the absolute minimum constraints: a single character string."""
        self.assertEqual(self.sol.smallestPalindrome("a", 1), "a")
        self.assertEqual(self.sol.smallestPalindrome("a", 2), "")

    def test_odd_length_palindrome_single_permutation(self):
        """Tests an odd length string with only one possible palindromic permutation."""
        self.assertEqual(self.sol.smallestPalindrome("racecar", 1), "acecrce")

    def test_multiple_identical_characters(self):
        """Tests handling of multiple identical characters which limits unique permutations."""
        # "aaaa" has only 1 distinct permutation: "aaaa"
        self.assertEqual(self.sol.smallestPalindrome("aaaa", 1), "aaaa")
        self.assertEqual(self.sol.smallestPalindrome("aaaa", 2), "")

    def test_larger_permutation_space(self):
        """Tests a case with a larger number of permutations to verify lexicographical ordering."""
        # Half string pool for "aabbcc": {'a': 1, 'b': 1, 'c': 1} -> 3! = 6 permutations
        # Order of halves: "abc", "acb", "bac", "bca", "cab", "cba"
        # Palindromes: "abccba", "acbbca", "baccab", "bcaacb", "cabbaac", "cbaabc"
        self.assertEqual(self.sol.smallestPalindrome("aabbcc", 1), "abccba")
        self.assertEqual(self.sol.smallestPalindrome("aabbcc", 3), "baccab")
        self.assertEqual(self.sol.smallestPalindrome("aabbcc", 6), "cbaabc")
        self.assertEqual(self.sol.smallestPalindrome("aabbcc", 7), "")


if __name__ == "__main__":
    unittest.main()