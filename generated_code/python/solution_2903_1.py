from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # If the list is empty or has only one node, no adjacent pairs exist.
        if not head or not head.next:
            return head
        
        # Use a pointer to traverse the list and inspect adjacent pairs.
        curr = head
        while curr and curr.next:
            # Calculate the GCD of the current node and the next node.
            gcd_val = math.gcd(curr.val, curr.next.val)
            
            # Create the new node to insert.
            new_node = ListNode(gcd_val)
            
            # Insert new_node between curr and curr.next.
            new_node.next = curr.next
            curr.next = new_node
            
            # Move the pointer past the newly inserted node to the original next node.
            curr = new_node.next
            
        return head