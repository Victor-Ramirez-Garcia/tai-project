import os
import importlib.util
import unittest

# Dynamic loading of the solution module as per the prompt instructions
solution_path = os.environ.get("TEST_SOLUTION_FILE")
if not solution_path:
    raise RuntimeError("TEST_SOLUTION_FILE environment variable is not set.")

spec = importlib.util.spec_from_file_location("Solution", solution_path)
sol_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol_module)
Solution = sol_module.Solution


class TestDeleteDuplicateFolder(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def assertPathsEqual(self, actual, expected):
        """Helper method to compare 2D path lists regardless of order."""
        sorted_actual = sorted([sorted(path) for path in actual])
        sorted_expected = sorted([sorted(path) for path in expected])

        # Normalize paths by converting them to tuples for sorting the outer list safely
        tuple_actual = sorted([tuple(path) for path in actual])
        tuple_expected = sorted([tuple(path) for path in expected])

        self.assertEqual(tuple_actual, tuple_expected)

    def test_example_1(self):
        paths = [["a"], ["c"], ["d"], ["a", "b"], ["c", "b"], ["d", "a"]]
        expected = [["d"], ["d", "a"]]
        actual = self.solution.deleteDuplicateFolder(paths)
        self.assertPathsEqual(actual, expected)

    def test_example_2(self):
        paths = [
            ["a"],
            ["c"],
            ["a", "b"],
            ["c", "b"],
            ["a", "b", "x"],
            ["a", "b", "x", "y"],
            ["w"],
            ["w", "y"],
        ]
        expected = [["c"], ["c", "b"], ["a"], ["a", "b"]]
        actual = self.solution.deleteDuplicateFolder(paths)
        self.assertPathsEqual(actual, expected)

    def test_example_3(self):
        paths = [["a", "b"], ["c", "d"], ["c"], ["a"]]
        expected = [["c"], ["c", "d"], ["a"], ["a", "b"]]
        actual = self.solution.deleteDuplicateFolder(paths)
        self.assertPathsEqual(actual, expected)

    def test_no_duplicates(self):
        paths = [["a"], ["a", "b"], ["a", "b", "c"]]
        expected = [["a"], ["a", "b"], ["a", "b", "c"]]
        actual = self.solution.deleteDuplicateFolder(paths)
        self.assertPathsEqual(actual, expected)

    def test_all_duplicates_deleted(self):
        # Two identical root-level folders with identical subfolders should both be deleted
        paths = [["a"], ["a", "x"], ["b"], ["b", "x"]]
        expected = []
        actual = self.solution.deleteDuplicateFolder(paths)
        self.assertPathsEqual(actual, expected)

    def test_nested_identical_structures(self):
        # Verification that identical subtrees deep within different hierarchies are marked
        paths = [
            ["root1", "a"],
            ["root1", "a", "b"],
            ["root2", "a"],
            ["root2", "a", "b"],
        ]
        expected = []
        actual = self.solution.deleteDuplicateFolder(paths)
        self.assertPathsEqual(actual, expected)

    def test_empty_folders_not_matching_non_empty(self):
        # An empty folder structure should not match a folder structure containing children
        paths = [["a"], ["b"], ["b", "c"]]
        expected = [["a"], ["b"], ["b", "c"]]
        actual = self.solution.deleteDuplicateFolder(paths)
        self.assertPathsEqual(actual, expected)

    def test_single_folder_path(self):
        # Minimal constraints: single root folder with no subfolders
        paths = [["a"]]
        expected = [["a"]]
        actual = self.solution.deleteDuplicateFolder(paths)
        self.assertPathsEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()