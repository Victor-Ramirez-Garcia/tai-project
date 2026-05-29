from typing import Optional

class ListNode:
    """Standard Node definition for a doubly linked list."""
    def __init__(self, val: int):
        self.val = val
        self.prev: Optional['ListNode'] = None
        self.next: Optional['ListNode'] = None

class MyLinkedList:
    """
    Implementation using a Doubly Linked List with sentinel (dummy) nodes.
    Sentinel nodes at the head and tail simplify edge cases for insertion 
    and deletion, as every 'real' node always has a neighbor.
    
    Complexity:
    - get: O(k) where k is the index.
    - addAtHead/Tail: O(1).
    - addAtIndex/deleteAtIndex: O(k).
    - Space: O(n) to store n elements.
    """

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # Sentinel head
        self.tail = ListNode(0)  # Sentinel tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        # Optimization: choose the shortest path (from head or tail)
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
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        
        # Find predecessor and successor of the new node
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


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)