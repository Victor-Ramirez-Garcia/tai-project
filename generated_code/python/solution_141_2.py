from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity: O(N) - In the worst case, we traverse each node at most twice.
        # Space Complexity: O(1) - Only two pointers are used, achieving constant memory.
        # Algorithm: Floyd's Tortoise and Hare (Two Pointers).
        
        # Edge case: An empty list or a list with only one node cannot have a cycle.
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        # Move 'slow' by 1 step and 'fast' by 2 steps.
        # If there's a cycle, the fast pointer will eventually catch up to the slow pointer.
        # If there's no cycle, the fast pointer will reach the end of the list.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If the two pointers meet, a cycle exists.
            if slow == fast:
                return True
                
        return False