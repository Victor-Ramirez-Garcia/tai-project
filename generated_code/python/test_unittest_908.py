import os
import sys
import importlib.util
import unittest

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

# Dynamically access ListNode from the module if defined there, otherwise define a standard one
if hasattr(sol_module, "ListNode"):
    ListNode = sol_module.ListNode
else:
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next


class TestMiddleNode(unittest.TestCase):
    def _create_linked_list(self, arr):
        """Helper method to construct a linked list from an array."""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def _linked_list_to_list(self, head):
        """Helper method to convert a linked list back to an array for assertion."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_example_1_odd_length(self):
        """Test with an odd number of nodes (Example 1: [1,2,3,4,5] -> [3,4,5])."""
        input_list = [1, 2, 3, 4, 5]
        head = self._create_linked_list(input_list)
        
        sol = Solution()
        actual_middle = sol.middleNode(head)
        
        actual_output = self._linked_list_to_list(actual_middle)
        expected_output = [3, 4, 5]
        self.assertEqual(actual_output, expected_output)

    def test_example_2_even_length(self):
        """Test with an even number of nodes (Example 2: [1,2,3,4,5,6] -> [4,5,6])."""
        input_list = [1, 2, 3, 4, 5, 6]
        head = self._create_linked_list(input_list)
        
        sol = Solution()
        actual_middle = sol.middleNode(head)
        
        actual_output = self._linked_list_to_list(actual_middle)
        expected_output = [4, 5, 6]
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_single_node(self):
        """Test the minimum boundary constraint: a list containing exactly 1 node."""
        input_list = [1]
        head = self._create_linked_list(input_list)
        
        sol = Solution()
        actual_middle = sol.middleNode(head)
        
        actual_output = self._linked_list_to_list(actual_middle)
        expected_output = [1]
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_two_nodes(self):
        """Test a minimal even length list containing exactly 2 nodes."""
        input_list = [1, 2]
        head = self._create_linked_list(input_list)
        
        sol = Solution()
        actual_middle = sol.middleNode(head)
        
        actual_output = self._linked_list_to_list(actual_middle)
        expected_output = [2]
        self.assertEqual(actual_output, expected_output)

    def test_edge_case_maximum_constraints(self):
        """Test the maximum boundary constraint: a list containing 100 nodes."""
        input_list = list(range(1, 101))  # [1, 2, ..., 100]
        head = self._create_linked_list(input_list)
        
        sol = Solution()
        actual_middle = sol.middleNode(head)
        
        actual_output = self._linked_list_to_list(actual_middle)
        # Even length 100: middle nodes are 50 and 51, should return from 51 onwards
        expected_output = list(range(51, 101))
        self.assertEqual(actual_output, expected_output)


if __name__ == "__main__":
    unittest.main()