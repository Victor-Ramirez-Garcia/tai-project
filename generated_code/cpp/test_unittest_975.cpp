#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include <iostream>
#include "solution_proxy.h"

// Helper function to build a tree from a level-order vector (using -1 for null/empty nodes)
TreeNode* buildTree(const std::vector<int>& nodes) {
    if (nodes.empty() || nodes[0] == -1) return nullptr;
    
    TreeNode* root = new TreeNode(nodes[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    
    size_t i = 1;
    while (!q.empty() && i < nodes.size()) {
        TreeNode* curr = q.front();
        q.pop();
        
        if (i < nodes.size() && nodes[i] != -1) {
            curr->left = new TreeNode(nodes[i]);
            q.push(curr->left);
        }
        i++;
        
        if (i < nodes.size() && nodes[i] != -1) {
            curr->right = new TreeNode(nodes[i]);
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

// Helper function to free the allocated tree memory
void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

class RangeSumBSTTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case 1: Provided Example 1
TEST_F(RangeSumBSTTest, Example1) {
    std::vector<int> nodes = {10, 5, 15, 3, 7, -1, 18};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 7, 15);
    EXPECT_EQ(result, 32);
    
    freeTree(root);
}

// Test Case 2: Provided Example 2
TEST_F(RangeSumBSTTest, Example2) {
    std::vector<int> nodes = {10, 5, 15, 3, 7, 13, 18, 1, -1, 6};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 6, 10);
    EXPECT_EQ(result, 23);
    
    freeTree(root);
}

// Test Case 3: Edge Case - Single Node Tree Within Range
TEST_F(RangeSumBSTTest, SingleNodeWithinRange) {
    std::vector<int> nodes = {10};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 5, 15);
    EXPECT_EQ(result, 10);
    
    freeTree(root);
}

// Test Case 4: Edge Case - Single Node Tree Outside Range (Too Low)
TEST_F(RangeSumBSTTest, SingleNodeOutsideRangeTooLow) {
    std::vector<int> nodes = {5};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 10, 20);
    EXPECT_EQ(result, 0);
    
    freeTree(root);
}

// Test Case 5: Edge Case - Single Node Tree Outside Range (Too High)
TEST_F(RangeSumBSTTest, SingleNodeOutsideRangeTooHigh) {
    std::vector<int> nodes = {25};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 10, 20);
    EXPECT_EQ(result, 0);
    
    freeTree(root);
}

// Test Case 6: Edge Case - Single Node Matching Exact Bound (Low Boundary)
TEST_F(RangeSumBSTTest, SingleNodeExactLowBound) {
    std::vector<int> nodes = {10};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 10, 20);
    EXPECT_EQ(result, 10);
    
    freeTree(root);
}

// Test Case 7: Edge Case - Single Node Matching Exact Bound (High Boundary)
TEST_F(RangeSumBSTTest, SingleNodeExactHighBound) {
    std::vector<int> nodes = {20};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 10, 20);
    EXPECT_EQ(result, 20);
    
    freeTree(root);
}

// Test Case 8: All Nodes Outside Range (Entire tree values less than low)
TEST_F(RangeSumBSTTest, AllNodesLessThanLow) {
    std::vector<int> nodes = {5, 3, 8, 1, 4};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 10, 20);
    EXPECT_EQ(result, 0);
    
    freeTree(root);
}

// Test Case 9: All Nodes Outside Range (Entire tree values greater than high)
TEST_F(RangeSumBSTTest, AllNodesGreaterThanHigh) {
    std::vector<int> nodes = {30, 25, 35};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 5, 15);
    EXPECT_EQ(result, 0);
    
    freeTree(root);
}

// Test Case 10: All Nodes Within Range (Inclusive sum of the entire tree)
TEST_F(RangeSumBSTTest, AllNodesWithinRange) {
    std::vector<int> nodes = {10, 5, 15};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 1, 20);
    EXPECT_EQ(result, 30); // 10 + 5 + 15
    
    freeTree(root);
}

// Test Case 11: Complex Tree with No Matching Range Elements
TEST_F(RangeSumBSTTest, NoNodesInRangeInComplexTree) {
    std::vector<int> nodes = {40, 20, 60, 10, 30, 50, 70};
    TreeNode* root = buildTree(nodes);
    
    int result = solution.rangeSumBST(root, 31, 39);
    EXPECT_EQ(result, 0);
    
    freeTree(root);
}