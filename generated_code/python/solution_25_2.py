from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: if k is 1 or list is empty, no reversal needed
        if not head or k == 1:
            return head
        
        # Dummy node to simplify handling the head of the modified list
        dummy = ListNode(0)
        dummy.next = head
        
        # Pointer to the node immediately before the group to be reversed
        group_prev = dummy
        
        while True:
            # Find the k-th node from group_prev
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    break
            
            # If there are fewer than k nodes left, we are done
            if not kth:
                break
                
            # Track the node right after the current k-group
            group_next = kth.next
            
            # Reverse the current k-group. 
            # prev starts at group_next to seamlessly connect the tail of the
            # reversed group to the remaining part of the list.
            prev, curr = group_next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # The original head of the group is now the tail.
            # Connect the previous group's tail to the new head of this reversed group.
            temp = group_prev.next
            group_prev.next = kth
            
            # Move group_prev to the tail of the current reversed group
            group_prev = temp
            
        return dummy.next