import random

class SkiplistNode:
    def __init__(self, val: int, levels: int):
        self.val = val
        # next[i] stores the forward pointer at level i
        self.next = [None] * levels

class Skiplist:
    def __init__(self):
        # Maximum height allowed for the skiplist
        self.MAX_LEVEL = 16
        # P-value for the geometric distribution of levels (0.5 is standard)
        self.P = 0.5
        # Sentinel head node with the lowest possible integer value
        self.head = SkiplistNode(-1, self.MAX_LEVEL)
        # Current maximum level of the skiplist containing actual nodes
        self.level = 1

    def _random_level(self) -> int:
        """Generates a random level for a new node using a geometric distribution."""
        lvl = 1
        while random.random() < self.P and lvl < self.MAX_LEVEL:
            lvl += 1
        return lvl

    def search(self, target: int) -> bool:
        """Returns True if the target exists in the skiplist, otherwise False."""
        curr = self.head
        # Traverse from the top level down to level 0
        for i in reversed(range(self.level)):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        
        # Check if the next node at level 0 contains the target
        curr = curr.next[0]
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        """Inserts a value into the skiplist."""
        # update[i] will store the node prior to the insertion point at level i
        update = [None] * self.MAX_LEVEL
        curr = self.head
        
        for i in reversed(range(self.level)):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
            
        # Determine the random level for the new node
        r_level = self._random_level()
        
        # If the new level exceeds the current max level, update the tracked head links
        if r_level > self.level:
            for i in range(self.level, r_level):
                update[i] = self.head
            self.level = r_level
            
        # Create the new node and splice it into the linked lists at all levels
        new_node = SkiplistNode(num, r_level)
        for i in range(r_level):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node

    def erase(self, num: int) -> bool:
        """Removes a value from the skiplist. Returns True if successful."""
        update = [None] * self.MAX_LEVEL
        curr = self.head
        
        for i in reversed(range(self.level)):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
            
        # Move to the potential target node at level 0
        curr = curr.next[0]
        
        # If the target is found, decouple it from all levels it occupies
        if curr and curr.val == num:
            for i in range(self.level):
                if update[i].next[i] != curr:
                    break
                update[i].next[i] = curr.next[i]
                
            # Recalculate the active maximum level if the top level(s) became empty
            while self.level > 1 and self.head.next[self.level - 1] is None:
                self.level -= 1
            return True
            
        return False