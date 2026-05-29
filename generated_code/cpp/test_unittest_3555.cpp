#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

// Test Case 1: Standard Example 1 (Simulated typical behavior)
// Input: nums = [2, 1, 3, 5, 6], k = 5, multiplier = 2
// Op 1: Min is 1 (idx 1) -> [2, 2, 3, 5, 6]
// Op 2: Min is 2 (idx 0, first occurrence) -> [4, 2, 3, 5, 6]
// Op 3: Min is 2 (idx 1) -> [4, 4, 3, 5, 6]
// Op 4: Min is 3 (idx 2) -> [4, 4, 6, 5, 6]
// Op 5: Min is 4 (idx 0, first occurrence) -> [8, 4, 6, 5, 6]
TEST(GetFinalStateTest, StandardExample1) {
    Solution sol;
    vector<int> nums = {2, 1, 3, 5, 6};
    int k = 5;
    int multiplier = 2;
    vector<int> expected = {8, 4, 6, 5, 6};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 2: Standard Example 2 (Simulated tie-breaking logic)
// Input: nums = [1, 2], k = 3, multiplier = 4
// Op 1: Min is 1 (idx 0) -> [4, 2]
// Op 2: Min is 2 (idx 1) -> [4, 8]
// Op 3: Min is 4 (idx 0) -> [16, 8]
TEST(GetFinalStateTest, StandardExample2) {
    Solution sol;
    vector<int> nums = {1, 2};
    int k = 3;
    int multiplier = 4;
    vector<int> expected = {16, 8};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 3: Zero operations (k = 0)
// The array should remain unchanged.
TEST(GetFinalStateTest, ZeroOperations) {
    Solution sol;
    vector<int> nums = {4, 7, 2, 9};
    int k = 0;
    int multiplier = 3;
    vector<int> expected = {4, 7, 2, 9};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 4: Multiplier is 1
// Multiplying by 1 does not change values, but structural updates should still process.
TEST(GetFinalStateTest, MultiplierIsOne) {
    Solution sol;
    vector<int> nums = {5, 3, 8};
    int k = 10;
    int multiplier = 1;
    vector<int> expected = {5, 3, 8};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 5: Single element array (Minimum size edge case)
TEST(GetFinalStateTest, SingleElementArray) {
    Solution sol;
    vector<int> nums = {3};
    int k = 3;
    int multiplier = 2;
    vector<int> expected = {24}; // 3 * 2 * 2 * 2
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 6: Duplicate minimum values tie-breaking stability
// Ensure that the first minimum occurrence is transformed first.
// Input: nums = [2, 2, 2], k = 2, multiplier = 3
// Op 1: Min is 2 (idx 0) -> [6, 2, 2]
// Op 2: Min is 2 (idx 1) -> [6, 6, 2]
TEST(GetFinalStateTest, DuplicateMinimumsTieBreaking) {
    Solution sol;
    vector<int> nums = {2, 2, 2};
    int k = 2;
    int multiplier = 3;
    vector<int> expected = {6, 6, 2};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}

// Test Case 7: All identical elements with enough operations to cycle through all
// Input: nums = [2, 2], k = 3, multiplier = 2
// Op 1: Min is 2 (idx 0) -> [4, 2]
// Op 2: Min is 2 (idx 1) -> [4, 4]
// Op 3: Min is 4 (idx 0) -> [8, 4]
TEST(GetFinalStateTest, CompleteCycleOfIdenticalElements) {
    Solution sol;
    vector<int> nums = {2, 2};
    int k = 3;
    int multiplier = 2;
    vector<int> expected = {8, 4};
    EXPECT_EQ(sol.getFinalState(nums, k, multiplier), expected);
}