import os
import importlib.util
import unittest

# Dynamic loading of the solution module
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestMaxAverageRatio(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()
        # Define acceptable delta for floating point comparisons based on problem statement (10^-5)
        self.places = 5

    def test_example_1(self):
        classes = [[1, 2], [3, 5], [2, 2]]
        extra_students = 2
        expected = 0.78333
        result = self.sol.maxAverageRatio(classes, extra_students)
        self.assertAlmostEqual(result, expected, places=self.places)

    def test_example_2(self):
        classes = [[2, 4], [3, 9], [4, 5], [2, 10]]
        extra_students = 4
        expected = 0.53485
        result = self.sol.maxAverageRatio(classes, extra_students)
        self.assertAlmostEqual(result, expected, places=self.places)

    def test_single_class_minimum_constraints(self):
        # Smallest possible input size: 1 class, 1 student, 1 extra student
        classes = [[1, 1]]
        extra_students = 1
        # (1+1)/(1+1) = 2/2 = 1.0
        expected = 1.0
        result = self.sol.maxAverageRatio(classes, extra_students)
        self.assertAlmostEqual(result, expected, places=self.places)

    def test_single_class_with_large_extra_students(self):
        classes = [[1, 2]]
        extra_students = 99999
        # (1 + 99999