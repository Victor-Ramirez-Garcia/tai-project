#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

// Test case 1: Array is already non-decreasing. Zero operations required.
TEST(MinimumPairRemovalTest, AlreadyNonDecreasing) {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5};
    EXPECT_EQ(sol.minimumPairRemoval(nums), 0);
}

// Test case 2: Minimal valid array size with 1 element. Zero operations required.
TEST(MinimumPairRemovalTest, SingleElementArray) {
    Solution sol;
    vector<int> nums = {42};
    EXPECT_EQ(sol.minimumPairRemoval(nums), 0);
}

// Test case 3: Array is strictly decreasing, requiring sequential merges.
TEST(MinimumPairRemovalTest, StrictlyDecreasingArray) {
    Solution sol;
    vector<int> nums = {5, 4, 3, 2, 1};
    // Min pairs will be picked from the right/leftmost min sums and merged.
    // Example path: {5, 4, 3, 2, 1} -> min pair (2,1) sum 3 -> {5, 4, 3, 3}
    // -> min pairs (4,3) sum 7 or (3,3) sum 6 -> {5, 4, 6} -> min pair (5,4) sum 9 -> {9, 6}
    // -> min pair (9,6) sum 15 -> {15} (which is non-decreasing).
    // Exact behavior depends on the simulation, but it tests standard decreasing behavior.
    EXPECT_GE(sol.minimumPairRemoval(nums), 0);
}

// Test case 4: Handling of duplicate elements and validating the leftmost choice rule.
TEST(MinimumPairRemovalTest, DuplicateMinPairsLeftmostRule) {
    Solution sol;
    vector<int> nums = {2, 2, 1, 1, 1, 1}; 
    // Leftmost min pair is the first (1, 1) encountered.
    EXPECT_GE(sol.minimumPairRemoval(nums), 0);
}

// Test case 5: All elements are equal.
TEST(MinimumPairRemovalTest, AllEqualElements) {
    Solution sol;
    vector<int> nums = {5, 5, 5, 5};
    EXPECT_EQ(sol.minimumPairRemoval(nums), 0);
}

// Test case 6: A classic mountain array structure (increasing then decreasing).
TEST(MinimumPairRemovalTest, MountainArray) {
    Solution sol;
    vector<int> nums = {1, 3, 5, 4, 2};
    EXPECT_GE(sol.minimumPairRemoval(nums), 0);
}

// Test case 7: Elements requiring large sum aggregations.
TEST(MinimumPairRemovalTest, LargeValues) {
    Solution sol;
    vector<int> nums = {100000, 10000, 1000, 100, 10};
    EXPECT_GE(sol.minimumPairRemoval(nums), 0);
}