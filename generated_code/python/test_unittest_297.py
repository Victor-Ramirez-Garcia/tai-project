import os
import importlib.util
import unittest

# Dynamic loading of the solution module as mandated by guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)

# Retrieve classes from the dynamically loaded module
Codec = sol_module.Codec
# Fallback to definition if TreeNode isn't exposed directly, though it's typically present
TreeNode = getattr(sol_module, 'TreeNode', None)

if TreeNode is None:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

class TestCodec(unittest.TestCase):

    def assert_tree_equal(self, t1, t2):
        """Helper method to deeply compare two binary trees."""
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            self.fail("Trees are not structurally identical (one is None, the other is not).")
        self.assertEqual(t1.val, t2.val, f"Node values differ: {t1.val} != {t2.val}")
        self.assert_tree_equal(t1.left, t2.left)
        self.assert_tree_equal(t1.right, t2.right)

    def test_example_1_standard_tree(self):
        """Tests standard binary tree from Example 1: [1,2,3,null,null,4,5]"""
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)

        codec = Codec()
        serialized_str = codec.serialize(root)
        
        self.assertIsInstance(serialized_str, str, "Serialization output must be a string.")
        
        deserialized_root = codec.deserialize(serialized_str)
        self.assert_tree_equal(root, deserialized_root)

    def test_example_2_empty_tree(self):
        """Tests an empty tree (edge case of minimum node constraint: 0 nodes)."""
        root = None

        codec = Codec()
        serialized_str = codec.serialize(root)
        
        self.assertIsInstance(serialized_str, str, "Serialization output must be a string.")
        
        deserialized_root = codec.deserialize(serialized_str)
        self.assertIsNone(deserialized_root, "Deserialized tree from an empty tree should be None.")

    def test_single_node_tree(self):
        """Tests a tree consisting of only a single root node."""
        root = TreeNode(42)

        codec = Codec()
        serialized_str = codec.serialize(root)
        deserialized_root = codec.deserialize(serialized_str)
        
        self.assert_tree_equal(root, deserialized_root)

    def test_skewed_left_tree_boundary_values(self):
        """Tests a deeply skewed left tree incorporating extreme node value constraints (-1000)."""
        root = TreeNode(-1000)
        root.left = TreeNode(-500)
        root.left.left = TreeNode(0)

        codec = Codec()
        serialized_str = codec.serialize(root)
        deserialized_root = codec.deserialize(serialized_str)
        
        self.assert_tree_equal(root, deserialized_root)

    def test_skewed_right_tree_boundary_values(self):
        """Tests a deeply skewed right tree incorporating extreme node value constraints (1000)."""
        root = TreeNode(1000)
        root.right = TreeNode(500)
        root.right.right = TreeNode(1)

        codec = Codec()
        serialized_str = codec.serialize(root)
        deserialized_root = codec.deserialize(serialized_str)
        
        self.assert_tree_equal(root, deserialized_root)

    def test_duplicate_values_in_tree(self):
        """Tests a tree where multiple nodes share identical values."""
        root = TreeNode(7)
        root.left = TreeNode(7)
        root.right = TreeNode(7)
        root.left.left = TreeNode(7)

        codec = Codec()
        serialized_str = codec.serialize(root)
        deserialized_root = codec.deserialize(serialized_str)
        
        self.assert_tree_equal(root, deserialized_root)

if __name__ == "__main__":
    unittest.main()