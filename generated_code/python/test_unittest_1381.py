import importlib.util
import os
import unittest

# Dynamic loading of the Solution class as mandated by guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError(
        "Environment variable 'TEST_SOLUTION_FILE' is not set."
    )

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestMaxScoreWords(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        words = ["dog", "cat", "dad", "good"]
        letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
        score = [
            1,
            0,
            9,
            5,
            0,
            0,
            3,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            2,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
        expected = 23
        self.assertEqual(
            self.sol.maxScoreWords(words, letters, score), expected
        )

    def test_example_2(self):
        words = ["xxxz", "ax", "bx", "cx"]
        letters = ["z", "a", "b", "c", "x", "x", "x"]
        score = [
            4,
            4,
            4,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            5,
            0,
            10,
        ]
        expected = 27
        self.assertEqual(
            self.sol.maxScoreWords(words, letters, score), expected
        )

    def test_example_3(self):
        words = ["leetcode"]
        letters = ["l", "e", "t", "c", "o", "d"]
        score = [
            0,
            0,
            1,
            1,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            1,
            0,
            0,
            0,
            0,
            0,
            0,
        ]
        expected = 0
        self.assertEqual(
            self.sol.maxScoreWords(words, letters, score), expected
        )

    def test_minimum_constraints(self):
        # Single single-letter word, single valid letter, minimum score tracking
        words = ["a"]
        letters = ["a"]
        score = [5] + [0] * 25
        expected = 5
        self.assertEqual(
            self.sol.maxScoreWords(words, letters, score), expected
        )

    def test_insufficient_letters(self):
        # The word cannot be formed because there are not enough letters
        words = ["apple"]
        letters = ["a", "p", "l", "e"]  # Missing one 'p'
        score = [1] * 26
        expected = 0
        self.assertEqual(
            self.sol.maxScoreWords(words, letters, score), expected
        )

    def test_all_words_can_be_formed(self):
        # Letters are sufficient to form every single word combined
        words = ["ab", "cd", "ef"]
        letters = ["a", "b", "c", "d", "e", "f", "z"]
        score = [1] * 26
        expected = 6  # 2 + 2 + 2
        self.assertEqual(
            self.sol.maxScoreWords(words, letters, score), expected
        )

    def test_zero_scores(self):
        # Valid subset of words can be formed, but all character scores are 0
        words = ["abc", "def"]
        letters = ["a", "b", "c", "d", "e", "f"]
        score = [0] * 26
        expected = 0
        self.assertEqual(
            self.sol.maxScoreWords(words, letters, score), expected
        )

    def test_maximum_words_constraint(self):
        # Maximum allowed number of words (14) with short lengths
        words = ["a"] * 14
        letters = ["a"] * 10
        score = [2] + [0] * 25
        expected = 20  # Can only form 10 "a" words because of letter pool limit
        self.assertEqual(
            self.sol.maxScoreWords(words, letters, score), expected
        )

    def test_no_words_can_be_formed(self):
        # None of the words can be formed by the letter pool
        words = ["xyz", "uvw"]
        letters = ["a", "b", "c", "d"]
        score = [10] * 26
        expected = 0
        self.assertEqual(
            self.sol.maxScoreWords(words, letters, score), expected
        )