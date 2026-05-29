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

class TestFinalValueAfterOperations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        """Tests the first example from the problem statement: mixed operations resulting in 1."""
        operations = ["--X", "X++", "X++"]
        expected_output = 1
        self.assertEqual(self.sol.finalValueAfterOperations(operations), expected_output)

    def test_example_2(self):
        """Tests the second example from the problem statement: all increment operations."""
        operations = ["++X", "++X", "X++"]
        expected_output = 3
        self.assertEqual(self.sol.finalValueAfterOperations(operations), expected_output)

    def test_example_3(self):
        """Tests the third example from the problem statement: net zero operations."""
        operations = ["X++", "++X", "--X", "X--"]
        expected_output = 0
        self.assertEqual(self.sol.finalValueAfterOperations(operations), expected_output)

    def test_single_increment_prefix(self):
        """Tests the minimum operational size with a single prefix increment."""
        operations = ["++X"]
        expected_output = 1
        self.assertEqual(self.sol.finalValueAfterOperations(operations), expected_output)

    def test_single_increment_postfix(self):
        """Tests the minimum operational size with a single postfix increment."""
        operations = ["X++"]
        expected_output = 1
        self.assertEqual(self.sol.finalValueAfterOperations(operations), expected_output)

    def test_single_decrement_prefix(self):
        """Tests the minimum operational size with a single prefix decrement."""
        operations = ["--X"]
        expected_output = -1
        self.assertEqual(self.sol.finalValueAfterOperations(operations), expected_output)

    def test_single_decrement_postfix(self):
        """Tests the minimum operational size with a single postfix decrement."""
        operations = ["X--"]
        expected_output = -1
        self.assertEqual(self.sol.finalValueAfterOperations(operations), expected_output)

    def test_all_decrements(self):
        """Tests a sequence composed entirely of decrement operations."""
        operations = ["--X", "X--", "--X", "X--"]
        expected_output = -4
        self.assertEqual(self.sol.finalValueAfterOperations(operations), expected_output)

    def test_large_input_net_positive(self):
        """Tests a larger list of operations that results in a positive value."""
        operations = ["++X", "X++", "++X", "--X", "X++", "X--", "++X", "X++", "X++", "--X"]
        # Initial: 0 -> 1 -> 2 -> 3 -> 2 -> 3 -> 2 -> 3 -> 4 -> 5 -> 4
        expected_output = 4
        self.assertEqual(self.sol.finalValueAfterOperations(operations), expected_output)

if __name__ == "__main__":
    unittest.main()