# Necessary imports for type hinting and data structures
from typing import Optional

class ListNode:
    """Definition for a doubly-linked list node."""
    def __init__(self, val: int = 0):
        self.val = val
        self.next: Optional[ListNode] = None
        self.prev: Optional[ListNode] = None

class MyLinkedList:
    """
    Implementation of a doubly-linked list with sentinel head and tail nodes.
    Using a doubly-linked list with pseudo-head and pseudo-tail simplifies boundary conditions,
    allowing O(1) insertions at head/tail and efficient O(min(index, size - index)) lookups and modifications.
    """
    def __init__(self):
        self.size = 0
        # Sentinel (dummy) nodes to simplify edge cases (empty list operations)
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        # Check for out-of-bounds indices
        if index < 0 or index >= self.size:
            return -1
        
        # Optimize search direction based on which end is closer
        if index + 1 < self.size - index:
            curr = self.head
            for _ in range(index + 1):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(self.size - index):
                curr = curr.prev
                
        return curr.val

    def addAtHead(self, val: int) -> None:
        # Add node immediately after the sentinel head
        pred, succ = self.head, self.head.next
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, val: int) -> None:
        # Add node immediately before the sentinel tail
        pred, succ = self.tail.prev, self.tail
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        # If index is greater than the length, the node will not be inserted.
        if index > self.size:
            return
        # If index is negative, the node will be inserted at the head.
        if index < 0:
            index = 0
            
        # Find predecessor and successor of the node to be inserted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            pred = succ.prev
            
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def deleteAtIndex(self, index: int) -> None:
        # Check for out-of-bounds indices
        if index < 0 or index >= self.size:
            return
        
        # Find predecessor and successor of the node to be deleted
        if index < self.size - index:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - index - 1):
                succ = succ.prev
            pred = succ.prev.prev
            
        self.size -= 1
        pred.next = succ
        succ.prev = pred