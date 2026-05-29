import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise ImportError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution
ListNode = sol_module.ListNode


class TestRemoveLinkedListElements(unittest.TestCase):

    def _create_linked_list(self, arr):
        """Helper method to create a linked list from a list."""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def _linked_list_to_list(self, head):
        """Helper method to convert a linked list back to a Python list."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_example_1_mixed_elements(self):
        """Test Example 1: Standard case with target elements in middle and end."""
        head = self._create_linked_list([1, 2, 6, 3, 4, 5, 6])
        val = 6
        sol = Solution()
        new_head = sol.removeElements(head, val)
        self.assertEqual(self._linked_list_to_list(new_head), [1, 2, 3, 4, 5])

    def test_example_2_empty_list(self):
        """Test Example 2: Edge case where the input list is completely empty."""
        head = self._create_linked_list([])
        val = 1
        sol = Solution()
        new_head = sol.removeElements(head, val)
        self.assertEqual(self._linked_list_to_list(new_head), [])

    def test_example_3_all_elements_match(self):
        """Test Example 3: Case where every single node matches the target value."""
        head = self._create_linked_list([7, 7, 7, 7])
        val = 7
        sol = Solution()
        new_head = sol.removeElements(head, val)
        self.assertEqual(self._linked_list_to_list(new_head), [])

    def test_edge_case_single_element_matching(self):
        """Test edge case with a single node list that matches the target value."""
        head = self._create_linked_list([5])
        val = 5
        sol = Solution()
        new_head = sol.removeElements(head, val)
        self.assertEqual(self._linked_list_to_list(new_head), [])

    def test_edge_case_single_element_not_matching(self):
        """Test edge case with a single node list that does not match the target value."""
        head = self._create_linked_list([5])
        val = 3
        sol = Solution()
        new_head = sol.removeElements(head, val)
        self.assertEqual(self._linked_list_to_list(new_head), [5])

    def test_target_at_head_only(self):
        """Test case where target elements are strictly at the beginning of the list."""
        head = self._create_linked_list([1, 1, 2, 3])
        val = 1
        sol = Solution()
        new_head = sol.removeElements(head, val)
        self.assertEqual(self._linked_list_to_list(new_head), [2, 3])

    def test_target_at_tail_only(self):
        """Test case where target elements are strictly at the end of the list."""
        head = self._create_linked_list([2, 3, 4, 4])
        val = 4
        sol = Solution()
        new_head = sol.removeElements(head, val)
        self.assertEqual(self._linked_list_to_list(new_head), [2, 3])

    def test_no_elements_match(self):
        """Test case where no elements in the list match the target value."""
        head = self._create_linked_list([1, 2, 3, 4, 5])
        val = 0
        sol = Solution()
        new_head = sol.removeElements(head, val)
        self.assertEqual(self._linked_list_to_list(new_head), [1, 2, 3, 4, 5])

    def test_consecutive_target_elements_interspersed(self):
        """Test case containing multiple consecutive target values interspersed with non-target values."""
        head = self._create_linked_list([1, 2, 2, 3, 2, 2, 2, 4, 2])
        val = 2
        sol = Solution()
        new_head = sol.removeElements(head, val)
        self.assertEqual(self._linked_list_to_list(new_head), [1, 3, 4])


if __name__ == "__main__":
    unittest.main()