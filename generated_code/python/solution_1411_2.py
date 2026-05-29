from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        # Time Complexity: O(N) where N is the number of nodes in the linked list.
        # Space Complexity: O(1) as we only use a single variable to accumulate the result.
        
        ans = 0
        current = head
        
        while current:
            # Shift the existing bits to the left by 1 (equivalent to multiplying by 2)
            # and add the current node's value using the bitwise OR operator.
            ans = (ans << 1) | current.val
            current = current.next
            
        return ans