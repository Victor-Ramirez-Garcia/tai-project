from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """
        Time Complexity: O(N) where N is the number of nodes in the linked list.
        Space Complexity: O(1) auxiliary space as we only use a single integer.
        
        Algorithm:
        Since the head represents the most significant bit, we can iterate through 
        the linked list from left to right. For each node, we shift our accumulated 
        result to the left by 1 bit (equivalent to multiplying by 2) and add the 
        current node's value using a bitwise OR operation.
        """
        ans = 0
        current = head
        
        while current:
            # Shift the current answer left by 1 and bitwise OR with the new bit
            ans = (ans << 1) | current.val
            current = current.next
            
        return ans