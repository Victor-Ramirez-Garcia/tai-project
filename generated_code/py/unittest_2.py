import unittest
from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Implementation placeholder for testing
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            total = val1 + val2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next

class TestAddTwoNumbers(unittest.TestCase):
    
    # Helper methods to convert between python lists and linked lists
    def to_linked_list(self, arr: List[int]) -> Optional[ListNode]:
        if not arr:
            return None
        dummy = ListNode(0)
        curr = dummy
        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def to_python_list(self, head: Optional[ListNode]) -> List[int]:
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr

    def assertLinkedListEqual(self, l1: Optional[ListNode], l2_arr: List[int]):
        self.assertEqual(self.to_python_list(l1), l2_arr)

    # --- Example Test Cases ---
    
    def test_example_1(self):
        """Test with l1 = [2,4,3] and l2 = [5,6,4] -> [7,0,8]"""
        l1 = self.to_linked_list([2, 4, 3])
        l2 = self.to_linked_list([5, 6, 4])
        sol = Solution()
        result = sol.addTwoNumbers(l1, l2)
        self.assertLinkedListEqual(result, [7, 0, 8])

    def test_example_2(self):
        """Test with l1 = [0] and l2 = [0] -> [0]"""
        l1 = self.to_linked_list([0])
        l2 = self.to_linked_list([0])
        sol = Solution()
        result = sol.addTwoNumbers(l1, l2)
        self.assertLinkedListEqual(result, [0])

    def test_example_3(self):
        """Test with different lengths and multiple carries: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]"""
        l1 = self.to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = self.to_linked_list([9, 9, 9, 9])
        sol = Solution()
        result = sol.addTwoNumbers(l1, l2)
        self.assertLinkedListEqual(result, [8, 9, 9, 9, 0, 0, 0, 1])

    # --- Edge Cases & Constraint Tests ---

    def test_single_digit_with_carry(self):
        """Test single digit addition that results in a carry: 5 + 5 = 10 -> [0, 1]"""
        l1 = self.to_linked_list([5])
        l2 = self.to_linked_list([5])
        sol = Solution()
        result = sol.addTwoNumbers(l1, l2)
        self.assertLinkedListEqual(result, [0, 1])

    def test_one_list_longer_no_carry(self):
        """Test where one list is longer and no carry transfers to the extended digits"""
        l1 = self.to_linked_list([1, 2])
        l2 = self.to_linked_list([3, 4, 5, 6])
        sol = Solution()
        result = sol.addTwoNumbers(l1, l2)
        self.assertLinkedListEqual(result, [4, 6, 5, 6])

    def test_one_list_longer_with_carry_propagation(self):
        """Test where carry propagates into the remaining digits of the longer list"""
        l1 = self.to_linked_list([9, 9])
        l2 = self.to_linked_list([1, 0, 0, 4])
        sol = Solution()
        result = sol.addTwoNumbers(l1, l2)
        self.assertLinkedListEqual(result, [0, 0, 1, 4])

    def test_max_length_constraint(self):
        """Test maximum constraint boundary (100 nodes each) filled with max digits"""
        l1 = self.to_linked_list([9] * 100)
        l2 = self.to_linked_list([9] * 100)
        sol = Solution()
        result = sol.addTwoNumbers(l1, l2)
        
        # 99...99 + 99...99 = 199...98
        expected = [8] + ([9] * 99) + [1]
        self.assertLinkedListEqual(result, expected)

if __name__ == '__main__':
    unittest.main()