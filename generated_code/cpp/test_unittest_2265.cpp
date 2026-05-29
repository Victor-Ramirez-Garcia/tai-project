#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

class PivotArrayTest : public ::testing::Test {
protected:
    Solution sol;
};

TEST_F(PivotArrayTest, Example1_StandardCase) {
    vector<int> nums = {9, 12, 5, 10, 14, 3, 10};
    int pivot = 10;
    vector<int> expected = {9, 5, 3, 10, 10, 12, 14};
    EXPECT_EQ(sol.pivotArray(nums, pivot), expected);
}

TEST_F(PivotArrayTest, Example2_NegativeAndSmallArray) {
    vector<int> nums = {-3, 4, 3, 2};
    int pivot = 2;
    vector<int> expected = {-3, 2, 4, 3};
    EXPECT_EQ(sol.pivotArray(nums, pivot), expected);
}

TEST_F(PivotArrayTest, MinimumConstraintSize) {
    vector<int> nums = {1};
    int pivot = 1;
    vector<int> expected = {1};
    EXPECT_EQ(sol.pivotArray(nums, pivot), expected);
}

TEST_F(PivotArrayTest, AllElementsSmallerThanPivot) {
    vector<int> nums = {1, 2, 3, 4};
    int pivot = 5;
    vector<int> expected = {1, 2, 3, 4};
    EXPECT_EQ(sol.pivotArray(nums, pivot), expected);
}

TEST_F(PivotArrayTest, AllElementsGreaterThanPivot) {
    vector<int> nums = {10, 20, 30};
    int pivot = 5;
    vector<int> expected = {10, 20, 30};
    EXPECT_EQ(sol.pivotArray(nums, pivot), expected);
}

TEST_F(PivotArrayTest, AllElementsEqualToPivot) {
    vector<int> nums = {5, 5, 5, 5};
    int pivot = 5;
    vector<int> expected = {5, 5, 5, 5};
    EXPECT_EQ(sol.pivotArray(nums, pivot), expected);
}

TEST_F(PivotArrayTest, PivotNotPresentInArray) {
    vector<int> nums = {10, 2, 8, 1};
    int pivot = 5;
    vector<int> expected = {2, 1, 10, 8};
    EXPECT_EQ(sol.pivotArray(nums, pivot), expected);
}

TEST_F(PivotArrayTest, MaintainsRelativeOrderLargeConstraints) {
    vector<int> nums = {20, 1, 20, 2, 20, 3};
    int pivot = 10;
    // Elements < 10: [1, 2, 3]
    // Elements == 10: []
    // Elements > 10: [20, 20, 20]
    vector<int> expected = {1, 2, 3, 20, 20, 20};
    EXPECT_EQ(sol.pivotArray(nums, pivot), expected);
}

TEST_F(PivotArrayTest, HandlesDuplicatePivotsAndMixedOrder) {
    vector<int> nums = {5, 2, 5, 8, 5, 1};
    int pivot = 5;
    // Elements < 5: [2, 1]
    // Elements == 5: [5, 5, 5]
    // Elements > 5: [8]
    vector<int> expected = {2, 1, 5, 5, 5, 8};
    EXPECT_EQ(sol.pivotArray(nums, pivot), expected);
}