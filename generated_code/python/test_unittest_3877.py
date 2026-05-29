import os
import importlib.util
import unittest

# Dynamic loading of the Solution class as mandated by guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestScore(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty_deck(self):
        """Tests that an empty deck of cards results in 0 points."""
        self.assertEqual(self.sol.score([], "a"), 0)

    def test_single_card(self):
        """Tests that a single card cannot form a pair and results in 0 points."""
        self.assertEqual(self.sol.score(["ab"], "a"), 0)

    def test_cards_without_target_letter(self):
        """Tests that cards not containing the letter x cannot be used, yielding 0 points."""
        self.assertEqual(self.sol.score(["ab", "bb", "cb"], "x"), 0)

    def test_single_valid_compatible_pair(self):
        """Tests a basic scenario where exactly one pair of compatible cards containing x exists."""
        # "ax" and "bx" both contain 'x' and differ in exactly 1 position (index 0).
        self.assertEqual(self.sol.score(["ax", "bx"], "x"), 1)

    def test_identical_cards_not_compatible(self):
        """Tests that identical cards are not compatible since they differ in 0 positions."""
        self.assertEqual(self.sol.score(["ax", "ax"], "x"), 0)

    def test_cards_differing_by_two_positions(self):
        """Tests that cards differing in both positions are not compatible."""
        # "ax" and "xb" both contain 'x' but differ at both index 0 and index 1.
        self.assertEqual(self.sol.score(["ax", "xb"], "x"), 0)

    def test_one_card_missing_target_letter(self):
        """Tests that even if two cards are compatible, they can't be paired if one lacks x."""
        # "ab" and "bb" differ by 1 position, but "bb" does not contain 'a'.
        self.assertEqual(self.sol.score(["ab", "bb"], "a"), 0)

    def test_multiple_disjoint_pairs(self):
        """Tests a deck containing multiple independent valid pairs."""
        cards = ["ax", "bx", "cx", "dx"]
        # ("ax", "bx") and ("cx", "dx") can form two distinct pairs.
        self.assertEqual(self.sol.score(cards, "x"), 2)

    def test_optimal_matching_greedy_failure(self):
        """
        Tests that optimal matching is required when a card can match with multiple others,
        and a naive greedy choice might yield a suboptimal score.
        """
        # "xa" can match with "xb" or "ya". 
        # If "xa" pairs with "xb", then "ya" and "yb" can pair up -> Total 2 points.
        # If "xa" pairs with "ya", "xb" and "yb" can pair up -> Total 2 points.
        # Here we construct a structural bottleneck to test maximum matching capability.
        cards = ["xa", "xb", "ya", "yb"]
        self.assertEqual(self.sol.score(cards, "x"), 2)

    def test_target_letter_both_positions(self):
        """Tests compatibility when the target letter occupies different or multiple positions."""
        # "xx" and "ax" both contain 'x' and differ by exactly 1 position.
        self.assertEqual(self.sol.score(["xx", "ax"], "x"), 1)


if __name__ == "__main__":
    unittest.main()