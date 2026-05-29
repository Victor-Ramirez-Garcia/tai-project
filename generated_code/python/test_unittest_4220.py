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

class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_dog(self):
        # Description Example: "dog" -> sort "og" to "go" -> "dgo" (1 operation)
        self.assertEqual(self.sol.minOperations("dog"), 1)

    def test_already_sorted_short(self):
        # String is already sorted, requires 0 operations
        self.assertEqual(self.sol.minOperations("abc"), 0)

    def test_already_sorted_all_same(self):
        # String with identical characters is already sorted
        self.assertEqual(self.sol.minOperations("aaaa"), 0)

    def test_single_character(self):
        # Constraints edge case: minimum length string (already sorted)
        self.assertEqual(self.sol.minOperations("a"), 0)

    def test_two_characters_unsorted(self):
        # Length 2 unsorted: cannot sort the entire string in 1 operation.
        # Any proper substring is length 1 (already sorted). Sorting it changes nothing.
        # Thus, it's impossible to sort the whole string.
        self.assertEqual(self.sol.minOperations("ba"), -1)

    def test_three_characters_reverse_sorted(self):
        # "cba" -> sort "cb" to "bc" -> "bca" -> sort "ca" to "ac" -> "bac" (not fully sorted yet)
        # Alternatively, "cba" -> sort "ba" to "ab" -> "cab".
        # To fix "cab", we can sort "ca" to "ac" -> "acb", then "cb" to "bc" -> "abc".
        # Since we cannot select the entire string, we look at the first and last characters.
        # If the minimum character is at the end or maximum at the start, it takes more steps or might be impossible.
        # For "cba": min is 'a' at index 2, max is 'c' at index 0.
        # Op 1: sort s[0:2] "cb" -> "bc" -> s = "bca"
        # Op 2: sort s[1:3] "ca" -> "ac" -> s = "bac"
        # Op 3: sort s[0:2] "ba" -> "ab" -> s = "abc"
        self.assertEqual(self.sol.minOperations("cba"), 3)

    def test_min_char_at_end_preventing_one_op(self):
        # "bcda" -> The smallest character 'a' is at the very end, and 'b' is at the start.
        # We cannot sort the whole string. Sorting "bcd" gives "bcda".
        # Sorting "cda" gives "bacd". Then sorting "ba" gives "abcd". (2 operations)
        self.assertEqual(self.sol.minOperations("bcda"), 2)

    def test_max_char_at_start_preventing_one_op(self):
        # "dabc" -> The largest character 'd' is at the start. 
        # Sorting "abc" changes nothing. Sorting "dab" gives "adbc".
        # Then sorting "dbc" gives "bcd" -> "abcd". (2 operations)
        self.assertEqual(self.sol.minOperations("dabc"), 2)

    def test_impossible_large_reverse(self):
        # For a strictly decreasing string of length > 2, it is always possible but takes multiple operations.
        # This test ensures a standard multi-op scrambled string resolves correctly.
        self.assertEqual(self.sol.minOperations("edcba"), 4)

if __name__ == "__main__":
    unittest.main()