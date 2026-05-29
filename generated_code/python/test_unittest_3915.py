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


class TestMaxProductNoCommonBits(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_case_with_valid_pairs(self):
        """
        Tests a typical case where valid pairs with no common set bits exist.
        e.g., nums = [4, 8, 3, 5]
        Binary: 4 (0100), 8 (1000), 3 (0011), 5 (0101)
        Valid pairs: (4, 3) -> no common bits, product = 12
                     (8, 3) -> no common bits, product = 24
                     (8, 5) -> no common bits, product = 40
        Max product should be 40.
        """
        nums = [4, 8, 3, 5]
        self.assertEqual(self.sol.maxProduct(nums), 40)

    def test_no_valid_pair_exists(self):
        """
        Tests a case where every number shares at least one bit with every other number,
        meaning no valid pair exists. Should return 0.
        """
        # All numbers have the lowest bit set (odd numbers)
        nums = [1, 3, 5, 7]
        self.assertEqual(self.sol.maxProduct(nums), 0)

    def test_minimum_constraints(self):
        """
        Tests the absolute minimum constraints: length of nums is 2.
        Case A: Valid pair.
        Case B: Invalid pair (shares bits).
        """
        # Case A: 2 (0010) and 5 (0101) -> no common bits, product = 10
        self.assertEqual(self.sol.maxProduct([2, 5]), 10)
        
        # Case B: 2 (0010) and 6 (0110) -> share the 2nd bit, no valid pair -> 0
        self.assertEqual(self.sol.maxProduct([2, 6]), 0)

    def test_duplicate_values(self):
        """
        Tests when duplicate values are present. Identical numbers (except 0, which isn't in constraints)
        always share set bits with themselves, so they cannot form a valid pair together.
        """
        # [4, 4] -> 4 (0100) and 4 (0100) share bits -> 0
        self.assertEqual(self.sol.maxProduct([4, 4]), 0)
        
        # [4, 4, 3] -> (4, 3) is valid -> 12
        self.assertEqual(self.sol.maxProduct([4, 4, 3]), 12)

    def test_maximum_value_constraints(self):
        """
        Tests upper bound values for elements (up to 10^6).
        1000000 in binary is 11110100001001000000 (20 bits).
        We pair it with a number that fills the remaining/opposite bit positions.
        """
        # 1000000 = 0xF4240
        # Complement mask within bounds, e.g., 9 (1001) -> 0x9. No shared bits.
        # 0xF4240 & 0x9 == 0
        nums = [1000000, 9]
        self.assertEqual(self.sol.maxProduct(nums), 9000000)

    def test_large_input_performance_and_correctness(self):
        """
        Tests a larger array to ensure scalability and that the global maximum 
        is prioritized over smaller valid products.
        """
        # 1024 (2^10) and 2048 (2^11) have no common bits and yield a high product.
        # Other elements are smaller or share bits.
        nums = [1024, 2048, 7, 15, 31, 63, 127]
        self.assertEqual(self.sol.maxProduct(nums), 1024 * 2048)


if __name__ == "__main__":
    unittest.main()