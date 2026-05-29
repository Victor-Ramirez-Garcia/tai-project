#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Test Case: Example 1 from problem description
TEST(FillCupsTest, Example1) {
    Solution solution;
    std::vector<int> amount = {1, 4, 2};
    EXPECT_EQ(solution.fillCups(amount), 4);
}

// Test Case: Example 2 from problem description
TEST(FillCupsTest, Example2) {
    Solution solution;
    std::vector<int> amount = {5, 4, 4};
    EXPECT_EQ(solution.fillCups(amount), 7);
}

// Test Case: Example 3 from problem description
TEST(FillCupsTest, Example3) {
    Solution solution;
    std::vector<int> amount = {5, 0, 0};
    EXPECT_EQ(solution.fillCups(amount), 5);
}

// Edge Case: Minimum possible constraints (all zeros)
TEST(FillCupsTest, AllZeros) {
    Solution solution;
    std::vector<int> amount = {0, 0, 0};
    EXPECT_EQ(solution.fillCups(amount), 0);
}

// Edge Case: Maximum possible constraints (all 100)
TEST(FillCupsTest, AllMaxValues) {
    Solution solution;
    std::vector<int> amount = {100, 100, 100};
    EXPECT_EQ(solution.fillCups(amount), 150);
}

// Edge Case: Two types are empty
TEST(FillCupsTest, TwoTypesEmpty) {
    Solution solution;
    std::vector<int> amount = {0, 0, 75};
    EXPECT_EQ(solution.fillCups(amount), 75);
}

// Edge Case: One type is dominating the sum of the other two
TEST(FillCupsTest, OneDominatingType) {
    Solution solution;
    std::vector<int> amount = {10, 20, 100};
    EXPECT_EQ(solution.fillCups(amount), 100);
}

// Edge Case: Balanced values where sum is odd
TEST(FillCupsTest, BalancedOddSum) {
    Solution solution;
    std::vector<int> amount = {33, 33, 33};
    EXPECT_EQ(solution.fillCups(amount), 50);
}

// Edge Case: Balanced values where sum is even
TEST(FillCupsTest, BalancedEvenSum) {
    Solution solution;
    std::vector<int> amount = {33, 33, 34};
    EXPECT_EQ(solution.fillCups(amount), 50);
}