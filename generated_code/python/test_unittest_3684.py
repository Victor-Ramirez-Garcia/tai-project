import os
import importlib.util
import unittest

# Dynamic loading of the solution module as required by guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestHasMatch(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1_basic_match(self):
        # General scenario where wildcard matches a middle segment
        self.assertTrue(self.sol.hasMatch("leetcode", "ee*e"))

    def test_example_2_no_match(self):
        # Scenario where the prefix and suffix exist but overlap incorrectly or cannot form a valid substring
        self.assertFalse(self.sol.hasMatch("car", "c*v"))

    def test_example_3_empty_wildcard_match(self):
        # Scenario where '*' matches zero characters (exact concatenation of prefix and suffix)
        self.assertTrue(self.sol.hasMatch("luck", "u*ck"))

    def test_minimum_constraints(self):
        # Smallest possible inputs: lengths of s and p are 1, meaning p is just '*'
        self.assertTrue(self.sol.hasMatch("a", "*"))

    def test_wildcard_at_start(self):
        # Prefix is empty, matching from the beginning of the string or anywhere
        self.assertTrue(self.sol.hasMatch("abcdef", "*ef"))
        self.assertTrue(self.sol.hasMatch("abcdef", "*cd"))
        self.assertFalse(self.sol.hasMatch("abcdef", "*xyz"))

    def test_wildcard_at_end(self):
        # Suffix is empty, matching up to the end of the string or anywhere
        self.assertTrue(self.sol.hasMatch("abcdef", "ab*"))
        self.assertTrue(self.sol.hasMatch("abcdef", "cd*"))
        self.assertFalse(self.sol.hasMatch("abcdef", "xyz*"))

    def test_exact_match_full_string(self):
        # Pattern spans the entire string with explicit boundaries
        self.assertTrue(self.sol.hasMatch("leetcode", "leet*code"))

    def test_overlapping_potential_matches(self):
        # Ensure the prefix match does not consume characters needed by the suffix match if they must be distinct
        # p = "a*a" requires finding an 'a' followed by another 'a' later (or adjacent)
        self.assertTrue(self.sol.hasMatch("a", "a*"))
        self.assertTrue(self.sol.hasMatch("aa", "a*a"))
        self.assertFalse(self.sol.hasMatch("a", "a*a"))

    def test_maximum_constraints_match(self):
        # Maximum lengths (50 characters) where a match exists
        s = "a" * 50
        p = "a" * 24 + "*" + "a" * 25
        self.assertTrue(self.sol.hasMatch(s, p))

    def test_maximum_constraints_no_match(self):
        # Maximum lengths (50 characters) where a match fails at the very end
        s = "a" * 49 + "b"
        p = "a" * 25 + "*" + "c"
        self.assertFalse(self.sol.hasMatch(s, p))


if __name__ == "__main__":
    unittest.main()