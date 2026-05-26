import unittest

# Assuming the solution class is defined here or imported
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Placeholder implementation for testing structure integration
        # In practice, this would contain the actual sliding window algorithm
        char_map = {}
        max_len = 0
        start = 0
        for end in range(len(s)):
            if s[end] in char_map and char_map[s[end]] >= start:
                start = char_map[s[end]] + 1
            char_map[s[end]] = end
            max_len = max(max_len, end - start + 1)
        return max_len

class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Example Test Cases ---
    def test_example_1_mixed_repeats(self):
        """Tests standard mixed repeating string 'abcabcbb' -> expected 3 ('abc')"""
        self.assertEqual(self.sol.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2_all_identical(self):
        """Tests string with all identical characters 'bbbbb' -> expected 1 ('b')"""
        self.assertEqual(self.sol.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_3_subsequence_trap(self):
        """Tests string with duplicate prefix 'pwwkew' -> expected 3 ('wke')"""
        self.assertEqual(self.sol.lengthOfLongestSubstring("pwwkew"), 3)

    # --- Edge Cases & Constraints ---
    def test_constraint_minimum_empty_string(self):
        """Tests the lower bound constraint: empty string s.length == 0 -> expected 0"""
        self.assertEqual(self.sol.lengthOfLongestSubstring(""), 0)

    def test_constraint_single_character(self):
        """Tests a string containing only one character -> expected 1"""
        self.assertEqual(self.sol.lengthOfLongestSubstring("a"), 1)

    def test_all_unique_characters(self):
        """Tests a string with all completely unique characters -> expected full length"""
        self.assertEqual(self.sol.lengthOfLongestSubstring("abcdefg"), 7)

    def test_spaces_and_symbols(self):
        """Tests character set constraints involving spaces, digits, and symbols"""
        self.assertEqual(self.sol.lengthOfLongestSubstring("a 1!a 1!"), 4)  # "a 1!" is unique

    def test_case_sensitivity(self):
        """Tests that upper and lower case letters are treated as distinct"""
        self.assertEqual(self.sol.lengthOfLongestSubstring("abABabc"), 4)  # "abAB" or "bABa" etc.

    def test_large_input_performance(self):
        """Tests upper bound constraint characteristics with a large repetitive sequence"""
        large_input = "abcdefghijklmnopqrstuvwxyz" * 1000
        self.assertEqual(self.sol.lengthOfLongestSubstring(large_input), 26)

if __name__ == "__main__":
    unittest.main()