from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Time Complexity: O(N) - In the worst case, we traverse each node once (no cycle) 
        # or proportional to the cycle length (with cycle).
        # Space Complexity: O(1) - Only two pointers are used, achieving constant memory.
        # Algorithm: Floyd's Tortoise and Hare (Two Pointers).
        
        # Edge case: An empty list or a list with only one node cannot have a cycle.
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        # Move fast by two steps and slow by one step.
        # If there is a cycle, they will eventually meet.
        # If there is no cycle, fast or fast.next will reach None.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If the pointers meet, a cycle exists.
            if slow == fast:
                return True
                
        return False