# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Using a dummy head simplifies the logic of managing the head node of the new list.
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        # Traverse both lists until we exhaust both and process any remaining carry.
        # Time Complexity: O(max(N, M)) where N and M are lengths of l1 and l2.
        # Space Complexity: O(max(N, M)) for the output list.
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and updated carry
            total_sum = val1 + val2 + carry
            carry = total_sum // 10
            
            # Create a new node with the current digit and move the pointer
            curr.next = ListNode(total_sum % 10)
            curr = curr.next
            
            # Advance the list pointers if nodes are available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next