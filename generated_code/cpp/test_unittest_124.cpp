#include "solution_proxy.h"
#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <iostream>

// Helper function to build a tree from a level-order traversal vector (including nulls as -1001)
// Since node values range from -1000 to 1000, we can use -1001 to represent nullptr.
const int NULL_NODE = -1001;

TreeNode* buildTree(const std::vector<int>& nodes) {
    if (nodes.empty() || nodes[0] == NULL_NODE) return nullptr;

    TreeNode* root = new TreeNode(nodes[0]);
    std::queue<TreeNode*> q;
    q.push(root);

    size_t i = 1;
    while (!q.empty() && i < nodes.size()) {
        TreeNode* curr = q.front();
        q.pop();

        if (i < nodes.size() && nodes[i] != NULL_NODE) {
            curr->left = new TreeNode(nodes[i]);
            q.push(curr->left);
        }
        i++;

        if (i < nodes.size() && nodes[i] != NULL_NODE) {
            curr->right = new TreeNode(nodes[i]);
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

// Helper function to safely delete the dynamically allocated tree
void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

class BinaryTreeMaxPathSumTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case 1: Provided Example 1 [1, 2, 3]
TEST_F(BinaryTreeMaxPathSumTest, Example1_SimpleTree) {
    std::vector<int> nodes = {1, 2, 3};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solution.maxPathSum(root), 6);
    freeTree(root);
}

// Test Case 2: Provided Example 2 [-10, 9, 20, null, null, 15, 7]
TEST_F(BinaryTreeMaxPathSumTest, Example2_TreeWithNegatives) {
    std::vector<int> nodes = {-10, 9, 20, NULL_NODE, NULL_NODE, 15, 7};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solution.maxPathSum(root), 42);
    freeTree(root);
}

// Test Case 3: Single node tree (Minimum size constraint)
TEST_F(BinaryTreeMaxPathSumTest, EdgeCase_SingleNodePositive) {
    std::vector<int> nodes = {42};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solution.maxPathSum(root), 42);
    freeTree(root);
}

// Test Case 4: Single node with minimum value constraint (-1000)
TEST_F(BinaryTreeMaxPathSumTest, EdgeCase_SingleNodeNegativeMinimum) {
    std::vector<int> nodes = {-1000};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solution.maxPathSum(root), -1000);
    freeTree(root);
}

// Test Case 5: All nodes are negative values
TEST_F(BinaryTreeMaxPathSumTest, Scenario_AllNegativeNodes) {
    std::vector<int> nodes = {-3, -1, -2};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solution.maxPathSum(root), -1);
    freeTree(root);
}

// Test Case 6: Path goes through only one branch (does not use root split)
TEST_F(BinaryTreeMaxPathSumTest, Scenario_PathInOneBranch) {
    std::vector<int> nodes = {5, 4, 8, 11, NULL_NODE, 13, 4, 7, 2, NULL_NODE, NULL_NODE, NULL_NODE, 1};
    TreeNode* root = buildTree(nodes);
    // Path: 11 -> 4 -> 7 or 11 -> 4 -> 2, maximum is 11 + 4 + 7 = 22 or 11 + 4 + 2 = 17, wait:
    // Let's verify the tree structure: 
    //            5
    //          /   \
    //         4     8
    //        /     / \
    //       11    13  4
    //      /  \        \
    //     7    2        1
    // Max path here is 7 -> 11 -> 2 = 20, or 7 -> 11 -> 4 -> 5 -> 8 -> 13 = 48
    EXPECT_EQ(solution.maxPathSum(root), 48);
    freeTree(root);
}

// Test Case 7: Only root is positive, children are highly negative
TEST_F(BinaryTreeMaxPathSumTest, Scenario_PositiveRootNegativeChildren) {
    std::vector<int> nodes = {10, -20, -30};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solution.maxPathSum(root), 10);
    freeTree(root);
}

// Test Case 8: Maximum constraint values (Maximum node value 1000)
TEST_F(BinaryTreeMaxPathSumTest, EdgeCase_MaximumValues) {
    std::vector<int> nodes = {1000, 1000, 1000};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solution.maxPathSum(root), 3000);
    freeTree(root);
}

// Test Case 9: Long skewed line tree (linked list pattern)
TEST_F(BinaryTreeMaxPathSumTest, Scenario_SkewedTree) {
    std::vector<int> nodes = {1, 2, NULL_NODE, 3, NULL_NODE, 4, NULL_NODE, 5};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solution.maxPathSum(root), 15);
    freeTree(root);
}