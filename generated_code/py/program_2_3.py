# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Algorithmic Strategy: Two Pointers / Linear Traversal
        # Time Complexity: O(max(N, M)) where N and M are the lengths of l1 and l2. We traverse each list at most once.
        # Space Complexity: O(1) auxiliary space (excluding the output list), as we only use a few pointers.
        
        # Dummy head simplifies the insertion logic for the result linked list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Loop until both lists are exhausted and there is no remaining carry
        while l1 or l2 or carry:
            # Extract values if nodes exist, otherwise default to 0
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate total sum for the current position along with the carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the single-digit result and advance the result list pointer
            current.next = ListNode(total % 10)
            current = current.next
            
            # Advance input list pointers if they are not null
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next