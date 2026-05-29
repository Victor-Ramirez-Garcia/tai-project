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

# Access the ListNode class dynamically from the module, or fallback if it's commented out in their starter
if hasattr(sol_module, 'ListNode'):
    ListNode = sol_module.ListNode
else:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

class TestHasCycle(unittest.TestCase):
    
    def create_linked_list_with_cycle(self, values, pos):
        """Helper method to construct a linked list and create a cycle at pos."""
        if not values:
            return None
        
        head = ListNode(values[0])
        current = head
        nodes = [head]
        
        for val in values[1:]:
            new_node = ListNode(val)
            current.next = new_node
            current = new_node
            nodes.append(new_node)
            
        if pos != -1 and 0 <= pos < len(nodes):
            current.next = nodes[pos]
            
        return head

    def test_example_1_has_cycle(self):
        # Input: head = [3,2,0,-4], pos = 1 -> Output: True
        head = self.create_linked_list_with_cycle([3, 2, 0, -4], 1)
        sol = Solution()
        self.assertTrue(sol.hasCycle(head))

    def test_example_2_has_cycle(self):
        # Input: head = [1,2], pos = 0 -> Output: True
        head = self.create_linked_list_with_cycle([1, 2], 0)
        sol = Solution()
        self.assertTrue(sol.hasCycle(head))

    def test_example_3_no_cycle(self):
        # Input: head = [1], pos = -1 -> Output: False
        head = self.create_linked_list_with_cycle([1], -1)
        sol = Solution()
        self.assertFalse(sol.hasCycle(head))

    def test_edge_case_empty_list(self):
        # Constraints: number of nodes can be 0. pos = -1
        head = self.create_linked_list_with_cycle([], -1)
        sol = Solution()
        self.assertFalse(sol.hasCycle(head))

    def test_edge_case_single_node_with_self_cycle(self):
        # Constraints: 1 node, pos = 0 (tail connects to itself)
        head = self.create_linked_list_with_cycle([42], 0)
        sol = Solution()
        self.assertTrue(sol.hasCycle(head))

    def test_large_list_no_cycle(self):
        # Upper constraint limit verification without cycle
        values = list(range(1000))
        head = self.create_linked_list_with_cycle(values, -1)
        sol = Solution()
        self.assertFalse(sol.hasCycle(head))

    def test_large_list_with_cycle(self):
        # Upper constraint limit verification with a cycle near the middle
        values = list(range(1000))
        head = self.create_linked_list_with_cycle(values, 500)
        sol = Solution()
        self.assertTrue(sol.hasCycle(head))