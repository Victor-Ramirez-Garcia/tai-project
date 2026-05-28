import unittest
import os
import importlib.util
# Load the file path from the environment variable set by your runner
solution_path = os.environ.get("TEST_SOLUTION_FILE")
spec = importlib.util.spec_from_file_location("SolutionModule", solution_path)
solution_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(solution_module)
Solution = solution_module.Solution

class TestGeneratedCode(unittest.TestCase):
    def test_python_code(self):
        solution = Solution()
        self.assertEqual(solution.foo(), "Hello, World!")
