#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

class MinCostPathTest : public ::testing::Test {
protected:
    Solution sol;
};

/**
 * @brief Example 1 from problem description.
 * Grid requires 3 direction changes to reach the bottom-right.
 */
TEST_F(MinCostPathTest, Example1_MultipleChanges) {
    vector<vector<int>> grid = {
        {1, 1, 1, 1},
        {2, 2, 2, 2},
        {1, 1, 1, 1},
        {2, 2, 2, 2}
    };
    EXPECT_EQ(sol.minCost(grid), 3);
}

/**
 * @brief Example 2 from problem description.
 * Path is already valid with 0 cost.
 */
TEST_F(MinCostPathTest, Example2_ZeroCost) {
    vector<vector<int>> grid = {
        {1, 1, 3},
        {3, 2, 2},
        {1, 1, 4}
    };
    EXPECT_EQ(sol.minCost(grid), 0);
}

/**
 * @brief Example 3 from problem description.
 * Small 2x2 grid requiring 1 change.
 */
TEST_F(MinCostPathTest, Example3_SmallGrid) {
    vector<vector<int>> grid = {
        {1, 2},
        {4, 3}
    };
    EXPECT_EQ(sol.minCost(grid), 1);
}

/**
 * @brief Minimum constraint: 1x1 grid.
 * Cost should be 0 as start and end are the same cell.
 */
TEST_F(MinCostPathTest, EdgeCase_SingleCell) {
    vector<vector<int>> grid = {{1}};
    EXPECT_EQ(sol.minCost(grid), 0);
}

/**
 * @brief Single row grid.
 * Should follow right arrows (1) or cost 1 to change to right.
 */
TEST_F(MinCostPathTest, EdgeCase_SingleRow) {
    vector<vector<int>> grid = {{1, 1, 2, 1}};
    // (0,0)->(0,1)->(0,2)[change 2 to 1 cost 1]->(0,3)
    EXPECT_EQ(sol.minCost(grid), 1);
}

/**
 * @brief Single column grid.
 * Should follow down arrows (3) or cost 1 to change to down.
 */
TEST_F(MinCostPathTest, EdgeCase_SingleColumn) {
    vector<vector<int>> grid = {{3}, {4}, {3}};
    // (0,0)->(1,0)[change 4 to 3 cost 1]->(2,0)
    EXPECT_EQ(sol.minCost(grid), 1);
}

/**
 * @brief All arrows point away from the target.
 * Tests if the algorithm correctly finds the minimum modifications.
 */
TEST_F(MinCostPathTest, Complex_AllWrongDirections) {
    vector<vector<int>> grid = {
        {2, 2, 2},
        {4, 4, 4},
        {4, 4, 4}
    };
    // Minimum cost would be going right twice and down twice (or vice versa)
    // with appropriate changes.
    EXPECT_EQ(sol.minCost(grid), 4);
}

/**
 * @brief Grid where arrows point outside boundaries.
 * Validates handling of out-of-bounds pointers.
 */
TEST_F(MinCostPathTest, EdgeCase_OutOfBoundsArrows) {
    vector<vector<int>> grid = {
        {2, 1},
        {4, 1}
    };
    // (0,0) points left (out), (0,1) points right (out)
    // (1,0) points up, (1,1) is target.
    // Optimal: (0,0) change to right (1) -> (0,1) change to down (3) -> (1,1) : cost 2
    // OR: (0,0) change to down (3) -> (1,0) change to right (1) -> (1,1) : cost 2
    EXPECT_EQ(sol.minCost(grid), 2);
}