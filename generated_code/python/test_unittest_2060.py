import os
import importlib.util
import unittest
from typing import List, Optional

# Dynamic Loading Setup as required
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

# We assume TreeNode is either defined within the solution module or standard LeetCode style.
# If TreeNode is needed for test construction, we attempt to grab it from the module or define a compatible one.
if hasattr(sol_module, 'TreeNode'):
    TreeNode = sol_module.TreeNode
else:
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

class TestCanMergeBSTs(unittest.TestCase):
    
    def _tree_to_list(self, root: Optional[TreeNode]) -> List[Optional[int]]:
        """Helper method to serialize a binary tree to a level-order list for assertion."""
        if not root:
            return []
        result = []
        queue = [root]
        while queue:
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
        # Trim trailing None values to match typical LeetCode serialization
        while result and result[-1] is None:
            result.pop()
        return result

    def test_example_1_successful_merge(self):
        # trees = [[2,1],[3,2,5],[5,4]]
        t1 = TreeNode(2, left=TreeNode(1))
        t2 = TreeNode(3, left=TreeNode(2), right=TreeNode(5))
        t3 = TreeNode(5, left=TreeNode(4))
        
        sol = Solution()
        result = sol.canMerge([t1, t2, t3])
        
        # Expected output serialization: [3,2,5,1,null,4]
        self.assertEqual(self._tree_to_list(result), [3, 2, 5, 1, None, 4])

    def test_example_2_invalid_bst_result(self):
        # trees = [[5,3,8],[3,2,6]]
        t1 = TreeNode(5, left=TreeNode(3), right=TreeNode(8))
        t2 = TreeNode(3, left=TreeNode(2), right=TreeNode(6))
        
        sol = Solution()
        result = sol.canMerge([t1, t2])
        
        # Expected output: None (impossible to form a *valid* BST)
        self.assertIsNone(result)

    def test_example_3_no_operations_possible(self):
        # trees = [[5,4],[3]]
        t1 = TreeNode(5, left=TreeNode(4))
        t2 = TreeNode(3)
        
        sol = Solution()
        result = sol.canMerge([t1, t2])
        
        self.assertIsNone(result)

    def test_single_tree_already_valid(self):
        # Minimum input size edge case: n = 1
        t1 = TreeNode(10, left=TreeNode(5), right=TreeNode(15))
        
        sol = Solution()
        result = sol.canMerge([t1])
        
        self.assertEqual(self._tree_to_list(result), [10, 5, 15])

    def test_cycle_detection(self):
        # Trees form a cycle (e.g., leaf of A matches root of B, leaf of B matches root of A)
        t1 = TreeNode(2, left=TreeNode(3))
        t2 = TreeNode(3, left=TreeNode(2))
        
        sol = Solution()
        result = sol.canMerge([t1, t2])
        
        self.assertIsNone(result)

    def test_disconnected_components(self):
        # Multiple trees that can't all be connected into a single component
        t1 = TreeNode(2, left=TreeNode(1))
        t2 = TreeNode(3, right=TreeNode(4))
        t3 = TreeNode(10, left=TreeNode(9))
        
        sol = Solution()
        result = sol.canMerge([t1, t2, t3])
        
        self.assertIsNone(result)

    def test_multiple_leaves_same_value(self):
        # Invalid configuration where multiple trees expect to attach to the same root value
        t1 = TreeNode(5, left=TreeNode(2))
        t2 = TreeNode(6, left=TreeNode(2))
        t3 = TreeNode(2)
        
        sol = Solution()
        result = sol.canMerge([t1, t2, t3])
        
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()