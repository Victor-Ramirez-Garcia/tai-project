import unittest
from solution_5_1 import Solution

class TestGeneratedCode(unittest.TestCase):
    def test_python_code(self):
        solution = Solution()
        self.assertEqual(solution.foo(), "a")
