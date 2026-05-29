from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        """
        Algorithm: Dummy Node / Sentinel Node approach.
        Time Complexity: O(N) where N is the number of nodes, as we traverse the list once.
        Space Complexity: O(1) as we modify the linked list in place.
        """
        # Create a dummy node that points to the head. 
        # This simplifies edge cases where the head itself needs to be removed.
        dummy = ListNode(next=head)
        current = dummy
        
        while current.next:
            if current.next.val == val:
                # Bypass the node with the matching value
                current.next = current.next.next
            else:
                # Move to the next node only if we didn't delete a node
                current = current.next
                
        return dummy.next