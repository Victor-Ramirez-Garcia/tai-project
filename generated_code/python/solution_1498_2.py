from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    """
    Algorithm: Parallel Depth First Search (DFS)
    
    Time Complexity: O(N) where N is the number of nodes in the tree, 
    as we might need to visit every node in the worst case.
    
    Space Complexity: O(H) where H is the height of the tree, representing
    the recursion stack. In the worst case (skewed tree), H = N.
    
    Choice: DFS is idiomatic and concise for tree traversal. Since we need to 
    find a specific node in a copy, we traverse both trees simultaneously. 
    When we find the reference 'target' in the 'original' tree, the current 
    node in 'cloned' is our result.
    """
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        # Base case: if we reach a null node, the target is not in this path
        if not original:
            return None
        
        # Check if the current node in the original tree is the target reference
        # Note: We use 'is' for reference equality as per problem constraints
        if original is target:
            return cloned
        
        # Recurse on the left subtree
        left_result = self.getTargetCopy(original.left, cloned.left, target)
        if left_result:
            return left_result
        
        # Recurse on the right subtree if not found in the left
        return self.getTargetCopy(original.right, cloned.right, target)