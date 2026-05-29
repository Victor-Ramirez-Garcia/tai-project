#include <gtest/gtest.h>
#include <vector>
#include <string>
#include "solution_proxy.h"

// Test Case: Example 1 from the problem description
TEST(MinOperationsTest, Example1) {
    Solution solver;
    std::string boxes = "110";
    std::vector<int> expected = {1, 1, 3};
    EXPECT_EQ(solver.minOperations(boxes), expected);
}

// Test Case: Example 2 from the problem description
TEST(MinOperationsTest, Example2) {
    Solution solver;
    std::string boxes = "001011";
    std::vector<int> expected = {11, 8, 5, 4, 3, 4};
    EXPECT_EQ(solver.minOperations(boxes), expected);
}

// Test Case: Minimum constraints - Single empty box
TEST(MinOperationsTest, SingleEmptyBox) {
    Solution solver;
    std::string boxes = "0";
    std::vector<int> expected = {0};
    EXPECT_EQ(solver.minOperations(boxes), expected);
}

// Test Case: Minimum constraints - Single box with a ball
TEST(MinOperationsTest, SingleBoxWithBall) {
    Solution solver;
    std::string boxes = "1";
    std::vector<int> expected = {0};
    EXPECT_EQ(solver.minOperations(boxes), expected);
}

// Test Case: All boxes are empty
TEST(MinOperationsTest, AllBoxesEmpty) {
    Solution solver;
    std::string boxes = "00000";
    std::vector<int> expected = {0, 0, 0, 0, 0};
    EXPECT_EQ(solver.minOperations(boxes), expected);
}

// Test Case: All boxes contain a ball
TEST(MinOperationsTest, AllBoxesFull) {
    Solution solver;
    std::string boxes = "1111";
    // For index 0: 1+2+3 = 6
    // For index 1: 1+0+1+2 = 4
    // For index 2: 2+1+0+1 = 4
    // For index 3: 3+2+1+0 = 6
    std::vector<int> expected = {6, 4, 4, 6};
    EXPECT_EQ(solver.minOperations(boxes), expected);
}

// Test Case: Maximum constraints scale check (2000 boxes, all full)
// This ensures no integer overflow and acceptable performance.
TEST(MinOperationsTest, MaxConstraintsAllFull) {
    Solution solver;
    int n = 2000;
    std::string boxes(n, '1');
    std::vector<int> result = solver.minOperations(boxes);
    
    ASSERT_EQ(result.size(), n);
    
    // Mathematically verifying the boundary elements
    // For the first element (index 0), total operations = sum from i=1 to 1999 of i
    // Sum = (1999 * 2000) / 2 = 1,999,000
    long long expected_first = (1999LL * 2000LL) / 2LL;
    EXPECT_EQ(result[0], static_cast<int>(expected_first));
    EXPECT_EQ(result[n - 1], static_cast<int>(expected_first));
}