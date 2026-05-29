from typing import Dict, Set

class Node:
    """
    A node in the doubly linked list.
    Each node represents a specific frequency/count and contains all keys with that count.
    """
    def __init__(self, count: int):
        self.count: int = count
        self.keys: Set[str] = set()
        self.prev: 'Node' = None
        self.next: 'Node' = None

class AllOne:
    """
    Design a data structure supporting inc, dec, getMaxKey, getMinKey in O(1) average time.
    Algorithm: Doubly Linked List of frequency nodes + Hash Map mapping keys to their nodes.
    """
    def __init__(self):
        # Maps each key to its corresponding Node in the doubly linked list
        self.key_to_node: Dict[str, Node] = {}
        
        # Sentinel head and tail for the doubly linked list to avoid edge cases
        self.head: Node = Node(0)
        self.tail: Node = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_node_after(self, new_node: Node, base_node: Node) -> None:
        """Helper to insert new_node right after base_node."""
        new_node.prev = base_node
        new_node.next = base_node.next
        base_node.next.prev = new_node
        base_node.next = new_node

    def _remove_node_if_empty(self, node: Node) -> None:
        """Helper to remove a node from the linked list if it contains no keys."""
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_to_node:
            # Key is new, initial count should be 1
            first_node = self.head.next
            if first_node == self.tail or first_node.count > 1:
                # Node with count 1 doesn't exist, create it
                new_node = Node(1)
                self._insert_node_after(new_node, self.head)
                first_node = new_node
            
            first_node.keys.add(key)
            self.key_to_node[key] = first_node
        else:
            # Key exists, increment its count
            curr_node = self.key_to_node[key]
            next_node = curr_node.next
            
            if next_node == self.tail or next_node.count > curr_node.count + 1:
                # Node with count + 1 doesn't exist, create it
                new_node = Node(curr_node.count + 1)
                self._insert_node_after(new_node, curr_node)
                next_node = new_node
                
            next_node.keys.add(key)
            self.key_to_node[key] = next_node
            
            curr_node.keys.remove(key)
            self._remove_node_if_empty(curr_node)

    def dec(self, key: str) -> None:
        # It is guaranteed that key exists before decrementing
        curr_node = self.key_to_node[key]
        prev_node = curr_node.prev
        
        if curr_node.count == 1:
            # If count becomes 0, remove the key entirely
            del self.key_to_node[key]
        else:
            if prev_node == self.head or prev_node.count < curr_node.count - 1:
                # Node with count - 1 doesn't exist, create it
                new_node = Node(curr_node.count - 1)
                self._insert_node_after(new_node, prev_node)
                prev_node = new_node
                
            prev_node.keys.add(key)
            self.key_to_node[key] = prev_node
            
        curr_node.keys.remove(key)
        self._remove_node_if_empty(curr_node)

    def getMaxKey(self) -> str:
        # The maximal count node is always just before the tail sentinel
        if self.tail.prev == self.head:
            return ""
        # Return any key from the set
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        # The minimal count node is always just after the head sentinel
        if self.head.next == self.tail:
            return ""
        # Return any key from the set
        return next(iter(self.head.next.keys))