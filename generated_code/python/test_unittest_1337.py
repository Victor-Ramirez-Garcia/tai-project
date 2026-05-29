import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Skiplist = sol_module.Skiplist


class TestSkiplist(unittest.TestCase):

    def test_example_case(self):
        """Validates the standard sequence provided in the LeetCode example."""
        skiplist = Skiplist()
        
        skiplist.add(1)
        skiplist.add(2)
        skiplist.add(3)
        
        self.assertFalse(skiplist.search(0), "Search for 0 should return False initially.")
        
        skiplist.add(4)
        
        self.assertTrue(skiplist.search(1), "Search for 1 should return True after addition.")
        self.assertFalse(skiplist.erase(0), "Erase of 0 should return False as it does not exist.")
        self.assertTrue(skiplist.erase(1), "Erase of 1 should return True.")
        self.assertFalse(skiplist.search(1), "Search for 1 should return False after erasure.")

    def test_empty_skiplist(self):
        """Validates actions on a newly initialized, empty Skiplist."""
        skiplist = Skiplist()
        self.assertFalse(skiplist.search(10), "Search on empty skiplist should return False.")
        self.assertFalse(skiplist.erase(10), "Erase on empty skiplist should return False.")

    def test_duplicate_elements(self):
        """Ensures that duplicate values are handled correctly during search and partial erasure."""
        skiplist = Skiplist()
        
        # Add duplicates
        skiplist.add(5)
        skiplist.add(5)
        skiplist.add(5)
        
        self.assertTrue(skiplist.search(5), "Search should find the duplicate element.")
        
        # Erase one instance
        self.assertTrue(skiplist.erase(5), "First erasure of 5 should succeed.")
        self.assertTrue(skiplist.search(5), "Search should still find 5 since duplicates remain.")
        
        # Erase second instance
        self.assertTrue(skiplist.erase(5), "Second erasure of 5 should succeed.")
        self.assertTrue(skiplist.search(5), "Search should still find 5 since one remains.")
        
        # Erase final instance
        self.assertTrue(skiplist.erase(5), "Third erasure of 5 should succeed.")
        self.assertFalse(skiplist.search(5), "Search should now return False as all instances are removed.")
        self.assertFalse(skiplist.erase(5), "Subsequent erasure of 5 should return False.")

    def test_boundary_values(self):
        """Tests minimal and maximal constraints often encountered in LeetCode problems (e.g., negative and large values)."""
        skiplist = Skiplist()
        
        min_val = -20000
        max_val = 20000
        zero_val = 0
        
        skiplist.add(min_val)
        skiplist.add(max_val)
        skiplist.add(zero_val)
        
        self.assertTrue(skiplist.search(min_val))
        self.assertTrue(skiplist.search(max_val))
        self.assertTrue(skiplist.search(zero_val))
        
        self.assertTrue(skiplist.erase(min_val))
        self.assertFalse(skiplist.search(min_val))

    def test_sequential_and_interleaved_operations(self):
        """Tests a larger volume of interleaved operations to verify consistency and state retention."""
        skiplist = Skiplist()
        elements = [10, 20, 30, 40, 50, 25, 35, 15, 5]
        
        for elem in elements:
            skiplist.add(elem)
            
        for elem in elements:
            self.assertTrue(skiplist.search(elem), f"Failed to find inserted element: {elem}")
            
        # Interleaved search and erase
        self.assertTrue(skiplist.erase(30))
        self.assertFalse(skiplist.search(30))
        self.assertTrue(skiplist.search(25))
        self.assertTrue(skiplist.search(35))
        
        self.assertTrue(skiplist.erase(5))
        self.assertFalse(skiplist.search(5))
        self.assertTrue(skiplist.search(10))


if __name__ == "__main__":
    unittest.main()