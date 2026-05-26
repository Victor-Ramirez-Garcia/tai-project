import unittest
from solution_3_1 import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        # Example 1 from problem description
        s = "abcabcbb"
        expected = 3
        self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

    def test_example_2(self):
        # Example 2 from problem description
        s = "bbbbb"
        expected = 1
        self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

    def test_example_3(self):
        # Example 3 from problem description
        s = "pwwkew"
        expected = 3
        self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

    def test_empty_string(self):
        # Minimum constraint: length of s is 0
        s = ""
        expected = 0
        self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

    def test_single_character(self):
        # Smallest non-empty string boundary
        s = "a"
        expected = 1
        self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

    def test_all_unique_characters(self):
        # Entire string is the longest substring
        s = "abcdefg12345!@# "
        expected = 16
        self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

    def test_characters_with_spaces_and_symbols(self):
        # Constraint check: includes spaces, digits, and symbols
        s = "a b c!@#123a "
        # Longest unique substring: " b c!@#123a"
        expected = 10
        self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

    def test_repeated_pattern_at_end(self):
        # Repeating pattern shifting at the end of the string
        s = "dvdf"
        expected = 3  # "vdf"
        self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

    def test_large_input_constraint(self):
        # Maximum constraint scaling: up to 5 * 10^4 characters
        # Constructing a large string with a repeating pattern of length 10
        pattern = "abcdefghij"
        s = pattern * 5000  # Total length 50,000
        expected = 10
        self.assertEqual(self.sol.lengthOfLongestSubstring(s), expected)

if __name__ == '__main__':
    unittest.main()