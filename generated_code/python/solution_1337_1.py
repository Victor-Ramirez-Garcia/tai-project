import random

class SkiplistNode:
    def __init__(self, val: int, levels: int):
        self.val = val
        # next pointers for each layer, from index 0 (bottom) to levels-1 (top)
        self.next = [None] * levels

class Skiplist:
    """
    Skiplist implementation with O(log N) average time complexity for search, add, and erase.
    Space complexity is O(N) on average.
    Uses a probabilistic alternative to balanced trees, maintaining multiple layers of linked lists.
    """
    def __init__(self):
        self.MAX_LEVEL = 16  # 2^16 is 65536, sufficient for the standard constraint size
        self.P = 0.5         # Coin flip probability for increasing level
        # Dummy head node that spans all possible levels
        self.head = SkiplistNode(-1, self.MAX_LEVEL)
        self.level = 1       # Current maximum non-empty level of the skiplist

    def _random_level(self) -> int:
        """Determines the level of a new node using geometric distribution."""
        lvl = 1
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        curr = self.head
        # Traverse from the top level down to the bottom level
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        
        # Move to the bottom level next node to check the exact value
        curr = curr.next[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        # update array stores the nodes where the search path drops down a level
        update = [None] * self.MAX_LEVEL
        curr = self.head
        
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
            
        lvl = self._random_level()
        
        # If the generated level exceeds the current max level, initialize update pointers
        if lvl > self.level:
            for i in range(self.level, lvl):
                update[i] = self.head
            self.level = lvl
            
        # Create the new node and insert it into the levels
        new_node = SkiplistNode(num, lvl)
        for i in range(lvl):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * self.MAX_LEVEL
        curr = self.head
        
        for i in range(self.level - 1, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
            
        # Check if the target node exists at the bottom level
        curr = curr.next[0]
        if curr is None or curr.val != num:
            return False
            
        # Unlink the node from all levels it belongs to
        for i in range(self.level):
            if update[i].next[i] != curr:
                break
            update[i].next[i] = curr.next[i]
            
        # Shrink the skiplist height if the top levels become empty
        while self.level > 1 and self.head.next[self.level - 1] is None:
            self.level -= 1
            
        return True