#include <gtest/gtest.h>
#include <vector>
#include <algorithm>
#include "program_1_1.cpp"

using namespace std;

class TwoSumTest : public ::testing::Test {
protected:
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
    vector<int> expected = {0, 1};
    verify_result(solution.twoSum(nums, target), expected);
}

// Test Example 2: Elements are not at the beginning
TEST_F(TwoSumTest, Example2_MiddleElements) {
    vector<int> nums = {3, 2, 4};
    int target = 6;
    vector<int> expected = {1, 2};
    verify_result(solution.twoSum(nums, target), expected);
}

// Test Example 3: Duplicate values
TEST_F(TwoSumTest, Example3_DuplicateValues) {
    vector<int> nums = {3, 3};
    int target = 6;
    vector<int> expected = {0, 1};
    verify_result(solution.twoSum(nums, target), expected);
}

// Test Edge Case: Minimum array length constraint (length = 2)
TEST_F(TwoSumTest, Constraint_MinimumLength) {
    vector<int> nums = {10, -10};
    int target = 0;
    vector<int> expected = {0, 1};
    verify_result(solution.twoSum(nums, target), expected);
}

// Test Edge Case: Large negative and positive values
TEST_F(TwoSumTest, Constraint_LargeValues) {
    vector<int> nums = {-1000000000, 1000000000, 0};
    int target = 0;
    vector<int> expected = {0, 1};
    verify_result(solution.twoSum(nums, target), expected);
}

// Test Case: Target is reached by adding a positive and a negative number
TEST_F(TwoSumTest, PositiveAndNegativeNumbers) {
    vector<int> nums = {-1, -2, -3, -4, -5};
    int target = -8;
    vector<int> expected = {2, 4};
    verify_result(solution.twoSum(nums, target), expected);
}

// Test Case: Solution elements are at the extreme ends of a large array
TEST_F(TwoSumTest, ElementsAtExtremeEnds) {
    vector<int> nums(10000, 0);
    nums[0] = 1;
    nums[9999] = 2;
    int target = 3;
    vector<int> expected = {0, 9999};
    verify_result(solution.twoSum(nums, target), expected);
}
