#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Test Case 1: Standard Example 1 from problem description
TEST(NumberGameTest, Example1) {
    Solution solution;
    std::vector<int> nums = {5, 4, 2, 3};
    std::vector<int> expected = {3, 2, 5, 4};
    EXPECT_EQ(solution.numberGame(nums), expected);
}

// Test Case 2: Standard Example 2 from problem description (Minimum even size)
TEST(NumberGameTest, Example2) {
    Solution solution;
    std::vector<int> nums = {2, 5};
    std::vector<int> expected = {5, 2};
    EXPECT_EQ(solution.numberGame(nums), expected);
}

// Test Case 3: Already sorted array input
TEST(NumberGameTest, AlreadySortedInput) {
    Solution solution;
    std::vector<int> nums = {1, 2, 3, 4, 5, 6};
    std::vector<int> expected = {2, 1, 4, 3, 6, 5};
    EXPECT_EQ(solution.numberGame(nums), expected);
}

// Test Case 4: Reverse sorted array input
TEST(NumberGameTest, ReverseSortedInput) {
    Solution solution;
    std::vector<int> nums = {6, 5, 4, 3, 2, 1};
    std::vector<int> expected = {2, 1, 4, 3, 6, 5};
    EXPECT_EQ(solution.numberGame(nums), expected);
}

// Test Case 5: Array containing duplicate elements
TEST(NumberGameTest, DuplicateElements) {
    Solution solution;
    std::vector<int> nums = {2, 2, 1, 1};
    std::vector<int> expected = {1, 1, 2, 2};
    EXPECT_EQ(solution.numberGame(nums), expected);
}

// Test Case 6: All elements are identical
TEST(NumberGameTest, AllIdenticalElements) {
    Solution solution;
    std::vector<int> nums = {7, 7, 7, 7, 7, 7};
    std::vector<int> expected = {7, 7, 7, 7, 7, 7};
    EXPECT_EQ(solution.numberGame(nums), expected);
}

// Test Case 7: Large values and negative elements if constraints permit signed integers
TEST(NumberGameTest, NegativeAndLargeValues) {
    Solution solution;
    std::vector<int> nums = {1000, -500, 0, -1000};
    std::vector<int> expected = {-500, -1000, 1000, 0};
    EXPECT_EQ(solution.numberGame(nums), expected);
}