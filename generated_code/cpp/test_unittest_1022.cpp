#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using std::vector;

// Test Case 1: Example 1 from problem description
TEST(UniquePathsIIITest, Example1) {
    Solution solver;
    vector<vector<int>> grid = {
        {1, 0, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 2, -1}
    };
    EXPECT_EQ(solver.uniquePathsIII(grid), 2);
}

// Test Case 2: Example 2 from problem description
TEST(UniquePathsIIITest, Example2) {
    Solution solver;
    vector<vector<int>> grid = {
        {1, 0, 0, 0},
        {0, 0, 0, 0},
        {0, 0, 0, 2}
    };
    EXPECT_EQ(solver.uniquePathsIII(grid), 4);
}

// Test Case 3: Example 3 from problem description (No valid path)
TEST(UniquePathsIIITest, Example3_NoPath) {
    Solution solver;
    vector<vector<int>> grid = {
        {0, 1},
        {2, 0}
    };
    EXPECT_EQ(solver.uniquePathsIII(grid), 0);
}

// Test Case 4: Minimal grid size (1x2) with just start and end, no empty cells
TEST(UniquePathsIIITest, MinimumGridSize_StartAndEndOnly) {
    Solution solver;
    vector<vector<int>> grid = {
        {1, 2}
    };
    EXPECT_EQ(solver.uniquePathsIII(grid), 1);
}

// Test Case 5: Grid with completely blocked paths due to obstacles
TEST(UniquePathsIIITest, BlockedByObstacles) {
    Solution solver;
    vector<vector<int>> grid = {
        {1,  0, -1},
        {-1, 0, -1},
        {-1, 0,  2}
    };
    EXPECT_EQ(solver.uniquePathsIII(grid), 0);
}

// Test Case 6: Grid where the end cell is trapped by obstacles
TEST(UniquePathsIIITest, TrappedEndCell) {
    Solution solver;
    vector<vector<int>> grid = {
        {1,  0,  0},
        {0, -1, -1},
        {0, -1,  2}
    };
    EXPECT_EQ(solver.uniquePathsIII(grid), 0);
}

// Test Case 7: Linear grid (1xn) with a single valid straight path
TEST(UniquePathsIIITest, LinearGrid_SinglePath) {
    Solution solver;
    vector<vector<int>> grid = {
        {1, 0, 0, 0, 2}
    };
    EXPECT_EQ(solver.uniquePathsIII(grid), 1);
}

// Test Case 8: Grid with multiple obstacles but exactly one winding path covering all empty spaces
TEST(UniquePathsIIITest, SnakingPathWithObstacles) {
    Solution solver;
    vector<vector<int>> grid = {
        { 1,  0, -1},
        { 0,  0, -1},
        { 0,  0,  2}
    };
    // Path: (0,0) -> (1,0) -> (2,0) -> (2,1) -> (1,1) -> (0,1) -> (0,2 is block, 1,2 is block) 
    // Wait, let's verify if all 0s can be visited.
    // 0s are at (0,1), (1,0), (1,1), (2,0), (2,1). Total 5 empty cells.
    // Length of path must be start + 5 empty + end = 7 cells.
    // (0,0)[1] -> (0,1)[0] -> (1,1)[0] -> (1,0)[0] -> (2,0)[0] -> (2,1)[0] -> (2,2)[2]. All visited exactly once.
    EXPECT_EQ(solver.uniquePathsIII(grid), 1);
}