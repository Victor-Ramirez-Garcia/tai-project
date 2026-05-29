import os
import importlib.util
import unittest

# Dynamic loading of the Solution class
solution_path = os.environ.get("TEST_SOLUTION_FILE")
spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

class TestEqualFrequency(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1_abcc(self):
        """Example 1: Removing one 'c' from 'abcc' leaves frequencies {a:1, b:1, c:1}."""
        self.assertTrue(self.sol.equalFrequency("abcc"))

    def test_example_2_aazz(self):
        """Example 2: Removing any char from 'aazz' leaves unequal frequencies (1 and 2)."""
        self.assertFalse(self.sol.equalFrequency("aazz"))

    def test_single_character(self):
        """Constraint: Minimum length string. Removing the only char leaves an empty set (equal)."""
        self.assertTrue(self.sol.equalFrequency("a"))

    def test_all_unique_characters(self):
        """Case: All characters unique. Removing any keeps all frequencies at 1."""
        self.assertTrue(self.sol.equalFrequency("abcdef"))

    def test_all_same_characters(self):
        """Case: All characters the same. Removing one keeps all (remaining) frequencies the same."""
        self.assertTrue(self.sol.equalFrequency("aaaaa"))

    def test_one_extra_frequency_of_one(self):
        """Case: One character has frequency 1, others have frequency N. Remove the unique one."""
        self.assertTrue(self.sol.equalFrequency("aabbccz"))

    def test_one_character_slightly_higher_frequency(self):
        """Case: All but one char have frequency N, one has frequency N+1. Remove from the N+1 one."""
        self.assertTrue(self.sol.equalFrequency("aaabbbcccdddd"))

    def test_two_characters_frequency_two(self):
        """Case: Two characters with frequency 2. Removing one leaves 1 and 2."""
        self.assertFalse(self.sol.equalFrequency("aabb"))

    def test_complex_false_case(self):
        """Case: Multiple differences that cannot be solved with one removal."""
        self.assertFalse(self.sol.equalFrequency("aaabbbccc"))

    def test_max_constraint_valid(self):
        """Case: Large input string where one removal satisfies the condition."""
        word = "a" * 49 + "b" * 50
        self.assertTrue(self.sol.equalFrequency(word))

    def test_single_char_freq_one_remaining_freq_large(self):
        """Case: "zzzzza" -> removing 'a' leaves only 'z's."""
        self.assertTrue(self.sol.equalFrequency("zzzzza"))

    def test_reduction_to_one_not_possible(self):
        """Case: "aabbcd" -> frequencies {2,2,1,1}. Removing one does not equalize others."""
        self.assertFalse(self.sol.equalFrequency("aabbcd"))