# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Using the Dummy Head technique to simplify edge case handling for the head node.
        # Time Complexity: O(max(N, M)) where N and M are the lengths of l1 and l2 respectively.
        # Space Complexity: O(max(N, M)) for the new linked list storing the result.
        dummy_head = ListNode(0)
        curr = dummy_head
        carry = 0
        
        # Traverse both lists until both are exhausted and no carry remains
        while l1 or l2 or carry:
            # Extract values, defaulting to 0 if a list has already finished
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the total sum for the current position and update the carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the single-digit result and advance the result pointer
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            # Move to the next nodes in the input lists if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next