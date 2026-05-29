import math
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case: if the list is empty or has only one node, no insertions are needed.
        if not head or not head.next:
            return head
        
        # Use a single pointer to traverse the list and check adjacent pairs.
        # Time Complexity: O(N * log(min(A, B))) where N is the number of nodes.
        # Space Complexity: O(1) auxiliary space as we modify the list in place.
        curr = head
        while curr and curr.next:
            # Calculate the greatest common divisor of the current and next node values
            gcd_val = math.gcd(curr.val, curr.next.val)
            
            # Create the new node with the GCD value
            gcd_node = ListNode(val=gcd_val)
            
            # Insert gcd_node between curr and curr.next
            gcd_node.next = curr.next
            curr.next = gcd_node
            
            # Move the pointer past the newly inserted node to the original next node
            curr = gcd_node.next
            
        return head