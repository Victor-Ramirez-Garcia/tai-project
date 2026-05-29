from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Using a dummy node simplifies edge cases where the head itself needs to be removed.
        # Time Complexity: O(N) where N is the number of nodes, as we visit each node exactly once.
        # Space Complexity: O(1) auxiliary space, as we only modify pointers in place.
        dummy = ListNode(next=head)
        current = dummy
        
        while current.next:
            if current.next.val == val:
                # Bypass the node that matches the target value
                current.next = current.next.next
            else:
                # Advance the pointer only if we didn't remove a node
                current = current.next
                
        return dummy.next