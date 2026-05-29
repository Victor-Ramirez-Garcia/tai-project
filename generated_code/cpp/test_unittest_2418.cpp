#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Test Case 1: Example 1 from the problem statement (No modifications allowed)
TEST(MinSumSquareDiffTest, Example1NoModifications) {
    Solution sol;
    std::vector<int> nums1 = {1, 2, 3, 4};
    std::vector<int> nums2 = {2, 10, 20, 19};
    int k1 = 0;
    int k2 = 0;
    long long expected = 579;
    EXPECT_EQ(sol.minSumSquareDiff(nums1, nums2, k1, k2), expected);
}

// Test Case 2: Example 2 from the problem statement (Standard budget for modifications)
TEST(MinSumSquareDiffTest, Example2StandardBudget) {
    Solution sol;
    std::vector<int> nums1 = {1, 4, 10, 12};
    std::vector<int> nums2 = {5, 8, 6, 9};
    int k1 = 1;
    int k2 = 1;
    long long expected = 43;
    EXPECT_EQ(sol.minSumSquareDiff(nums1, nums2, k1, k2), expected);
}

// Test Case 3: Absolute difference can be completely reduced to 0
TEST(MinSumSquareDiffTest, BudgetExceedsTotalDifference) {
    Solution sol;
    std::vector<int> nums1 = {1, 3, 5};
    std::vector<int> nums2 = {3, 5, 7};
    int k1 = 3;
    int k2 = 4; // Total k = 7, total absolute difference = 2 + 2 + 2 = 6
    long long expected = 0;
    EXPECT_EQ(sol.minSumSquareDiff(nums1, nums2, k1, k2), expected);
}

// Test Case 4: Minimal constraint edge case (n = 1, elements are equal)
TEST(MinSumSquareDiffTest, MinimumSizeAlreadyEqual) {
    Solution sol;
    std::vector<int> nums1 = {10};
    std::vector<int> nums2 = {10};
    int k1 = 5;
    int k2 = 5;
    long long expected = 0;
    EXPECT_EQ(sol.minSumSquareDiff(nums1, nums2, k1, k2), expected);
}

// Test Case 5: Large single difference with a budget that does not cover it entirely
TEST(MinSumSquareDiffTest, LargeSingleDifferencePartialReduction) {
    Solution sol;
    std::vector<int> nums1 = {100};
    std::vector<int> nums2 = {0};
    int k1 = 30;
    int k2 = 20; // Total k = 50, remaining diff = 50
    long long expected = 2500; // 50^2
    EXPECT_EQ(sol.minSumSquareDiff(nums1, nums2, k1, k2), expected);
}

// Test Case 6: Multiple maximum differences that must be decremented evenly
TEST(MinSumSquareDiffTest, EvenDistributionOfReductions) {
    Solution sol;
    std::vector<int> nums1 = {10, 10, 10};
    std::vector<int> nums2 = {0, 0, 0};
    int k1 = 2;
    int k2 = 2; // Total k = 4. Diffs: [10, 10, 10] -> [9, 9, 8]
    long long expected = 9 * 9 + 9 * 9 + 8 * 8; // 81 + 81 + 64 = 226
    EXPECT_EQ(sol.minSumSquareDiff(nums1, nums2, k1, k2), expected);
}

// Test Case 7: Elements have identical values but varying cross-array differences
TEST(MinSumSquareDiffTest, MixedDifferences) {
    Solution sol;
    std::vector<int> nums1 = {1, 2, 3, 4, 5};
    std::vector<int> nums2 = {5, 4, 3, 2, 1}; // Diffs: [4, 2, 0, 2, 4]
    int k1 = 3;
    int k2 = 1; // Total k = 4. Highest diffs (4, 4) become (2, 2) or balanced.
    // Initial diff frequencies: 4:2, 2:2, 0:1
    // Decrementing largest: 4, 4 -> 3, 3 (k=2 used) -> 2, 2 (k=4 used)
    // Final diffs: [2, 2, 0, 2, 2]
    long long expected = 4 * (2 * 2) + 0; // 16
    EXPECT_EQ(sol.minSumSquareDiff(nums1, nums2, k1, k2), expected);
}

// Test Case 8: Maximum constraint verification for k values (k1, k2 up to 10^9)
// Checks that potential integer overflow is properly handled by using long long
TEST(MinSumSquareDiffTest, LargeKValuesHandling) {
    Solution sol;
    std::vector<int> nums1 = {100000, 100000};
    std::vector<int> nums2 = {0, 0};
    int k1 = 1000000000;
    int k2 = 1000000000;
    long long expected = 0; // Budget enormously exceeds total possible difference
    EXPECT_EQ(sol.minSumSquareDiff(nums1, nums2, k1, k2), expected);
}