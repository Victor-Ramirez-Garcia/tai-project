# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy head to simplify the linked list construction logic
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        # Loop through both lists until both are exhausted and no carry remains
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for the current position
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the single-digit value
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # Move to the next nodes if they exist
            if l1: l1 = l1.next
            if l2: l2 = l2.next
                
        # Return the actual head of the resulting list (skipping the dummy node)
        return dummy_head.next