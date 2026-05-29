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


class TestMinimumPairRemoval(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_already_non_decreasing_sorted(self):
        # Array is already non-decreasing, 0 operations needed
        nums = [1, 2, 3, 4, 5]
        self.assertEqual(self.sol.minimumPairRemoval(nums), 0)

    def test_already_non_decreasing_with_duplicates(self):
        # Array contains duplicates but is non-decreasing
        nums = [2, 2, 3, 3, 4]
        self.assertEqual(self.sol.minimumPairRemoval(nums), 0)

    def test_single_element_array(self):
        # Base edge case: an array of size 1 is vacuously non-decreasing
        nums = [10]
        self.assertEqual(self.sol.minimumPairRemoval(nums), 0)

    def test_strictly_decreasing_array(self):
        # Leftmost minimum sum pair simulation:
        # [4, 3, 2, 1] -> min sum is 2+1=3 (rightmost). Wait, leftmost min sum pair:
        # Pairs: (4,3)->7, (3,2)->5, (2,1)->3. Min sum is 3. New array: [4, 3, 3]
        # Next pairs: (4,3)->7, (3,3)->6. Min sum is 6. New array: [4, 6] -> Non-decreasing.
        # Total operations: 2
        nums = [4, 3, 2, 1]
        self.assertEqual(self.sol.minimumPairRemoval(nums), 2)

    def test_leftmost_tie_breaking(self):
        # Pairs and sums: (3,1)->4, (1,3)->4, (3,1)->4. 
        # All have sum 4. Rule dictates choosing the leftmost pair (index 0 and 1).
        # [3, 1, 3, 1] -> replace leftmost (3,1) with 4 -> [4, 3, 1]
        # Next pairs: (4,3)->7, (3,1)->4. Min sum is 4 -> [4, 4] -> Non-decreasing.
        # Total operations: 2
        nums = [3, 1, 3, 1]
        self.assertEqual(self.sol.minimumPairRemoval(nums), 2)

    def test_large_elements_no_overflow(self):
        # Testing larger values to ensure constraints handling
        nums = [1000000, 500000, 600000]
        # Pairs: (1000000, 500000)->1500000, (500000, 600000)->1100000
        # Min sum is 1100000. New array: [1000000, 1100000] -> Non-decreasing.
        # Total operations: 1
        nums = [1000000, 500000, 600000]
        self.assertEqual(self.sol.minimumPairRemoval(nums), 1)

    def test_single_operation_needed(self):
        # A small violation at the end
        nums = [1, 2, 4, 3]
        # Pairs: (1,2)->3, (2,4)->6, (4,3)->7
        # Min sum pair is (1,2) -> [3, 4, 3]
        # Next pairs: (3,4)->7, (4,3)->7. Leftmost is (3,4) -> [7, 3]
        # Next pair: (7,3)->10 -> [10] -> Non-decreasing.
        # Total operations: 3
        nums = [1, 2, 4, 3]
        self.assertEqual(self.sol.minimumPairRemoval(nums), 3)


if __name__ == "__main__":
    unittest.main()