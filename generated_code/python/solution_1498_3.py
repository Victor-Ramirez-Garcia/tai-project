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
        Algorithm: Simultaneous Tree Traversal (Breadth-First Search / BFS)
        Time Complexity: O(N) where N is the number of nodes in the tree.
        Space Complexity: O(W) where W is the maximum width of the tree (for the BFS queue).
        
        Since we need to find the corresponding node in the cloned tree, we traverse
        both trees simultaneously using the exact same path. When we find the 'target'
        node in the 'original' tree, the current node in the 'cloned' tree is our answer.
        """
        if not original:
            return None
            
        # Initialize queues for simultaneous BFS traversal of both trees
        queue_orig = deque([original])
        queue_clone = deque([cloned])
        
        while queue_orig:
            curr_orig = queue_orig.popleft()
            curr_clone = queue_clone.popleft()
            
            # Check if we have found the target node in the original tree
            # We compare references (curr_orig is target) as per problem description
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