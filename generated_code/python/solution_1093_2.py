from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        """
        Algorithm: Iterative Preorder Simulation using a Stack
        Time Complexity: O(N) where N is the length of the traversal string. 
                         Each character is processed a constant number of times.
        Space Complexity: O(H) where H is the maximum depth of the tree (stack size).
                          In the worst case, H can be equal to the number of nodes.
        """
        stack: List[TreeNode] = []
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
            
            # 3. Maintain the stack so its size matches the required depth of the current node.
            # If the stack size is greater than the depth, it means we have finished processing 
            # the current subtree, so we pop elements until we reach the parent level.
            while len(stack) > depth:
                stack.pop()
                
            # 4. Attach the node to its parent.
            # Preorder traversal ensures the left child is always populated before the right child.
            if stack:
                if not stack[-1].left:
                    stack[-1].left = node
                else:
                    stack[-1].right = node
                    
            # 5. Push the current node onto the stack as a potential parent for subsequent nodes
            stack.append(node)
            
        # The root of the reconstructed tree will always be the first element in the stack
        return stack[0] if stack else None