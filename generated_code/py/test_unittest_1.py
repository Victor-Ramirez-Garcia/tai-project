import unittest
from solution_1_1 import Solution

class TestGeneratedCode(unittest.TestCase):
    def test_python_code(self):
        solution = Solution()
        self.assertEqual(solution.foo(), "Hello, World!")
