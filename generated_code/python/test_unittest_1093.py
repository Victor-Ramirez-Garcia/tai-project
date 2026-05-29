import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution

# Assuming TreeNode is either defined in the solution module or accessible
# We extract it from the loaded module to ensure compatibility
TreeNode = sol_module.TreeNode

class TestRecoverFromPreorder(unittest.TestCase):
    
    def _tree_to_list(self, root):
        """Helper method to serialize a binary tree into a level-order list with nulls,
        matching the LeetCode output format."""
        if not root:
            return []
        
        result = []
        queue = [root]
        
        while queue:
            # Check if there are any non-None nodes left in the queue to avoid trailing nulls
            if not any(node is not None for node in queue):
                break
                
            current = queue.pop(0)
            if current:
                result.append(current.val)
                queue.append(current.left)
                queue.append(current.right)
            else:
                result.append(None)
                
        # Trim trailing None values for exact matching
        while result and result[-1] is None:
            result.pop()
            
        return result

    def test_example_1(self):
        """Tests the first standard example: standard balanced-like tree."""
        traversal = "1-2--3--4-5--6--7"
        expected = [1, 2, 5, 3, 4, 6, 7]
        
        sol = Solution()
        root = sol.recoverFromPreorder(traversal)
        self.assertEqual(self._tree_to_list(root), expected)

    def test_example_2(self):
        """Tests the second standard example: deep left-skewed structures."""
        traversal = "1-2--3---4-5--6---7"
        expected = [1, 2, 5, 3, None, 6, None, 4, None, 7]
        
        sol = Solution()
        root = sol.recoverFromPreorder(traversal)
        self.assertEqual(self._tree_to_list(root), expected)

    def test_example_3(self):
        """Tests the third standard example: multi-digit node values and asymmetric children."""
        traversal = "1-401--349---90--88"
        expected = [1, 401, None, 349, 88, 90]
        
        sol = Solution()
        root = sol.recoverFromPreorder(traversal)
        self.assertEqual(self._tree_to_list(root), expected)

    def test_edge_case_single_node(self):
        """Tests the minimum constraint: a tree containing exactly one root node."""
        traversal = "99"
        expected = [99]
        
        sol = Solution()
        root = sol.recoverFromPreorder(traversal)
        self.assertEqual(self._tree_to_list(root), expected)

    def test_edge_case_max_value_node(self):
        """Tests node values at the maximum constraint limits (10^9)."""
        traversal = "1000000000-1000000000"
        expected = [1000000000, 1000000000]
        
        sol = Solution()
        root = sol.recoverFromPreorder(traversal)
        self.assertEqual(self._tree_to_list(root), expected)

    def test_edge_case_strictly_left_skewed(self):
        """Tests a completely linear left-skewed tree where each node has only a left child."""
        traversal = "1-2--3---4----5"
        expected = [1, 2, None, 3, None, 4, None, 5]
        
        sol = Solution()
        root = sol.recoverFromPreorder(traversal)
        self.assertEqual(self._tree_to_list(root), expected)

    def test_edge_case_deep_backtrack(self):
        """Tests deep backtracking where a right child attaches much higher up the tree hierarchy."""
        traversal = "1-2--3---4-5"
        expected = [1, 2, 5, 3, None, None, None, 4]
        
        sol = Solution()
        root = sol.recoverFromPreorder(traversal)
        self.assertEqual(self._tree_to_list(root), expected)