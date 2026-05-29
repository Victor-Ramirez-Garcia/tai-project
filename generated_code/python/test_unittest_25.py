import os
import importlib.util
import unittest

# Dynamic loading of the solution module as mandated by guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution
ListNode = sol_module.ListNode


class TestReverseKGroup(unittest.TestCase):
    def _create_linked_list(self, values):
        """Helper method to construct a linked list from a list of values."""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def _linked_list_to_list(self, head):
        """Helper method to convert a linked list back into a Python list."""
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        return values

    def _assert_reverse_k_group(self, input_list, k, expected_list):
        """Helper assertion method to execute the test and verify output."""
        head = self._create_linked_list(input_list)
        solution = Solution()
        result_head = solution.reverseKGroup(head, k)
        result_list = self._linked_list_to_list(result_head)
        self.assertEqual(result_list, expected_list)

    def test_example_1(self):
        """Tests Example 1: Full blocks of size 2 with one leftover element."""
        self._assert_reverse_k_group([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5])

    def test_example_2(self):
        """Tests Example 2: One full block of size 3 with leftovers at the end."""
        self._assert_reverse_k_group([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5])

    def test_minimum_constraints(self):
        """Tests the absolute minimum constraint where n = 1 and k = 1."""
        self._assert_reverse_k_group([1], 1, [1])

    def test_k_equals_one(self):
        """Tests that the list remains unchanged when k = 1."""
        self._assert_reverse_k_group([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5])

    def test_k_equals_length_exact(self):
        """Tests reversing the entire list when k is exactly equal to the list length."""
        self._assert_reverse_k_group([1, 2, 3, 4], 4, [4, 3, 2, 1])

    def test_length_exact_multiple_of_k(self):
        """Tests a list whose total length is an exact multiple of k (no remainders)."""
        self._assert_reverse_k_group([1, 2, 3, 4, 5, 6], 3, [3, 2, 1, 6, 5, 4])

    def test_length_less_than_k(self):
        """Tests that the list remains unchanged if total length is less than k."""
        self._assert_reverse_k_group([1, 2, 3], 4, [1, 2, 3])

    def test_node_values_bounds(self):
        """Tests correctness when node values touch the boundary limits (0 and 1000)."""
        self._assert_reverse_k_group([0, 500, 1000, 250], 2, [500, 0, 250, 1000])


if __name__ == "__main__":
    unittest.main()