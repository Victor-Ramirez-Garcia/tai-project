import unittest
from typing import List, Optional
from program_2_1 import Solution

# Definition for singly-linked list (needed for test setup and verification)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestAddTwoNumbers(unittest.TestCase):

    def helper_create_linked_list(self, arr: List[int]) -> Optional[ListNode]:
        """Helper method to convert a Python list into a ListNode linked list."""
        if not arr:
            return None
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def helper_linked_list_to_list(self, head: Optional[ListNode]) -> List[int]:
        """Helper method to convert a ListNode linked list back into a Python list."""
        arr = []
        current = head
        while current:
            arr.append(current.val)
            current = current.next
        return arr

    def assert_linked_lists_equal(self, expected_arr: List[int], actual_head: Optional[ListNode]):
        """Custom assertion to verify the result linked list matches the expected array."""
        actual_arr = self.helper_linked_list_to_list(actual_head)
        self.assertEqual(actual_arr, expected_arr, f"Expected {expected_arr}, but got {actual_arr}")

    def test_example_1(self):
        """Test Example 1: l1 = [2,4,3], l2 = [5,6,4] -> Output: [7,0,8]"""
        sol = Solution()
        l1 = self.helper_create_linked_list([2, 4, 3])
        l2 = self.helper_create_linked_list([5, 6, 4])
        result = sol.addTwoNumbers(l1, l2)
        self.assert_linked_lists_equal([7, 0, 8], result)

    def test_example_2(self):
        """Test Example 2: l1 = [0], l2 = [0] -> Output: [0]"""
        sol = Solution()
        l1 = self.helper_create_linked_list([0])
        l2 = self.helper_create_linked_list([0])
        result = sol.addTwoNumbers(l1, l2)
        self.assert_linked_lists_equal([0], result)

    def test_example_3(self):
        """Test Example 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> Output: [8,9,9,9,0,0,0,1]"""
        sol = Solution()
        l1 = self.helper_create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.helper_create_linked_list([9, 9, 9, 9])
        result = sol.addTwoNumbers(l1, l2)
        self.assert_linked_lists_equal([8, 9, 9, 9, 0, 0, 0, 1], result)

    def test_different_lengths_l1_shorter(self):
        """Test lists of different lengths where l1 is shorter than l2."""
        sol = Solution()
        l1 = self.helper_create_linked_list([1])
        l2 = self.helper_create_linked_list([9, 9])
        result = sol.addTwoNumbers(l1, l2)
        self.assert_linked_lists_equal([0, 0, 1], result)

    def test_carry_creates_new_most_significant_digit(self):
        """Test where the final addition creates a carry that extends the list length."""
        sol = Solution()
        l1 = self.helper_create_linked_list([5])
        l2 = self.helper_create_linked_list([5])
        result = sol.addTwoNumbers(l1, l2)
        self.assert_linked_lists_equal([0, 1], result)

    def test_minimum_constraint_single_nodes(self):
        """Test minimum constraint values: Single nodes with low values without carry."""
        sol = Solution()
        l1 = self.helper_create_linked_list([1])
        l2 = self.helper_create_linked_list([2])
        result = sol.addTwoNumbers(l1, l2)
        self.assert_linked_lists_equal([3], result)

    def test_large_value_constraint_100_nodes(self):
        """Test maximum constraint boundaries: 100 nodes filled with 9s (triggering continuous carries)."""
        sol = Solution()
        l1 = self.helper_create_linked_list([9] * 100)
        l2 = self.helper_create_linked_list([9] * 100)
        result = sol.addTwoNumbers(l1, l2)
        
        # Adding 99...9 (100 digits) + 99...9 (100 digits) results in:
        # [8, 9, 9, ..., 9, 1] -> 18 followed by ninety-nine 9s, then 1 (total 101 digits)
        expected = [8] + ([9] * 99) + [1]
        self.assert_linked_lists_equal(expected, result)

if __name__ == '__main__':
    unittest.main()