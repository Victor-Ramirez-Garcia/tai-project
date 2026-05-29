from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        """
        Algorithm: Simultaneous Breadth-First Search (BFS) / Level-Order Traversal.
        
        Since 'cloned' is an exact copy of 'original', traversing both trees 
        in identical fashion ensures that when we find the 'target' node pointer 
        in the 'original' tree, the corresponding node pointer in the 'cloned' 
        tree is at the exact same position.
        
        Time Complexity: O(N) where N is the number of nodes in the tree, 
                         as we may visit all nodes in the worst case.
        Space Complexity: O(W) where W is the maximum width of the tree, 
                          used by the queues for the level-order traversal.
        """
        # Using deques for efficient O(1) popleft operations
        queue_orig = deque([original])
        queue_clone = deque([cloned])
        
        while queue_orig:
            curr_orig = queue_orig.popleft()
            curr_clone = queue_clone.popleft()
            
            # If we find the reference to the target node in the original tree,
            # return the corresponding node from the cloned tree.
            if curr_orig is target:
                return curr_clone
            
            # Enqueue left children if they exist
            if curr_orig.left:
                queue_orig.append(curr_orig.left)
                queue_clone.append(curr_clone.left)
                
            # Enqueue right children if they exist
            if curr_orig.right:
                queue_orig.append(curr_orig.right)
                queue_clone.append(curr_clone.right)
                
        return None