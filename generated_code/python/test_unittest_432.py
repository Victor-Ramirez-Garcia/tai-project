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
AllOne = sol_module.AllOne


class TestAllOne(unittest.TestCase):

    def test_example_case(self):
        """Validates the standard sequence of operations provided in the problem description."""
        all_one = AllOne()
        all_one.inc("hello")
        all_one.inc("hello")
        self.assertEqual(all_one.getMaxKey(), "hello")
        self.assertEqual(all_one.getMinKey(), "hello")
        all_one.inc("leet")
        self.assertEqual(all_one.getMaxKey(), "hello")
        self.assertEqual(all_one.getMinKey(), "leet")

    def test_empty_data_structure(self):
        """Verifies that getMaxKey and getMinKey return empty strings when no keys exist."""
        all_one = AllOne()
        self.assertEqual(all_one.getMaxKey(), "")
        self.assertEqual(all_one.getMinKey(), "")

    def test_single_element_insertion_and_removal(self):
        """Tests inserting a single key, decrementing it to 0, and ensuring it is removed."""
        all_one = AllOne()
        all_one.inc("apple")
        self.assertEqual(all_one.getMaxKey(), "apple")
        self.assertEqual(all_one.getMinKey(), "apple")
        
        all_one.dec("apple")
        self.assertEqual(all_one.getMaxKey(), "")
        self.assertEqual(all_one.getMinKey(), "")

    def test_multiple_keys_same_frequency(self):
        """Tests behavior when multiple keys have the exact same minimum or maximum frequency."""
        all_one = AllOne()
        all_one.inc("a")
        all_one.inc("b")
        all_one.inc("c")
        
        # Any of the keys are valid as they all have a frequency of 1
        self.assertIn(all_one.getMaxKey(), {"a", "b", "c"})
        self.assertIn(all_one.getMinKey(), {"a", "b", "c"})

    def test_frequency_increment_and_decrement_ordering(self):
        """Tests structural adjustments as keys dynamically change frequencies."""
        all_one = AllOne()
        all_one.inc("key1")
        all_one.inc("key1")
        all_one.inc("key1")  # key1 freq = 3
        
        all_one.inc("key2")
        all_one.inc("key2")  # key2 freq = 2
        
        all_one.inc("key3")  # key3 freq = 1
        
        self.assertEqual(all_one.getMaxKey(), "key1")
        self.assertEqual(all_one.getMinKey(), "key3")
        
        # Decrement key1 down to freq 1
        all_one.dec("key1")
        all_one.dec("key1")  # key1 freq = 1
        
        # key2 (freq 2) should now be the maximum
        self.assertEqual(all_one.getMaxKey(), "key2")
        # key1 or key3 (freq 1) should be the minimum
        self.assertIn(all_one.getMinKey(), {"key1", "key3"})

    def test_key_reinsertion_after_removal(self):
        """Ensures a key can be entirely removed and successfully re-inserted with clean state."""
        all_one = AllOne()
        all_one.inc("temp")
        all_one.dec("temp")
        self.assertEqual(all_one.getMaxKey(), "")
        
        all_one.inc("temp")
        self.assertEqual(all_one.getMaxKey(), "temp")
        self.assertEqual(all_one.getMinKey(), "temp")


if __name__ == "__main__":
    unittest.main()