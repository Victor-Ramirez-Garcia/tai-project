import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per guidelines
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution
TreeNode = sol_module.TreeNode

class TestIsSubtree(unittest.TestCase):
    
    def _build_tree(self, nodes):
        """Helper method to construct a binary tree from a LeetCode level-order list."""
        if not nodes:
            return None
        
        root = TreeNode(nodes[0])
        queue = [root]
        front = 0
        index = 1
        
        while index < len(nodes):
            node = queue[front]
            front += 1
            
            # Left child
            if nodes[index] is not None:
                node.left = TreeNode(nodes[index])
                queue.append(node.left)
            index += 1
            
            # Right child
            if index < len(nodes):
                if nodes[index] is not None:
                    node.right = TreeNode(nodes[index])
                    queue.append(node.right)
                index += 1
                
        return root

    def test_example_1_positive_match(self):
        # Input: root = [3,4,5,1,2], subRoot = [4,1,2] -> True
        root = self._build_tree([3, 4, 5, 1, 2])
        sub_root = self._build_tree([4, 1, 2])
        
        sol = Solution()
        self.assertTrue(sol.isSubtree(root, sub_root))

    def test_example_2_structural_mismatch(self):
        # Input: root = [3,4,5,1,2,None,None,None,None,0], subRoot = [4,1,2] -> False
        root = self._build_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
        sub_root = self._build_tree([4, 1, 2])
        
        sol = Solution()
        self.assertFalse(sol.isSubtree(root, sub_root))

    def test_identical_trees(self):
        # Core Constraint/Property: A tree is a subtree of itself
        root = self._build_tree([1, 2, 3])
        sub_root = self._build_tree([1, 2, 3])
        
        sol = Solution()
        self.assertTrue(sol.isSubtree(root, sub_root))

    def test_single_node_match(self):
        # Minimum input constraints: Both trees have 1 node and match
        root = self._build_tree([42])
        sub_root = self._build_tree([42])
        
        sol = Solution()
        self.assertTrue(sol.isSubtree(root, sub_root))

    def test_single_node_mismatch(self):
        # Minimum input constraints: Both trees have 1 node but values differ
        root = self._build_tree([42])
        sub_root = self._build_tree([99])
        
        sol = Solution()
        self.assertFalse(sol.isSubtree(root, sub_root))

    def test_subroot_deeper_than_root(self):
        # Structural constraint: subRoot has more nodes than root, cannot be a subtree
        root = self._build_tree([1])
        sub_root = self._build_tree([1, 2, 3])
        
        sol = Solution()
        self.assertFalse(sol.isSubtree(root, sub_root))

    def test_negative_values_match(self):
        # Value boundaries: Constraints specify -10^4 <= val <= 10^4
        root = self._build_tree([-10, -20, -30, -40])
        sub_root = self._build_tree([-20, -40])
        
        sol = Solution()
        self.assertTrue(sol.isSubtree(root, sub_root))

    def test_duplicate_values_in_root_correct_match(self):
        # Ensure the algorithm traverses the entire tree and finds the actual matching subtree 
        # even if an earlier node with the same value fails the full structural match.
        root = self._build_tree([4, 4, 5, 1, 2]) # Top root is 4, left child is also 4
        sub_root = self._build_tree([4, 1, 2])
        
        sol = Solution()
        self.assertTrue(sol.isSubtree(root, sub_root))

if __name__ == "__main__":
    unittest.main()