#include <gtest/gtest.h>
#include <vector>
#include <string>
#include "solution_proxy.h"

// Test Case 1: Example 1 from problem description
TEST(FinalValueAfterOperationsTest, Example1) {
    Solution solution;
    std::vector<std::string> operations = {"--X", "X++", "X++"};
    EXPECT_EQ(solution.finalValueAfterOperations(operations), 1);
}

// Test Case 2: Example 2 from problem description
TEST(FinalValueAfterOperationsTest, Example2) {
    Solution solution;
    std::vector<std::string> operations = {"++X", "++X", "X++"};
    EXPECT_EQ(solution.finalValueAfterOperations(operations), 3);
}

// Test Case 3: Example 3 from problem description
TEST(FinalValueAfterOperationsTest, Example3) {
    Solution solution;
    std::vector<std::string> operations = {"X++", "++X", "--X", "X--"};
    EXPECT_EQ(solution.finalValueAfterOperations(operations), 0);
}

// Test Case 4: Single increment operation (Edge Case / Minimum Constraints)
TEST(FinalValueAfterOperationsTest, SingleIncrement) {
    Solution solution;
    std::vector<std::string> operations1 = {"++X"};
    std::vector<std::string> operations2 = {"X++"};
    EXPECT_EQ(solution.finalValueAfterOperations(operations1), 1);
    EXPECT_EQ(solution.finalValueAfterOperations(operations2), 1);
}

// Test Case 5: Single decrement operation (Edge Case / Minimum Constraints)
TEST(FinalValueAfterOperationsTest, SingleDecrement) {
    Solution solution;
    std::vector<std::string> operations1 = {"--X"};
    std::vector<std::string> operations2 = {"X--"};
    EXPECT_EQ(solution.finalValueAfterOperations(operations1), -1);
    EXPECT_EQ(solution.finalValueAfterOperations(operations2), -1);
}

// Test Case 6: All increments to test positive scaling
TEST(FinalValueAfterOperationsTest, AllIncrements) {
    Solution solution;
    std::vector<std::string> operations = {"++X", "X++", "++X", "X++", "++X"};
    EXPECT_EQ(solution.finalValueAfterOperations(operations), 5);
}

// Test Case 7: All decrements to test negative scaling
TEST(FinalValueAfterOperationsTest, AllDecrements) {
    Solution solution;
    std::vector<std::string> operations = {"--X", "X--", "--X", "X--", "--X"};
    EXPECT_EQ(solution.finalValueAfterOperations(operations), -5);
}