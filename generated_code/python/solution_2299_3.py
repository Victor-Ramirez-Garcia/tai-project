from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Two-pointer in-place approach.
        # Time Complexity: O(N) where N is the number of nodes in the linked list.
        # Space Complexity: O(1) as we modify the existing list nodes in-place.
        
        # 'modify' will track the node where we overwrite the summed values.
        # 'curr' will traverse the list to calculate the sums.
        modify = head.next
        curr = modify
        
        while curr is not None:
            current_sum = 0
            # Accumulate values until we encounter the next 0 node.
            while curr and curr.val != 0:
                current_sum += curr.val
                curr = curr.next
            
            # Overwrite the value of the modify node with the accumulated sum.
            modify.val = current_sum
            
            # Move curr to the node after the 0 node.
            curr = curr.next
            
            # Link the current modified node to the next segment's start node.
            modify.next = curr
            
            # Move the modify pointer forward for the next segment.
            modify = modify.next
            
        return head.next