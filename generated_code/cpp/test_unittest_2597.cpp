#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

using namespace std;

// Test case for Example 1 from the problem description
TEST(CycleLengthQueriesTest, Example1) {
    Solution solution;
    int n = 3;
    vector<vector<int>> queries = {{5, 3}, {4, 7}, {2, 3}};
    vector<int> expected = {4, 5, 3};
    EXPECT_EQ(solution.cycleLengthQueries(n, queries), expected);
}

// Test case for Example 2 from the problem description
TEST(CycleLengthQueriesTest, Example2) {
    Solution solution;
    int n = 2;
    vector<vector<int>> queries = {{1, 2}};
    vector<int> expected = {2};
    EXPECT_EQ(solution.cycleLengthQueries(n, queries), expected);
}

// Test case for queries between a node and itself (cycle length 1 via multi-edge)
TEST(CycleLengthQueriesTest, SameNodeQuery) {
    Solution solution;
    int n = 3;
    vector<vector<int>> queries = {{3, 3}, {5, 5}};
    vector<int> expected = {1, 1};
    EXPECT_EQ(solution.cycleLengthQueries(n, queries), expected);
}

// Test case where one node is the direct parent of the other
TEST(CycleLengthQueriesTest, DirectParentChildQuery) {
    Solution solution;
    int n = 4;
    vector<vector<int>> queries = {{2, 4}, {1, 3}, {3, 7}};
    vector<int> expected = {2, 2, 2};
    EXPECT_EQ(solution.cycleLengthQueries(n, queries), expected);
}

// Test case for nodes sharing the same immediate parent (siblings)
TEST(CycleLengthQueriesTest, SiblingQuery) {
    Solution solution;
    int n = 4;
    vector<vector<int>> queries = {{4, 5}, {6, 7}, {2, 3}};
    vector<int> expected = {3, 3, 3};
    EXPECT_EQ(solution.cycleLengthQueries(n, queries), expected);
}

// Test case hitting extreme values near the maximum depth of the tree
TEST(CycleLengthQueriesTest, MaxDepthAndLargeValues) {
    Solution solution;
    int n = 30; // Max constraint typical for such binary tree depth problems
    // 1 << 29 is a valid node within the tree range [1, 2^n - 1]
    int nodeA = (1 << 29);
    int nodeB = (1 << 29) + 1; // Sibling to nodeA
    
    vector<vector<int>> queries = {{nodeA, nodeB}};
    vector<int> expected = {3}; // Path: nodeA -> parent -> nodeB -> back via new edge
    EXPECT_EQ(solution.cycleLengthQueries(n, queries), expected);
}

// Test case with multiple repetitive and mixed queries to verify stability
TEST(CycleLengthQueriesTest, MixedAndRepetitiveQueries) {
    Solution solution;
    int n = 5;
    vector<vector<int>> queries = {{16, 31}, {16, 31}, {1, 2}, {4, 7}};
    vector<int> expected = {9, 9, 2, 5};
    EXPECT_EQ(solution.cycleLengthQueries(n, queries), expected);
}