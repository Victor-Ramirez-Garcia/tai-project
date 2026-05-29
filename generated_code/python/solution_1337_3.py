import random

class SkiplistNode:
    def __init__(self, val: int, levels: int):
        self.val = val
        # next[i] stores the forward pointer at level i
        self.next = [None] * levels

class Skiplist:
    """
    Skiplist implementation using a probabilistic multi-level linked list.
    Average Time Complexity: O(log N) for search, add, and erase operations.
    Space Complexity: O(N) average space.
    """
    def __init__(self):
        self.max_level = 16  # Reasonable maximum level bound for the expected constraints
        self.p = 0.5         # Probability factor for coin flips determining node height
        # Sentinel head node containing minimum possible value, spanning max_level levels
        self.head = SkiplistNode(-1, self.max_level)
        self.level = 1       # Current highest non-empty level in the skiplist

    def _random_level(self) -> int:
        """Returns a random level for a new node using a geometric distribution."""
        lvl = 1
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        # Traverse downwards from the highest level to level 0
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        
        # Check if the next node at the base level contains the target
        curr = curr.next[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        # update array keeps track of the node at each level where the new node will follow
        update = [None] * self.max_level
        curr = self.head
        
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
            
        lvl = self._random_level()
        # If the random level exceeds current highest level, extend the update array reference
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl
            
        # Create the new node and insert it across its designated levels
        new_node = SkiplistNode(num, lvl)
        for i in range(lvl):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.max_level
        curr = self.head
        
        # Locate the predecessor nodes for the target across all levels
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
            
        curr = curr.next[0]
        # If the target element is not present, return False
        if curr is None or curr.val != num:
            return False
            
        # Unlink the node from all levels it populates
        for i in range(self.level):
            if update[i].next[i] != curr:
                break
            update[i].next[i] = curr.next[i]
            
        # Shrink the level of the skiplist if the highest levels became empty
        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1
            
        return True