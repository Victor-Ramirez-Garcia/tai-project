import os
import importlib.util
import unittest

# Dynamic loading setup as per instructions
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

# We assume TreeNode is defined in the solution module or accessible from it.
# If not, we define a compatible TreeNode helper for test construction.
TreeNode = getattr(sol_module, 'TreeNode', None)
if TreeNode is None:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None

class TestGetTargetCopy(unittest.TestCase):
    
    def _find_node_by_val(self, root: TreeNode, val: int) -> TreeNode:
        """Helper method to find a node by value to set up target references."""
        if not root:
            return None
        if root.val == val:
            return root
        left_res = self._find_node_by_val(root.left, val)
        if left_res:
            return left_res
        return self._find_node_by_val(root.right, val)

    def test_example_1(self):
        # tree = [7,4,3,null,null,6,19], target = 3
        
        # Original Tree
        orig = TreeNode(7)
        orig.left = TreeNode(4)
        orig.right = TreeNode(3)
        orig.right.left = TreeNode(6)
        orig.right.right = TreeNode(19)
        
        # Cloned Tree
        cloned = TreeNode(7)
        cloned.left = TreeNode(4)
        cloned.right = TreeNode(3)
        cloned.right.left = TreeNode(6)
        cloned.right.right = TreeNode(19)
        
        target = orig.right  # Node with value 3
        expected_output = cloned.right
        
        sol = Solution()
        result = sol.getTargetCopy(orig, cloned, target)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 3)
        self.assertIs(result, expected_output)

    def test_example_2_single_node_extreme_minimum(self):
        # tree = [7], target = 7 (Constraint Minimum)
        orig = TreeNode(7)
        cloned = TreeNode(7)
        target = orig
        expected_output = cloned
        
        sol = Solution()
        result = sol.getTargetCopy(orig, cloned, target)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 7)
        self.assertIs(result, expected_output)

    def test_example_3_skewed_tree(self):
        # tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
        values = [8, 6, 5, 4, 3, 2, 1]
        
        def build_skewed_right(vals):
            if not vals:
                return None
            root = TreeNode(vals[0])
            curr = root
            for val in vals[1:]:
                curr.right = TreeNode(val)
                curr = curr.right
            return root

        orig = build_skewed_right(values)
        cloned = build_skewed_right(values)
        
        target = self._find_node_by_val(orig, 4)
        expected_output = self._find_node_by_val(cloned, 4)
        
        sol = Solution()
        result = sol.getTargetCopy(orig, cloned, target)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 4)
        self.assertIs(result, expected_output)

    def test_target_is_left_leaf(self):
        # Balanced structure to ensure pathing logic covers left branches properly
        orig = TreeNode(10)
        orig.left = TreeNode(5)
        orig.right = TreeNode(15)
        
        cloned = TreeNode(10)
        cloned.left = TreeNode(5)
        cloned.right = TreeNode(15)
        
        target = orig.left
        expected_output = cloned.left
        
        sol = Solution()
        result = sol.getTargetCopy(orig, cloned, target)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 5)
        self.assertIs(result, expected_output)

    def test_deeply_nested_tree_constraint_large(self):
        # Validates deep recursion limits and structural traversal integrity
        # Creates a deep tree of 1000 nodes alternating left and right
        curr_orig = orig = TreeNode(0)
        curr_cloned = cloned = TreeNode(0)
        
        for i in range(1, 1000):
            if i % 2 == 1:
                curr_orig.left = TreeNode(i)
                curr_cloned.left = TreeNode(i)
                curr_orig = curr_orig.left
                curr_cloned = curr_cloned.left
            else:
                curr_orig.right = TreeNode(i)
                curr_cloned.right = TreeNode(i)
                curr_orig = curr_orig.right
                curr_cloned = curr_cloned.right
                
        target = curr_orig  # Deepest node (value 999)
        expected_output = curr_cloned
        
        sol = Solution()
        result = sol.getTargetCopy(orig, cloned, target)
        
        self.assertIsNotNone(result)
        self.assertEqual(result.val, 999)
        self.assertIs(result, expected_output)