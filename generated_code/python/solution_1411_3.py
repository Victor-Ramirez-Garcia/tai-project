from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """
        Algorithm: Bitwise Shift / Horner's Method
        Time Complexity: O(N) where N is the number of nodes. We traverse the list exactly once.
        Space Complexity: O(1) as we only use a single integer variable to store the result.
        
        Since the most significant bit is at the head, each time we move to the next node,
        we can shift our current result to the left by 1 (equivalent to multiplying by 2)
        and then add the current node's value using a bitwise OR operation.
        """
        ans = 0
        current = head
        
        while current:
            # Shift the current value to the left and add the new bit
            ans = (ans << 1) | current.val
            current = current.next
            
        return ans