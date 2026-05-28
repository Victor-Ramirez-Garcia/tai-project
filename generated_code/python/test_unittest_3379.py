import os
import importlib.util
import unittest

# Dynamic loading of the Solution class as mandated by guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("Environment variable 'TEST_SOLUTION_FILE' is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestScoreOfString(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1_hello(self):
        """
        Tests Example 1 from standard problem statement:
        s = "hello" -> |104-101| + |101-108| + |108-108| + |108-111| = 3 + 7 + 0 + 3 = 13
        """
        self.assertEqual(self.sol.scoreOfString("hello"), 13)

    def test_example_2_zaz(self):
        """
        Tests Example 2 from standard problem statement:
        s = "zaz" -> |122-97| + |97-122| = 25 + 25 = 50
        """
        self.assertEqual(self.sol.scoreOfString("zaz"), 50)

    def test_minimum_length_constraints(self):
        """
        Tests the absolute minimum length constraint (s.length == 2).
        """
        # Identical characters
        self.assertEqual(self.sol.scoreOfString("aa"), 0)
        # Maximum difference for lowercase English letters ('a' = 97, 'z' = 122)
        self.assertEqual(self.sol.scoreOfString("az"), 25)
        self.assertEqual(self.sol.scoreOfString("za"), 25)

    def test_identical_characters_long_string(self):
        """
        Tests a longer string consisting of all identical characters.
        The absolute differences should all be 0, resulting in a score of 0.
        """
        self.assertEqual(self.sol.scoreOfString("nnnnnnnnnnnnnnnnnnnn"), 0)

    def test_strictly_increasing_sequence(self):
        """
        Tests a strictly increasing sequence of characters.
        """
        # "abcdef" -> 1 + 1 + 1 + 1 + 1 = 5
        self.assertEqual(self.sol.scoreOfString("abcdef"), 5)

    def test_strictly_decreasing_sequence(self):
        """
        Tests a strictly decreasing sequence of characters.
        """
        # "fedcba" -> 1 + 1 + 1 + 1 + 1 = 5
        self.assertEqual(self.sol.scoreOfString("fedcba"), 5)

    def test_maximum_length_constraints(self):
        """
        Tests the maximum length constraint boundary (s.length == 100).
        """
        # Alternating max-diff characters to maximize potential score accumulation
        # 99 adjacent pairs, each with a difference of 25. 99 * 25 = 2475
        s_max_alternating = "az" * 50
        self.assertEqual(self.sol.scoreOfString(s_max_alternating), 2475)

        # 100 characters of the same element to check the lower bound at max length
        s_max_identical = "x" * 100
        self.assertEqual(self.sol.scoreOfString(s_max_identical), 0)


if __name__ == "__main__":
    unittest.main()