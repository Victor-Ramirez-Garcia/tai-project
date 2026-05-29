import math
from typing import Optional

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
        
        # Use a single pointer to traverse the list and inspect adjacent pairs.
        # Time Complexity: O(N * log(min(A, B))) where N is the number of nodes.
        # Space Complexity: O(1) auxiliary space (ignoring the newly created nodes).
        curr = head
        while curr and curr.next:
            # Calculate the GCD of the current node and the next node
            gcd_val = math.gcd(curr.val, curr.next.val)
            
            # Create the new node with the GCD value
            new_node = ListNode(val=gcd_val, next=curr.next)
            
            # Insert the new node between curr and curr.next
            curr.next = new_node
            
            # Move the pointer past the inserted node to the original next node
            curr = new_node.next
            
        return head