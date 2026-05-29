# Optimal Doubly Linked List implementation with dummy head and tail for O(1) operations at bounds
# and simplified insertion/deletion logic.

class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initializes the MyLinkedList object using sentinel/dummy nodes.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        self.size = 0
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node. Returns -1 if invalid.
        Optimized by choosing to traverse from head or tail depending on index proximity.
        Time Complexity: O(min(index, size - index)) -> O(N) worst-case
        Space Complexity: O(1)
        """
        if index < 0 or index >= self.size:
            return -1
        
        # Traverse from head if index is in the first half, else from tail
        if index < self.size // 2:
            curr = self.head.next
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail.prev
            for _ in range(self.size - 1 - index):
                curr = curr.prev
                
        return curr.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        pred, succ = self.head, self.head.next
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val as the last element.
        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        pred, succ = self.tail.prev, self.tail
        
        self.size += 1
        to_add = ListNode(val)
        to_add.prev = pred
        to_add.next = succ
        pred.next = to_add
        succ.prev = to_add

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node. 
        If index equals length, append to end. If index > length, do nothing.
        Time Complexity: O(min(index, size - index)) -> O(N)
        Space Complexity: O(1)
        """
        if index > self.size:
            return
        if index < 0:
            index = 0
            
        # Find predecessor and successor of the node to be added
        if index < self.size // 2:
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
        """
        Delete the index-th node, if the index is valid.
        Time Complexity: O(min(index, size - index)) -> O(N)
        Space Complexity: O(1)
        """
        if index < 0 or index >= self.size:
            return
            
        # Find predecessor and successor of the node to be deleted
        if index < self.size // 2:
            pred = self.head
            for _ in range(index):
                pred = pred.next
            succ = pred.next.next
        else:
            succ = self.tail
            for _ in range(self.size - 1 - index):
                succ = succ.prev
            pred = succ.prev.prev
            
        self.size -= 1
        pred.next = succ
        succ.prev = pred