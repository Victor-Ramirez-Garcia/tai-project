#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Test case for Example 1 provided in the problem description
TEST(TotalStepsTest, Example1) {
    Solution solution;
    std::vector<int> nums = {5, 3, 4, 4, 7, 3, 6, 11, 8, 5, 11};
    EXPECT_EQ(solution.totalSteps(nums), 3);
}

// Test case for Example 2 provided in the problem description (already sorted)
TEST(TotalStepsTest, Example2) {
    Solution solution;
    std::vector<int> nums = {4, 5, 7, 7, 13};
    EXPECT_EQ(solution.totalSteps(nums), 0);
}

// Test case for the minimum input size boundary constraint (length = 1)
TEST(TotalStepsTest, MinimumLength) {
    Solution solution;
    std::vector<int> nums = {42};
    EXPECT_EQ(solution.totalSteps(nums), 0);
}

// Test case where elements are strictly decreasing
TEST(TotalStepsTest, StrictlyDecreasing) {
    Solution solution;
    std::vector<int> nums = {5, 4, 3, 2, 1};
    // Step 1: 5 remains, all others are stripped because nums[i-1] > nums[i]
    EXPECT_EQ(solution.totalSteps(nums), 1);
}

// Test case where all elements are identical
TEST(TotalStepsTest, AllIdenticalElements) {
    Solution solution;
    std::vector<int> nums = {7, 7, 7, 7, 7};
    EXPECT_EQ(solution.totalSteps(nums), 0);
}

// Test case simulating cascading dependencies/steps where elements are removed sequentially
TEST(TotalStepsTest, CascadingRemovals) {
    Solution solution;
    // 10 will eat 1, then in the next step eat 2, then 3, then 4. Total steps = 4.
    std::vector<int> nums = {10, 1, 2, 3, 4};
    EXPECT_EQ(solution.totalSteps(nums), 4);
}

// Test case involving multiple independent peak/valley segments
TEST(TotalStepsTest, MultiplePeaksAndValleys) {
    Solution solution;
    // Peaks at 10 and 20 acting independently
    std::vector<int> nums = {10, 1, 2, 20, 1, 2, 3};
    // For 10, {1, 2} takes 2 steps. For 20, {1, 2, 3} takes 3 steps. Max steps = 3.
    EXPECT_EQ(solution.totalSteps(nums), 3);
}

// Test case with a single large peak followed by many smaller, increasing values
TEST(TotalStepsTest, LargePeakFollowedByIncreasingSequence) {
    Solution solution;
    std::vector<int> nums = {100, 10, 20, 30, 40, 50};
    EXPECT_EQ(solution.totalSteps(nums), 5);
}