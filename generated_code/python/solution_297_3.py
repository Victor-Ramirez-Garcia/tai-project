from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    Algorithm: Preorder Traversal (DFS)
    
    Time Complexity: 
      - serialize: O(N) where N is the number of nodes, as we visit each node once.
      - deserialize: O(N) since we process each split token exactly once.
    Space Complexity:
      - serialize: O(N) to store the call stack and the resulting string pieces.
      - deserialize: O(N) to store the list of tokens and the recursion stack.
    """

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        vals = []
        
        def dfs(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Split the serialized string into an iterable queue of tokens
        tokens = deque(data.split(","))
        
        def dfs():
            if not tokens:
                return None
            
            val = tokens.popleft()
            if val == "#":
                return None
            
            # Reconstruct the current node and its subtrees sequentially
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))