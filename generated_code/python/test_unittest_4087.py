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

class TestMaxDistinctSubstrings(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_abab(self):
        # Example from problem statement: "abab" -> "a", "bab" (starts with 'a' and 'b')
        self.assertEqual(self.sol.maxDistinct("abab"), 2)

    def test_single_character(self):
        # Minimum input size edge case
        self.assertEqual(self.sol.maxDistinct("a"), 1)

    def test_all_identical_characters(self):
        # Case where all characters are the same; can only form 1 valid substring
        self.assertEqual(self.sol.maxDistinct("aaaaa"), 1)

    def test_all_distinct_characters(self):
        # Every character is unique; can be split into individual characters
        self.assertEqual(self.sol.maxDistinct("abcdef"), 6)

    def test_reappearing_characters_ordered(self):
        # "abcba" -> can split into "a", "b", "cba" (starts with 'a', 'b', 'c')
        self.assertEqual(self.sol.maxDistinct("abcba"), 3)

    def test_long_string_limited_alphabet(self):
        # String with only two characters alternating
        self.assertEqual(self.sol.maxDistinct("abababababab"), 2)

    def test_max_possible_distinct(self):
        # Alphabet limit constraint: maximum 26 unique starting characters
        full_alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual(self.sol.maxDistinct(full_alphabet), 26)
        self.assertEqual(self.sol.maxDistinct(full_alphabet + full_alphabet), 26)

if __name__ == "__main__":
    unittest.main()