import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # We use a standard Preorder Traversal (DFS) to serialize the tree.
        # This keeps the logic simple and ensures linear O(N) time complexity.
        vals = []
        
        def dfs(node):
            if not node:
                vals.append("#") # Use '#' as a placeholder for null nodes
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return ",".join(vals) # Join with a delimiter to handle multi-digit/negative numbers

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # Split the string by the delimiter to get our tokens
        vals = data.split(",")
        # Use an iterator or collections.deque for efficient O(1) popping from the front
        queue = collections.deque(vals)
        
        def dfs():
            if not queue:
                return None
            
            val = queue.popleft()
            if val == "#":
                return None
            
            # Create the current node and reconstruct left and right subtrees recursively
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))