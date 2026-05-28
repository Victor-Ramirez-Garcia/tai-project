import unittest
from typing import List, Optional
from solution_2_1 import Solution

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestAddTwoNumbers(unittest.TestCase):
    
    def helper_create_linked_list(self, arr: List[int]) -> Optional[ListNode]:
        """Helper method to convert a Python list into a linked list."""
        if not arr:
            return None
        dummy = ListNode(0)
        current = dummy
        for val in arr:
            current.next = ListNode(val)
            current = current.next
        return dummy.next

    def helper_linked_list_to_list(self, head: Optional[ListNode]) -> List[int]:
        """Helper method to convert a linked list back into a Python list for easy assertion."""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_example_1(self):
        """Test standard case with same lengths and a mid-carry (342 + 465 = 807)."""
        sol = Solution()
        l1 = self.helper_create_linked_list([2, 4, 3])
        l2 = self.helper_create_linked_list([5, 6, 4])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.helper_linked_list_to_list(result), [7, 0, 8])

    def test_example_2(self):
        """Test standard case with single-element zero lists (0 + 0 = 0)."""
        sol = Solution()
        l1 = self.helper_create_linked_list([0])
        l2 = self.helper_create_linked_list([0])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.helper_linked_list_to_list(result), [0])

    def test_example_3(self):
        """Test asymmetric lengths with cascading carries (9999999 + 9999 = 10009998)."""
        sol = Solution()
        l1 = self.helper_create_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.helper_create_linked_list([9, 9, 9, 9])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.helper_linked_list_to_list(result), [8, 9, 9, 9, 0, 0, 0, 1])

    def test_single_digit_with_carry(self):
        """Test single digits that generate a carry resulting in an extra node (5 + 5 = 10)."""
        sol = Solution()
        l1 = self.helper_create_linked_list([5])
        l2 = self.helper_create_linked_list([5])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.helper_linked_list_to_list(result), [0, 1])

    def test_different_lengths_no_carry(self):
        """Test lists of different lengths where no carry occurs (123 + 4000 = 4123)."""
        sol = Solution()
        l1 = self.helper_create_linked_list([3, 2, 1])
        l2 = self.helper_create_linked_list([0, 0, 0, 4])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.helper_linked_list_to_list(result), [3, 2, 1, 4])

    def test_one_list_is_zero(self):
        """Test adding zero to a multi-digit number (123 + 0 = 123)."""
        sol = Solution()
        l1 = self.helper_create_linked_list([3, 2, 1])
        l2 = self.helper_create_linked_list([0])
        result = sol.addTwoNumbers(l1, l2)
        self.assertEqual(self.helper_linked_list_to_list(result), [3, 2, 1])

    def test_max_constraint_length_all_nines(self):
        """Test extreme boundary constraint with 100 nodes of 9s to ensure scalability and cascading."""
        sol = Solution()
        l1 = self.helper_create_linked_list([9] * 100)
        l2 = self.helper_create_linked_list([1])
        result = sol.addTwoNumbers(l1, l2)
        
        # 999...999 (100 times) + 1 = 1000...000 (100 zeros and a leading 1)
        # Reversed list representation: [0] * 100 followed by [1]
        expected = [0] * 100 + [1]
        self.assertEqual(self.helper_linked_list_to_list(result), expected)

if __name__ == '__main__':
    unittest.main()