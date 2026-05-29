from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # An iterative approach using a stack to keep track of the path from the root.
        # Time Complexity: O(N) where N is the length of the traversal string.
        # Space Complexity: O(H) where H is the maximum depth (height) of the tree.
        stack: List[TreeNode] = []
        i = 0
        n = len(traversal)
        
        while i < n:
            # Count the number of dashes to determine the depth of the current node
            depth = 0
            while i < n and traversal[i] == '-':
                depth += 1
                i += 1
            
            # Parse the value of the current node
            val = 0
            while i < n and traversal[i].isdigit():
                val = val * 10 + int(traversal[i])
                i += 1
                
            node = TreeNode(val)
            
            # If the stack has more elements than the current depth, 
            # we must pop until the stack size equals the depth.
            # This ensures that stack[-1] will be the parent of the current node.
            while len(stack) > depth:
                stack.pop()
                
            # If the stack is not empty, attach the current node to its parent.
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
                    
            # Push the current node onto the stack as it could be a parent for subsequent nodes
            stack.append(node)
            
        # The root of the reconstructed tree is always the first node pushed into the stack
        return stack[0] if stack else None