def serialize(self, root):
    """Encodes a tree to a single string.
    
    :type root: TreeNode
    :rtype: str
    """
    # We use a pre-order traversal (DFS) to serialize the tree.
    # This is optimal in terms of both time and space complexity O(N).
    vals = []
    
    def doit(node):
        if node:
            vals.append(str(node.val))
            doit(node.left)
            doit(node.right)
        else:
            vals.append('#') # Use '#' to denote a null node
            
    doit(root)
    return ','.join(vals)

def deserialize(self, data):
    """Decodes your encoded data to tree.
    
    :type data: str
    :rtype: TreeNode
    """
    # Split the serialized string into an iterator of values.
    # An iterator allows us to consume elements sequentially across recursive calls.
    vals = iter(data.split(','))
    
    def doit():
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = doit()
        node.right = doit()
        return node
        
    return doit()