from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Algorithm: Two Pointers (In-place modification)
        Time Complexity: O(n) - We visit each node in the linked list exactly once.
        Space Complexity: O(1) - We reuse the existing nodes to build the result list, 
                                 modifying it in-place without extra memory allocation.
        """
        # 'modify' tracks the position where the next summed value will be stored.
        # 'curr' traverses through the rest of the list to calculate the sums.
        modify = head.next
        curr = modify
        
        while curr is not None:
            current_sum = 0
            # Accumulate values until encountering the next 0 node
            while curr and curr.val != 0:
                current_sum += curr.val
                curr = curr.next
            
            # Store the accumulated sum in the 'modify' node
            modify.val = current_sum
            
            # Advance 'curr' past the 0 node to start the next segment
            if curr:
                curr = curr.next
                
            # Link the current modified node to the next segment's modify node
            modify.next = curr
            modify = modify.next
            
        return head.next