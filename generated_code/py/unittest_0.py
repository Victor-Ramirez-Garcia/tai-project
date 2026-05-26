import unittest
from generated_code.utest_0.py.utest_0 import foo
import sol_0.py

class TestGeneratedCode(unittest.TestCase):
    def test_python_code(self):
        self.assertEqual(foo(), "Hello, World!")
