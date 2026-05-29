from typing import Set, Dict

class Node:
    """
    A doubly linked list node that stores a count and a set of keys with that count.
    This allows O(1) insertion, deletion, and access to the min/max elements.
    """
    def __init__(self, count: int):
        self.count = count
        self.keys: Set[str] = set()
        self.prev: 'Node' = None
        self.next: 'Node' = None

class AllOne:
    """
    Algorithm: Doubly Linked List + Hash Map
    - The Hash Map stores the mapping from 'key' to its corresponding 'Node' in the linked list.
    - The Doubly Linked List stores nodes sorted by count.
    - Each Node contains a set of keys that share the same frequency.
    - Time Complexity: O(1) for all operations.
    - Space Complexity: O(N) where N is the number of unique strings.
    """

    def __init__(self):
        # Sentinel nodes for the doubly linked list to simplify insertion/deletion logic
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # Maps key -> Node
        self.key_map: Dict[str, Node] = {}

    def _add_node_after(self, new_node: Node, prev_node: Node) -> Node:
        """Inserts a new_node immediately after prev_node."""
        next_node = prev_node.next
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        next_node.prev = new_node
        return new_node

    def _remove_node_if_empty(self, node: Node) -> None:
        """Removes a node from the linked list if it no longer contains any keys."""
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def inc(self, key: str) -> None:
        if key not in self.key_map:
            # Case 1: Key is new, target count is 1
            first_node = self.head.next
            if first_node == self.tail or first_node.count > 1:
                # Create a new node for count 1 if it doesn't exist
                new_node = self._add_node_after(Node(1), self.head)
            else:
                new_node = first_node
            new_node.keys.add(key)
            self.key_map[key] = new_node
        else:
            # Case 2: Key exists, move from current count node to count + 1 node
            curr_node = self.key_map[key]
            next_node = curr_node.next
            if next_node == self.tail or next_node.count > curr_node.count + 1:
                # Create a new node for count + 1 if it doesn't exist
                next_node = self._add_node_after(Node(curr_node.count + 1), curr_node)
            
            next_node.keys.add(key)
            self.key_map[key] = next_node
            curr_node.keys.remove(key)
            self._remove_node_if_empty(curr_node)

    def dec(self, key: str) -> None:
        # Guaranteed that key exists per constraints
        curr_node = self.key_map[key]
        curr_node.keys.remove(key)
        
        if curr_node.count == 1:
            # If count becomes 0, remove the key from the structure entirely
            del self.key_map[key]
        else:
            # Move key to count - 1 node
            prev_node = curr_node.prev
            if prev_node == self.head or prev_node.count < curr_node.count - 1:
                # Create a new node for count - 1 if it doesn't exist
                prev_node = self._add_node_after(Node(curr_node.count - 1), curr_node.prev)
            
            prev_node.keys.add(key)
            self.key_map[key] = prev_node
            
        self._remove_node_if_empty(curr_node)

    def getMaxKey(self) -> str:
        # Maximum count is stored at the tail's predecessor
        if self.tail.prev == self.head:
            return ""
        # Return any key from the set (O(1) in Python to get an iterator item)
        return next(iter(self.tail.prev.keys))

    def getMinKey(self) -> str:
        # Minimum count is stored at the head's successor
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))