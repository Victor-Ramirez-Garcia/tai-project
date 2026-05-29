from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using Floyd's Tortoise and Hare algorithm (Two Pointers)
        # Time Complexity: O(N) where N is the number of nodes
        # Space Complexity: O(1) auxiliary space
        
        slow = head
        fast = head
        
        # Move 'fast' by two steps and 'slow' by one step.
        # When 'fast' reaches the end, 'slow' will be at the middle.
        # For even lengths, this naturally stops at the second middle node.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow