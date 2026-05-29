from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Algorithm: Two Pointers (Fast and Slow)
        # Time Complexity: O(N) where N is the number of nodes in the linked list.
        # Space Complexity: O(1) as we only use two pointers.
        
        slow = head
        fast = head
        
        # Move 'fast' two steps and 'slow' one step at a time.
        # When 'fast' reaches the end, 'slow' will be at the middle.
        # This naturally handles the second middle node for even lengths due to the fast.next check.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow