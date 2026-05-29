import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestMinimizeStringValue(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_aab_logic(self):
        """Validates a basic scenario where question marks can be optimally filled."""
        # If input is "???" we expect "abc" to minimize the cost (0+0+0) and be lexicographically smallest
        self.assertEqual(self.sol.minimizeStringValue("???"), "abc")

    def test_no_question_marks(self):
        """Validates that a string without any '?' remains unchanged."""
        self.assertEqual(self.sol.minimizeStringValue("abc"), "abc")
        self.assertEqual(self.sol.minimizeStringValue("aaaa"), "aaaa")

    def test_all_question_marks_large(self):
        """Validates a longer string of all '?' to ensure round-robin distribution for cost minimization."""
        # 27 question marks should use all 26 letters once, and the 27th should be 'a'
        # Sorted lexicographically, the injected characters 'a' through 'z' plus one 'a' 
        # will be placed in an optimal order.
        result = self.sol.minimizeStringValue("?" * 27)
        self.assertEqual(len(result), 27)
        self.assertEqual(result.count("a"), 2)
        self.assertEqual(result.count("b"), 1)

    def test_lexicographical_tie_breaking(self):
        """Validates that the lexicographically smallest string is chosen when costs are tied."""
        # "a?" -> filling with 'b' gives "ab" (cost: a=0, b=0). 
        # Filling with 'a' gives "aa" (cost: a=0, a=1). 
        # "ab" has a lower cost than "aa".
        self.assertEqual(self.sol.minimizeStringValue("a?"), "ab")

    def test_minimum_constraints(self):
        """Validates the boundary condition of the smallest possible input length."""
        self.assertEqual(self.sol.minimizeStringValue("?"), "a")
        self.assertEqual(self.sol.minimizeStringValue("z"), "z")

    def test_preexisting_frequency_impact(self):
        """Validates that '?' choices adapt to highly frequent pre-existing characters."""
        # 'a' is heavily blocked, so '?' should lean towards 'b', 'c', etc.
        self.assertEqual(self.sol.minimizeStringValue("aaaa?"), "aaaab")


if __name__ == "__main__":
    unittest.main()