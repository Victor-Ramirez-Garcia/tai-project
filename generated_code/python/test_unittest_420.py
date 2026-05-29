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


class TestStrongPasswordChecker(unittest.TestCase):
    def setUp(self):
        self.checker = Solution()

    # --- Problem Examples ---

    def test_example_1_short_single_char(self):
        # Requires 5 insertions to reach length 6 and satisfy missing types
        self.assertEqual(self.checker.strongPasswordChecker("a"), 5)

    def test_example_2_short_mixed_types(self):
        # Length 3, has lower, upper, digit. Needs 3 insertions for length 6
        self.assertEqual(self.checker.strongPasswordChecker("aA1"), 3)

    def test_example_3_already_strong(self):
        # Length 8, has lower, upper, digit, no 3-repeats
        self.assertEqual(self.checker.strongPasswordChecker("1337C0d3"), 0)

    # --- Edge Cases: Short Passwords (< 6 characters) ---

    def test_short_empty_string(self):
        # Length 0 constraint boundary check (if input can be empty)
        self.assertEqual(self.checker.strongPasswordChecker(""), 6)

    def test_short_missing_all_types(self):
        # Length 5, but all same lowercase characters.
        # Needs 1 insertion to reach length 6, which can break the repeat and add a type,
        # but we still need 2 more types (upper, digit). Max(6-5, missing_types) = 3
        self.assertEqual(self.checker.strongPasswordChecker("aaaaa"), 3)

    def test_short_exactly_five_chars_with_repeats(self):
        # Length 5, missing upper and digit. Repeats can be handled by the insertion
        # that brings length to 6.
        self.assertEqual(self.checker.strongPasswordChecker("aaa1a"), 2)

    # --- Edge Cases: Valid Length (6 to 20 characters) ---

    def test_valid_length_missing_all_types(self):
        # Length 6, but only lowercase and repeating. Missing upper and digit.
        # Replacing characters can fix both repeats and missing types.
        self.assertEqual(self.checker.strongPasswordChecker("aaaaaa"), 2)

    def test_valid_length_one_repeat_group_missing_types(self):
        # Length 6, missing upper and digit. "aaa" needs 1 replacement.
        # The other missing type needs another replacement. Total = 2.
        self.assertEqual(self.checker.strongPasswordChecker("aaa123"), 2)

    def test_valid_length_multiple_separated_repeats(self):
        # Length 10, has upper, lower, digit. Two distinct repeating triplets.
        # Requires 2 replacements (one for each triplet).
        self.assertEqual(self.checker.strongPasswordChecker("aaaBBB1112"), 2)

    # --- Edge Cases: Long Passwords (> 20 characters) ---

    def test_long_exactly_21_chars_one_repeat(self):
        # Length 21, all types present. Needs 1 deletion.
        # "aaaaaa" -> 6 same chars. Deleting 1 leaves 5, which still needs 1 replacement.
        # Total: 1 deletion + 1 replacement = 2 steps.
        self.assertEqual(self.checker.strongPasswordChecker("aaaaaaA1bcdefghijklmn"), 2)

    def test_long_large_repeat_group_requiring_deletions(self):
        # Length 22, all types present. "aaaaaaa" (7 'a's).
        # Optimization prefers deleting from groups where len % 3 == 1.
        self.assertEqual(self.checker.strongPasswordChecker("aaaaaaaA1bcdefghijklmn"), 3)

    def test_long_maximum_constraint_boundary(self):
        # Complex case with multiple repeating structures requiring structural changes and deletions.
        password = "AAAAAaaaaa1111122222BB"  # Length 22
        # Missing: None. Length: 22 (needs 2 deletions).
        # Repeats: AAAAA (5), aaaaa (5), 11111 (5), 22222 (5)
        self.assertEqual(self.checker.strongPasswordChecker(password), 6)


if __name__ == "__main__":
    unittest.main()