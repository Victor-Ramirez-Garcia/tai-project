import unittest
import os
import importlib.util

# Dynamic loading of the Solution class based on the environment variable
solution_path = os.environ.get("TEST_SOLUTION_FILE")
spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

class TestMinOperations(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        """Test case from Example 1: '110' -> [1, 1, 3]"""
        boxes = "110"
        expected = [1, 1, 3]
        self.assertEqual(self.sol.minOperations(boxes), expected)

    def test_example_2(self):
        """Test case from Example 2: '001011' -> [11, 8, 5, 4, 3, 4]"""
        boxes = "001011"
        expected = [11, 8, 5, 4, 3, 4]
        self.assertEqual(self.sol.minOperations(boxes), expected)

    def test_minimum_constraint_no_ball(self):
        """Edge case: Minimum length (1) with no ball."""
        boxes = "0"
        expected = [0]
        self.assertEqual(self.sol.minOperations(boxes), expected)

    def test_minimum_constraint_with_ball(self):
        """Edge case: Minimum length (1) with one ball."""
        boxes = "1"
        expected = [0]
        self.assertEqual(self.sol.minOperations(boxes), expected)

    def test_all_zeros(self):
        """Edge case: Large input with no balls present."""
        boxes = "00000"
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(self.sol.minOperations(boxes), expected)

    def test_all_ones(self):
        """Edge case: All boxes contain a ball."""
        boxes = "111"
        # Box 0: 1+2=3, Box 1: 1+1=2, Box 2: 2+1=3
        expected = [3, 2, 3]
        self.assertEqual(self.sol.minOperations(boxes), expected)

    def test_balls_at_extremes(self):
        """Edge case: Balls only at the very first and last positions."""
        boxes = "10001"
        # Box 0: 0+4=4, Box 1: 1+3=4, Box 2: 2+2=4, Box 3: 3+1=4, Box 4: 4+0=4
        expected = [4, 4, 4, 4, 4]
        self.assertEqual(self.sol.minOperations(boxes), expected)

    def test_single_ball_middle(self):
        """Scenario: Only one ball in the middle of the string."""
        boxes = "00100"
        # Distances to index 2: 2, 1, 0, 1, 2
        expected = [2, 1, 0, 1, 2]
        self.assertEqual(self.sol.minOperations(boxes), expected)

if __name__ == "__main__":
    unittest.main()