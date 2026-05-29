import os
import importlib.util
import unittest
from collections import Counter

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestFrequencySort(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def assert_valid_frequency_sort(self, original: str, result: str):
        """
        Helper method to validate if the result string is a correctly sorted 
        version of the original string based on character frequencies.
        """
        # 1. Check length equivalence
        self.assertEqual(len(original), len(result))
        
        # 2. Check that character compositions match
        orig_counts = Counter(original)
        res_counts = Counter(result)
        self.assertEqual(orig_counts, res_counts)
        
        # 3. Check that identical characters are grouped together sequentially
        # and frequencies are sorted in descending order
        current_char = None
        seen_chars = set()
        last_frequency = float('inf')
        
        i = 0
        while i < len(result):
            char = result[i]
            # Detect character transitions
            if char != current_char:
                if char in seen_chars:
                    self.fail(f"Characters are not grouped together: '{char}' reappeared.")
                seen_chars.add(char)
                current_char = char
                
                # Verify that frequencies strictly decrease or stay equal
                char_freq = orig_counts[char]
                if char_freq > last_frequency:
                    self.fail(f"Frequencies are not in decreasing order. "
                              f"'{char}' with frequency {char_freq} appeared after a lower frequency group.")
                last_frequency = char_freq
            
            # Verify the block size matches the expected frequency
            block_len = 0
            while i < len(result) and result[i] == current_char:
                block_len += 1
                i += 1
                
            if block_len != orig_counts[current_char]:
                self.fail(f"Fragment block for '{current_char}' has an invalid length.")
            
    def test_example_1(self):
        s = "tree"
        result = self.sol.frequencySort(s)
        self.assert_valid_frequency_sort(s, result)

    def test_example_2(self):
        s = "cccaaa"
        result = self.sol.frequencySort(s)
        self.assert_valid_frequency_sort(s, result)

    def test_example_3(self):
        s = "Aabb"
        result = self.sol.frequencySort(s)
        self.assert_valid_frequency_sort(s, result)

    def test_minimum_length_constraint(self):
        # Constraint: 1 <= s.length
        s = "a"
        result = self.sol.frequencySort(s)
        self.assertEqual(result, "a")

    def test_all_same_characters(self):
        s = "vvvvvvv"
        result = self.sol.frequencySort(s)
        self.assertEqual(result, "vvvvvvv")

    def test_all_distinct_characters(self):
        s = "abcdef"
        result = self.sol.frequencySort(s)
        self.assert_valid_frequency_sort(s, result)

    def test_case_sensitivity(self):
        s = "cccCCC"
        result = self.sol.frequencySort(s)
        self.assert_valid_frequency_sort(s, result)

    def test_digits_and_letters(self):
        s = "m1m1m122bb"
        result = self.sol.frequencySort(s)
        self.assert_valid_frequency_sort(s, result)


if __name__ == "__main__":
    unittest.main()