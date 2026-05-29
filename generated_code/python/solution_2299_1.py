from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Since the head is guaranteed to have val == 0, we can use the original
        # list nodes to store the sums in-place, achieving O(1) auxiliary space.
        
        # 'modify' tracks the node where we will store the current block's sum.
        # 'curr' is used to traverse through the linked list.
        modify = head.next
        curr = modify
        
        while curr is not None:
            current_sum = 0
            
            # Accumulate the values of nodes between the consecutive 0s.
            while curr is not None and curr.val != 0:
                current_sum += curr.val
                curr = curr.next
            
            # Store the accumulated sum into the 'modify' node.
            modify.val = current_sum
            
            # Move 'curr' to the node after the current '0' to start the next segment.
            curr = curr.next
            
            # Link the current 'modify' node to the next segment's sum node.
            # If 'curr' is None, it means we've reached the end of the list.
            modify.next = curr
            
            # Move the 'modify' pointer forward for the next iteration.
            modify = modify.next
            
        # The head of the modified list is the first node after the original 0 node.
        return head.next