import unittest
from program_3_1 import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    # --- Example Test Cases ---
    def test_example_1(self):
        """Standard case with mixed repeating characters: 'abcabcbb' -> 3 ('abc')"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcabcbb"), 3)

    def test_example_2(self):
        """Case with all identical characters: 'bbbbb' -> 1 ('b')"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("bbbbb"), 1)

    def test_example_3(self):
        """Case with duplicate characters at the beginning and middle: 'pwwkew' -> 3 ('wke')"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("pwwkew"), 3)

    # --- Edge Cases & Constraints ---
    def test_empty_string(self):
        """Constraint minimum: 0 length string -> 0"""
        self.assertEqual(self.solution.lengthOfLongestSubstring(""), 0)

    def test_single_character(self):
        """Minimal non-empty string -> 1"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("a"), 1)

    def test_all_unique_characters(self):
        """String with absolutely no duplicate characters -> full length"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdefg"), 7)

    def test_spaces_and_symbols(self):
        """Constraint check: Ensures spaces, digits, and symbols are handled properly"""
        # "a b!" has unique characters: 'a', ' ', 'b', '!' -> length 4
        self.assertEqual(self.solution.lengthOfLongestSubstring("a b!"), 4)
        # "   " has 3 spaces -> length 1
        self.assertEqual(self.solution.lengthOfLongestSubstring("   "), 1)

    def test_digits_and_mixed_case(self):
        """Case sensitivity check and numeric support: 'aA12a' -> 4 ('aA12')"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("aA12a"), 4)

    def test_longest_at_the_end(self):
        """The longest unique substring is located at the very end of the string"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("aaaaabcdef"), 6)

    def test_longest_at_the_beginning(self):
        """The longest unique substring is located at the very beginning of the string"""
        self.assertEqual(self.solution.lengthOfLongestSubstring("abcdefaaaaa"), 6)

    def test_large_input_constraint(self):
        """Performance & correctness check with a larger input near maximum constraints"""
        # Periodic repeating pattern ensures the sliding window resets frequently
        large_input = "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*() " * 1000
        # The unique alphabet size here is 47 characters
        self.assertEqual(self.solution.lengthOfLongestSubstring(large_input), 47)

if __name__ == "__main__":
    unittest.main()