import os
import importlib.util
import unittest

# Dynamic loading of the solution module
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise ValueError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution
ListNode = sol_module.ListNode


class TestMergeNodes(unittest.TestCase):
    def helper_create_linked_list(self, arr):
        """Helper method to create a linked list from an array."""
        if not arr:
            return None
        head = ListNode(arr[0])
        current = head
        for val in arr[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def helper_linked_list_to_list(self, head):
        """Helper method to convert a linked list back to a Python list."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_example_1(self):
        """Tests Example 1: head = [0, 3, 1, 0, 4, 5, 2, 0] -> [4, 11]"""
        input_list = [0, 3, 1, 0, 4, 5, 2, 0]
        expected_output = [4, 11]

        head = self.helper_create_linked_list(input_list)
        sol = Solution()
        modified_head = sol.mergeNodes(head)
        output_list = self.helper_linked_list_to_list(modified_head)

        self.assertEqual(output_list, expected_output)

    def test_example_2(self):
        """Tests Example 2: head = [0, 1, 0, 3, 0, 2, 2, 0] -> [1, 3, 4]"""
        input_list = [0, 1, 0, 3, 0, 2, 2, 0]
        expected_output = [1, 3, 4]

        head = self.helper_create_linked_list(input_list)
        sol = Solution()
        modified_head = sol.mergeNodes(head)
        output_list = self.helper_linked_list_to_list(modified_head)

        self.assertEqual(output_list, expected_output)

    def test_minimum_constraints(self):
        """Tests the minimum possible valid length constraint (3 nodes: [0, X, 0])."""
        input_list = [0, 5, 0]
        expected_output = [5]

        head = self.helper_create_linked_list(input_list)
        sol = Solution()
        modified_head = sol.mergeNodes(head)
        output_list = self.helper_linked_list_to_list(modified_head)

        self.assertEqual(output_list, expected_output)

    def test_nodes_with_zero_value(self):
        """Tests segments containing non-zero values that are actually 0, but separated (e.g., Node.val == 0 but not consecutive 0's)."""
        input_list = [0, 0, 0]  # The constraints say 'no two consecutive nodes with Node.val == 0' (except bounding zeros, meaning this exact case is invalid per rules, but a segment summing to 0 is possible if nodes are 0? Wait, constraint says '0 <= Node.val <= 1000' and 'no two consecutive nodes with Node.val == 0'. Thus, zeros only exist as delimiters. Let's test single large numbers instead.)
        pass

    def test_single_element_segments(self):
        """Tests multiple segments where each segment contains exactly one node."""
        input_list = [0, 10, 0, 20, 0, 30, 0]
        expected_output = [10, 20, 30]

        head = self.helper_create_linked_list(input_list)
        sol = Solution()
        modified_head = sol.mergeNodes(head)
        output_list = self.helper_linked_list_to_list(modified_head)

        self.assertEqual(output_list, expected_output)

    def test_large_segment_values(self):
        """Tests values at the upper constraint limit (Node.val up to 1000)."""
        input_list = [0, 1000, 1000, 1000, 0, 500, 500, 0]
        expected_output = [3000, 1000]

        head = self.helper_create_linked_list(input_list)
        sol = Solution()
        modified_head = sol.mergeNodes(head)
        output_list = self.helper_linked_list_to_list(modified_head)

        self.assertEqual(output_list, expected_output)


if __name__ == "__main__":
    unittest.main()