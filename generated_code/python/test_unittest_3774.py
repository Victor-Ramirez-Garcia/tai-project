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


class TestHasSameDigits(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_example_1_same_final_digits(self):
        """
        Tests a standard case where reduction results in two identical digits.
        Example simulation: '3902' -> '292' -> '11' -> True
        """
        s = "3902"
        self.assertTrue(self.sol.hasSameDigits(s))

    def test_example_2_different_final_digits(self):
        """
        Tests a standard case where reduction results in two different digits.
        Example simulation: '34789' -> '7157' -> '862' -> '48' -> False
        """
        s = "34789"
        self.assertFalse(self.sol.hasSameDigits(s))

    def test_minimum_length_edge_case_true(self):
        """
        Tests the absolute minimum constraints where the input already has 2 identical digits.
        """
        s = "44"
        self.assertTrue(self.sol.hasSameDigits(s))

    def test_minimum_length_edge_case_false(self):
        """
        Tests the absolute minimum constraints where the input already has 2 distinct digits.
        """
        s = "45"
        self.assertFalse(self.sol.hasSameDigits(s))

    def test_all_zeros(self):
        """
        Tests a string entirely composed of zeros, which should always evaluate to '00' -> True.
        """
        s = "0000000"
        self.assertTrue(self.sol.hasSameDigits(s))

    def test_all_same_non_zero_digits(self):
        """
        Tests a string where all initial digits are identical but non-zero.
        """
        s = "5555"  # '5555' -> '000' -> '00' -> True
        self.assertTrue(self.sol.hasSameDigits(s))

    def test_alternating_digits(self):
        """
        Tests an alternating sequence pattern.
        """
        s = "121212"
        # '121212' -> '33333' -> '6666' -> '222' -> '44' -> True
        self.assertTrue(self.sol.hasSameDigits(s))

    def test_large_sum_modulo_behavior(self):
        """
        Tests scenarios where consecutive sums heavily trigger the modulo 10 boundary (e.g., 9+9=18 -> 8).
        """
        s = "9999"  # '9999' -> '888' -> '66' -> True
        self.assertTrue(self.sol.hasSameDigits(s))
        
        s2 = "9898" # '9898' -> '777' -> '44' -> True
        self.assertTrue(self.sol.hasSameDigits(s2))


if __name__ == "__main__":
    unittest.main()