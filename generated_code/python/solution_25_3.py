from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Time Complexity: O(N) where N is the number of nodes in the linked list. 
        # Each node is processed at most twice (once to count/check, once to reverse).
        # Space Complexity: O(1) auxiliary space as we modify pointers in place.
        
        # Base case: if list is empty or k is 1, no reversal needed.
        if not head or k == 1:
            return head
        
        # Use a dummy node to simplify handling the new head of the list.
        dummy = ListNode(0)
        dummy.next = head
        
        # group_prev will always point to the node just before the current k-group.
        group_prev = dummy
        
        while True:
            # Check if there are at least k nodes left to reverse.
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    # Fewer than k nodes remaining, leave them as is and finish.
                    return dummy.next
            
            # Store the connection to the next group before reversing.
            group_next = kth.next
            
            # Reverse the current k-group.
            # prev starts at group_next so the tail of the reversed group connects to the next group.
            prev = group_next
            curr = group_prev.next
            
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            # group_prev.next currently points to the old head of this group (which is now the tail).
            # We save it to become the next group_prev after updating connections.
            new_group_prev = group_prev.next
            
            # Connect the previous part of the list to the new head of the reversed group.
            group_prev.next = kth
            
            # Move group_prev to the tail of the current reversed group.
            group_prev = new_group_prev