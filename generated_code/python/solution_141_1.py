from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Using Floyd's Tortoise and Hare algorithm (Two Pointers)
        # Time Complexity: O(N) where N is the number of nodes
        # Space Complexity: O(1) auxiliary space
        
        if not head or not head.next:
            return False
            
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next          # Moves 1 step at a time
            fast = fast.next.next     # Moves 2 steps at a time
            
            # If there is a cycle, the fast pointer will eventually catch up to the slow pointer
            if slow == fast:
                return True
                
        # If fast reaches the end of the list, no cycle exists
        return False