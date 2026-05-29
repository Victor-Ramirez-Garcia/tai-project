import os
import importlib.util
import unittest

# Dynamic loading of the solution module as mandated by guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("Environment variable 'TEST_SOLUTION_FILE' is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution
ListNode = sol_module.ListNode


class TestGetDecimalValue(unittest.TestCase):

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

    def test_example_1_multiple_nodes(self):
        """Test Example 1: head = [1,0,1] which equals 5 in decimal."""
        head = self._create_linked_list([1, 0, 1])
        solution = Solution()
        self.assertEqual(solution.getDecimalValue(head), 5)

    def test_example_2_single_zero(self):
        """Test Example 2: head = [0] which equals 0 in decimal."""
        head = self._create_linked_list([0])
        solution = Solution()
        self.assertEqual(solution.getDecimalValue(head), 0)

    def test_edge_case_single_one(self):
        """Test minimum size constraint with a value of 1: head = [1] which equals 1."""
        head = self._create_linked_list([1])
        solution = Solution()
        self.assertEqual(solution.getDecimalValue(head), 1)

    def test_edge_case_all_zeros(self):
        """Test multiple nodes all containing zeros: head = [0,0,0] which equals 0."""
        head = self._create_linked_list([0, 0, 0])
        solution = Solution()
        self.assertEqual(solution.getDecimalValue(head), 0)

    def test_edge_case_maximum_nodes_all_ones(self):
        """Test maximum size constraint (30 nodes) all set to 1."""
        # 30 nodes of 1s represents (2^30) - 1 = 1073741823
        values = [1] * 30
        head = self._create_linked_list(values)
        solution = Solution()
        expected_decimal = (1 << 30) - 1
        self.assertEqual(solution.getDecimalValue(head), expected_decimal)

    def test_edge_case_maximum_nodes_mixed(self):
        """Test maximum size constraint (30 nodes) with alternating alternating bits."""
        # 30 bits: 101010...10 (15 pairs of 10)
        # Binary: 101010101010101010101010101010 -> 715827882 in decimal
        values = [1, 0] * 15
        head = self._create_linked_list(values)
        solution = Solution()
        self.assertEqual(solution.getDecimalValue(head), 715827882)


if __name__ == "__main__":
    unittest.main()