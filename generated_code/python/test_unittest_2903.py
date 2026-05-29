import os
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
ListNode = sol_module.ListNode


class TestInsertGreatestCommonDivisors(unittest.TestCase):

    def _create_linked_list(self, arr):
        """Helper method to construct a linked list from an array."""
        if not arr:
            return None
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.next = ListNode(val)
            curr = curr.next
        return head

    def _linked_list_to_list(self, head):
        """Helper method to convert a linked list to a Python list for easy assertion."""
        result = []
        curr = head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def test_example_1_multiple_nodes(self):
        """Test with multiple nodes having various GCD values (Example 1)."""
        input_list = [18, 6, 10, 3]
        expected_output = [18, 6, 6, 2, 10, 1, 3]
        
        head = self._create_linked_list(input_list)
        sol = Solution()
        result_head = sol.insertGreatestCommonDivisors(head)
        
        self.assertEqual(self._linked_list_to_list(result_head), expected_output)

    def test_example_2_single_node(self):
        """Test with a single node where no pairs exist (Example 2 / Minimum constraint)."""
        input_list = [7]
        expected_output = [7]
        
        head = self._create_linked_list(input_list)
        sol = Solution()
        result_head = sol.insertGreatestCommonDivisors(head)
        
        self.assertEqual(self._linked_list_to_list(result_head), expected_output)

    def test_two_nodes_same_value(self):
        """Test with two nodes having identical values (GCD should equal the value)."""
        input_list = [5, 5]
        expected_output = [5, 5, 5]
        
        head = self._create_linked_list(input_list)
        sol = Solution()
        result_head = sol.insertGreatestCommonDivisors(head)
        
        self.assertEqual(self._linked_list_to_list(result_head), expected_output)

    def test_two_nodes_coprime(self):
        """Test with two coprime nodes (GCD should be 1)."""
        input_list = [13, 7]
        expected_output = [13, 1, 7]
        
        head = self._create_linked_list(input_list)
        sol = Solution()
        result_head = sol.insertGreatestCommonDivisors(head)
        
        self.assertEqual(self._linked_list_to_list(result_head), expected_output)

    def test_maximum_constraint_values(self):
        """Test with maximum allowed node values (1000) to ensure correctness."""
        input_list = [1000, 500, 1000]
        expected_output = [1000, 500, 500, 500, 1000]
        
        head = self._create_linked_list(input_list)
        sol = Solution()
        result_head = sol.insertGreatestCommonDivisors(head)
        
        self.assertEqual(self._linked_list_to_list(result_head), expected_output)


if __name__ == "__main__":
    unittest.main()