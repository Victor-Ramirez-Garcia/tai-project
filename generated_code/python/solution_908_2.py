from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using Floyd's Tortoise and Hare algorithm (Two Pointers).
        # Time Complexity: O(N) where N is the number of nodes in the linked list.
        # Space Complexity: O(1) as we only use two pointers.
        slow = head
        fast = head
        
        # Move 'fast' by two steps and 'slow' by one step.
        # When 'fast' reaches the end, 'slow' will be at the middle.
        # This naturally handles both odd and even lengths, returning the
        # second middle node for even lengths due to the fast.next check.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow