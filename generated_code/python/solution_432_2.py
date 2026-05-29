from typing import Set

class Node:
    """
    A node in the doubly linked list representing a specific frequency bucket.
    Each node stores its frequency and a set of keys that have this frequency.
    """
    def __init__(self, count: int):
        self.count: int = count
        self.keys: Set[str] = set()
        self.prev: 'Node' = None
        self.next: 'Node' = None

class AllOne:
    """
    AllOne data structure designed to perform all operations (inc, dec, getMaxKey, getMinKey) 
    in O(1) average time complexity using a hash map combined with a doubly linked list.
    """

    def __init__(self):
        # Maps each key to its corresponding Node in the doubly linked list.
        self.key_to_node = {}
        
        # Initialize sentinel head and tail nodes to easily maintain min/max boundaries.
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node: Node, prev_node: Node) -> None:
        """Helper to insert a new node immediately after an existing node."""
        new_node.prev = prev_node
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        prev_node.next = new_node

    def _remove_node(self, node: Node) -> None:
        """Helper to remove a node from the doubly linked list."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key in self.key_to_node:
            current_node = self.key_to_node[key]
            next_count = current_node.count + 1
            
            # Check if a node with the incremented frequency already exists
            if current_node.next == self.tail or current_node.next.count != next_count:
                new_node = Node(next_count)
                self._add_node_after(new_node, current_node)
            
            target_node = current_node.next
            target_node.keys.add(key)
            self.key_to_node[key] = target_node
            
            # Clean up the key from its old frequency bucket
            current_node.keys.remove(key)
            if not current_node.keys:
                self._remove_node(current_node)
        else:
            # The key is completely new, it should go to a node with count 1
            if self.head.next == self.tail or self.head.next.count != 1:
                new_node = Node(1)
                self._add_node_after(new_node, self.head)
                
            target_node = self.head.next
            target_node.keys.add(key)
            self.key_to_node[key] = target_node

    def dec(self, key: str) -> None:
        # It is guaranteed that key exists in the data structure before decrement
        current_node = self.key_to_node[key]
        next_count = current_node.count - 1
        
        # Clean up the key from its current frequency bucket
        current_node.keys.remove(key)
        
        if next_count == 0:
            del self.key_to_node[key]
        else:
            # Check if a node with the decremented frequency already exists
            if current_node.prev == self.head or current_node.prev.count != next_count:
                new_node = Node(next_count)
                # Insert the new node before current_node (after current_node.prev)
                self._add_node_after(new_node, current_node.prev)
                
            target_node = current_node.prev
            target_node.keys.add(key)
            self.key_to_node[key] = target_node
            
        # Delete the empty node to maintain consistent min/max tracking
        if not current_node.keys:
            self._remove_node(current_node)

    def getMaxKey(self) -> str:
        # The node closest to the tail contains the highest frequencies
        if self.tail.prev == self.head:
            return ""
        # Accessing any arbitrary element from the set in O(1) time
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        # The node closest to the head contains the lowest frequencies
        if self.head.next == self.tail:
            return ""
        # Accessing any arbitrary element from the set in O(1) time
        return next(iter(self.head.next.keys))