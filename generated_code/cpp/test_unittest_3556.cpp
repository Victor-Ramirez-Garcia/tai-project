#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Test Case 1: Standard example with distinct elements
TEST(GetFinalStateTest, StandardExampleDistinct) {
    Solution sol;
    std::vector<int> nums = {2, 1, 3, 5, 6};
    int k = 5;
    int multiplier = 2;
    // Expected simulation:
    // Op 1: min=1 (idx 1) -> {2, 2, 3, 5, 6}
    // Op 2: min=2 (idx 0) -> {4, 2, 3, 5, 6}
    // Op 3: min=2 (idx 1) -> {4, 4, 3, 5, 6}
    // Op 4: min=3 (idx 2) -> {4, 4, 6, 5, 6}
    // Op 5: min=4 (idx 0) -> {8, 4, 6, 5, 6}
    // Modulo 10^9 + 7 applied at the end
    std::vector<int> expected = {8, 4, 6, 5, 6};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 2: Multiplier of 1 (array should remain unchanged)
TEST(GetFinalStateTest, MultiplierIsOne) {
    Solution sol;
    std::vector<int> nums = {1, 2, 3, 4};
    int k = 100;
    int multiplier = 1;
    std::vector<int> expected = {1, 2, 3, 4};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 3: Zero operations (k = 0)
TEST(GetFinalStateTest, ZeroOperations) {
    Solution sol;
    std::vector<int> nums = {4, 3, 2, 1};
    int k = 0;
    int multiplier = 5;
    std::vector<int> expected = {4, 3, 2, 1};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 4: Multiple occurrences of the minimum value (tie-breaking rule)
// Should always select the one that appears first (lowest index).
TEST(GetFinalStateTest, DuplicateMinimumsTieBreaking) {
    Solution sol;
    std::vector<int> nums = {2, 2, 2};
    int k = 2;
    int multiplier = 2;
    // Op 1: min=2 (idx 0) -> {4, 2, 2}
    // Op 2: min=2 (idx 1) -> {4, 4, 2}
    std::vector<int> expected = {4, 4, 2};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 5: Single element array (Edge Case)
TEST(GetFinalStateTest, SingleElement) {
    Solution sol;
    std::vector<int> nums = {3};
    int k = 3;
    int multiplier = 2;
    // 3 * 2 * 2 * 2 = 24
    std::vector<int> expected = {24};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 6: Large k causing modulo trigger
// Verifies that the final results are correctly moduloed by 10^9 + 7.
TEST(GetFinalStateTest, ModuloOverflowTrigger) {
    Solution sol;
    std::vector<int> nums = {1000000000};
    int k = 1;
    int multiplier = 2;
    // 1000000000 * 2 = 2000000000
    // 2000000000 % 1000000007 = 999999993
    std::vector<int> expected = {999999993};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}