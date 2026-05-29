from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Time Complexity: O(N) where N is the number of nodes in the linked list. 
                         Each node is processed at most twice (once to count/find the k-th node, once to reverse).
        Space Complexity: O(1) auxiliary space as we reverse the nodes in-place using pointers.
        """
        if not head or k == 1:
            return head
        
        # Dummy node to simplify handling the new head of the list
        dummy = ListNode(0)
        dummy.next = head
        
        # Pointers to track the end of the previous reversed group and the current segment
        group_prev = dummy
        
        while True:
            # Check if there are at least k nodes left to reverse
            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break
                
            # Store the connection to the next group
            group_next = kth.next
            
            # Reverse the current group of k nodes
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                
            # Re-link the reversed group back into the main list
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp
            
        return dummy.next

    def get_kth_node(self, curr: Optional[ListNode], k: int) -> Optional[ListNode]:
        """Helper function to find the k-th node from the current position."""
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr