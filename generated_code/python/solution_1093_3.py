from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        n = len(traversal)
        
        while i < n:
            # 1. Count the number of dashes to determine the depth of the current node
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # 2. Extract the integer value of the current node
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(val)
            
            # 3. Maintain the stack so its size matches the required depth.
            # If the stack size is greater than the depth, it means we are backtracking
            # up the tree, so we pop elements that are no longer parents of the current node.
            while len(stack) > depth:
                stack.pop()
            
            # 4. Attach the node to its parent.
            # If the stack is not empty, the top of the stack is the parent.
            if stack:
                parent = stack[-1]
                # Since we always try to populate the left child first, if left is free,
                # we assign it there. Otherwise, it goes to the right child.
                if not parent.left:
                    parent.left = node
                else:
                    parent.right = node
            
            # 5. Push the current node onto the stack as a potential parent for future nodes
            stack.append(node)
            
        # The first element in the stack will always be the root of the tree
        return stack[0] if stack else None