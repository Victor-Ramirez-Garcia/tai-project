#include <gtest/gtest.h>
#include <vector>
#include <algorithm>
#include "solution_1_1.cpp" // Assuming ID is 1 based on the Two Sum problem ID

// Helper function to compare vectors regardless of order since the problem states:
// "You can return the answer in any order."
void AssertVectorEqualsIgnoreOrder(std::vector<int> actual, std::vector<int> expected) {
    std::sort(actual.begin(), actual.end());
    std::sort(expected.begin(), expected.end());
    EXPECT_EQ(actual, expected);
}

// Test case for Example 1 from the problem description
TEST(TwoSumTest, Example1) {
    Solution solution;

    // Helper to sort indices since the problem allows any order
    void verify_result(vector<int> result, vector<int> expected) {
        sort(result.begin(), result.end());
        sort(expected.begin(), expected.end());
        EXPECT_EQ(result, expected);
    }
};
// Test Example 1: Standard case
TEST_F(TwoSumTest, Example1_StandardCase) {
    vector<int> nums = {2, 7, 11, 15};
    int target = 9;
    std::vector<int> expected = {0, 1};
    AssertVectorEqualsIgnoreOrder(solution.twoSum(nums, target), expected);
}

// Test case for Example 2 from the problem description
TEST(TwoSumTest, Example2) {
    Solution solution;
    std::vector<int> nums = {3, 2, 4};
    int target = 6;
    std::vector<int> expected = {1, 2};
    AssertVectorEqualsIgnoreOrder(solution.twoSum(nums, target), expected);
}

// Test case for Example 3 from the problem description
TEST(TwoSumTest, Example3) {
    Solution solution;
    std::vector<int> nums = {3, 3};
    int target = 6;
    std::vector<int> expected = {0, 1};
    AssertVectorEqualsIgnoreOrder(solution.twoSum(nums, target), expected);
}

// Edge case: Minimum allowed array length constraint (nums.length == 2)
TEST(TwoSumTest, MinimumLengthConstraint) {
    Solution solution;
    std::vector<int> nums = {10, -5};
    int target = 5;
    std::vector<int> expected = {0, 1};
    AssertVectorEqualsIgnoreOrder(solution.twoSum(nums, target), expected);
}

// Edge case: Negative numbers in the input array and negative target
TEST(TwoSumTest, NegativeNumbersAndTarget) {
    Solution solution;
    std::vector<int> nums = {-1, -2, -3, -4, -5};
    int target = -8;
    std::vector<int> expected = {2, 4}; // -3 + -5 = -8
    AssertVectorEqualsIgnoreOrder(solution.twoSum(nums, target), expected);
}

// Edge case: Handling maximum and minimum constraint values (10^9 and -10^9)
TEST(TwoSumTest, LargeValueConstraints) {
    Solution solution;
    std::vector<int> nums = {1000000000, -1000000000, 0, 5};
    int target = 0;
    std::vector<int> expected = {0, 1}; // 10^9 + (-10^9) = 0
    AssertVectorEqualsIgnoreOrder(solution.twoSum(nums, target), expected);
}

// Edge case: Target is zero with mixed positive and negative numbers
TEST(TwoSumTest, TargetZeroWithMixedSigns) {
    Solution solution;
    std::vector<int> nums = {1, 2, 3, -2};
    int target = 0;
    std::vector<int> expected = {1, 3}; // 2 + (-2) = 0
    AssertVectorEqualsIgnoreOrder(solution.twoSum(nums, target), expected);
}

// Edge case: Elements that could add up to target but are the same index (must not use same element twice)
// Ensure the code correctly finds distinct elements with identical values.
TEST(TwoSumTest, DuplicateElementsSeparateIndices) {
    Solution solution;
    std::vector<int> nums = {1, 5, 3, 5, 9};
    int target = 10;
    std::vector<int> expected = {1, 3}; // The two 5s at indices 1 and 3
    AssertVectorEqualsIgnoreOrder(solution.twoSum(nums, target), expected);
}
