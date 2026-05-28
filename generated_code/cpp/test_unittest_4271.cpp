#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

// Test Case 1: Standard graph (Example scenario)
TEST(FindDegreesTest, StandardGraph) {
    Solution solution;
    vector<vector<int>> matrix = {
        {0, 1, 1},
        {1, 0, 0},
        {1, 0, 0}
    };
    vector<int> expected = {2, 1, 1};
    EXPECT_EQ(solution.findDegrees(matrix), expected);
}

// Test Case 2: Disconnected graph (No edges at all)
TEST(FindDegreesTest, DisconnectedGraph) {
    Solution solution;
    vector<vector<int>> matrix = {
        {0, 0, 0},
        {0, 0, 0},
        {0, 0, 0}
    };
    vector<int> expected = {0, 0, 0};
    EXPECT_EQ(solution.findDegrees(matrix), expected);
}

// Test Case 3: Complete graph (Every vertex is connected to every other vertex except itself)
TEST(FindDegreesTest, CompleteGraph) {
    Solution solution;
    vector<vector<int>> matrix = {
        {0, 1, 1, 1},
        {1, 0, 1, 1},
        {1, 1, 0, 1},
        {1, 1, 1, 0}
    };
    vector<int> expected = {3, 3, 3, 3};
    EXPECT_EQ(solution.findDegrees(matrix), expected);
}

// Test Case 4: Minimum input size (Single vertex graph)
TEST(FindDegreesTest, SingleVertexGraph) {
    Solution solution;
    vector<vector<int>> matrix = {
        {0}
    };
    vector<int> expected = {0};
    EXPECT_EQ(solution.findDegrees(matrix), expected);
}

// Test Case 5: Empty matrix boundary condition
TEST(FindDegreesTest, EmptyMatrix) {
    Solution solution;
    vector<vector<int>> matrix = {};
    vector<int> expected = {};
    EXPECT_EQ(solution.findDegrees(matrix), expected);
}

// Test Case 6: Graph containing self-loops 
// (Ensures the implementation correctly handles or counts self-edges if they occur)
TEST(FindDegreesTest, GraphWithSelfLoops) {
    Solution solution;
    vector<vector<int>> matrix = {
        {1, 1},
        {1, 0}
    };
    vector<int> expected = {2, 1};
    EXPECT_EQ(solution.findDegrees(matrix), expected);
}

// Test Case 7: Asymmetric matrix or star topology
TEST(FindDegreesTest, StarTopologyGraph) {
    Solution solution;
    vector<vector<int>> matrix = {
        {0, 1, 1, 1},
        {1, 0, 0, 0},
        {1, 0, 0, 0},
        {1, 0, 0, 0}
    };
    vector<int> expected = {3, 1, 1, 1};
    EXPECT_EQ(solution.findDegrees(matrix), expected);
}