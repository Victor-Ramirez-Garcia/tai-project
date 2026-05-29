import os
import importlib.util
import unittest

# Dynamic loading of the solution module via environment variable
solution_path = os.environ.get("TEST_SOLUTION_FILE")
spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
MyLinkedList = sol_module.MyLinkedList


class TestMyLinkedList(unittest.TestCase):

    def test_example_case(self):
        """Validates the standard LeetCode example sequence."""
        linked_list = MyLinkedList()
        linked_list.addAtHead(1)
        linked_list.addAtTail(3)
        linked_list.addAtIndex(1, 2)  # List: 1 -> 2 -> 3
        self.assertEqual(linked_list.get(1), 2)
        linked_list.deleteAtIndex(1)  # List: 1 -> 3
        self.assertEqual(linked_list.get(1), 3)

    def test_get_on_empty_list(self):
        """Validates that getting an element from an empty list returns -1."""
        linked_list = MyLinkedList()
        self.assertEqual(linked_list.get(0), -1)
        self.assertEqual(linked_list.get(-1), -1)
        self.assertEqual(linked_list.get(5), -1)

    def test_add_at_head(self):
        """Validates consecutive insertions at the head."""
        linked_list = MyLinkedList()
        linked_list.addAtHead(10)
        linked_list.addAtHead(20)
        linked_list.addAtHead(30)  # List: 30 -> 20 -> 10
        self.assertEqual(linked_list.get(0), 30)
        self.assertEqual(linked_list.get(1), 20)
        self.assertEqual(linked_list.get(2), 10)
        self.assertEqual(linked_list.get(3), -1)

    def test_add_at_tail(self):
        """Validates consecutive insertions at the tail."""
        linked_list = MyLinkedList()
        linked_list.addAtTail(10)
        linked_list.addAtTail(20)
        linked_list.addAtTail(30)  # List: 10 -> 20 -> 30
        self.assertEqual(linked_list.get(0), 10)
        self.assertEqual(linked_list.get(1), 20)
        self.assertEqual(linked_list.get(2), 30)
        self.assertEqual(linked_list.get(3), -1)

    def test_add_at_index(self):
        """Validates standard insertions at specified valid indices."""
        linked_list = MyLinkedList()
        # Add to empty list at index 0 (equivalent to head/tail)
        linked_list.addAtIndex(0, 10)  # List: 10
        # Add at index equal to length (equivalent to tail)
        linked_list.addAtIndex(1, 30)  # List: 10 -> 30
        # Add at an intermediate index
        linked_list.addAtIndex(1, 20)  # List: 10 -> 20 -> 30

        self.assertEqual(linked_list.get(0), 10)
        self.assertEqual(linked_list.get(1), 20)
        self.assertEqual(linked_list.get(2), 30)

    def test_add_at_index_edge_cases(self):
        """Validates behavior when adding at boundary or invalid indices."""
        linked_list = MyLinkedList()
        # If index is negative, insertion should ideally prepended to head (0)
        linked_list.addAtIndex(-1, 5)  # List: 5
        self.assertEqual(linked_list.get(0), 5)

        # If index is greater than length, the node should not be inserted
        linked_list.addAtIndex(5, 100)  # Length is 1, index 5 is invalid
        self.assertEqual(linked_list.get(1), -1)

    def test_delete_at_index(self):
        """Validates deletion operations at various valid and boundary indices."""
        linked_list = MyLinkedList()
        linked_list.addAtTail(10)
        linked_list.addAtTail(20)
        linked_list.addAtTail(30)
        linked_list.addAtTail(40)  # List: 10 -> 20 -> 30 -> 40

        # Delete from the middle
        linked_list.deleteAtIndex(1)  # List: 10 -> 30 -> 40
        self.assertEqual(linked_list.get(1), 30)

        # Delete the head
        linked_list.deleteAtIndex(0)  # List: 30 -> 40
        self.assertEqual(linked_list.get(0), 30)

        # Delete the tail (index == length - 1)
        linked_list.deleteAtIndex(1)  # List: 30
        self.assertEqual(linked_list.get(0), 30)
        self.assertEqual(linked_list.get(1), -1)

        # Delete the remaining single node
        linked_list.deleteAtIndex(0)  # List is now empty
        self.assertEqual(linked_list.get(0), -1)

    def test_delete_at_invalid_index(self):
        """Validates that deleting at invalid indices does not alter the list or crash."""
        linked_list = MyLinkedList()
        linked_list.addAtTail(10)
        linked_list.addAtTail(20)  # List: 10 -> 20

        # Negative index deletion should be ignored
        linked_list.deleteAtIndex(-1)
        self.assertEqual(linked_list.get(0), 10)

        # Index equal to length or greater should be ignored
        linked_list.deleteAtIndex(2)
        linked_list.deleteAtIndex(10)
        self.assertEqual(linked_list.get(0), 10)
        self.assertEqual(linked_list.get(1), 20)


if __name__ == "__main__":
    unittest.main()