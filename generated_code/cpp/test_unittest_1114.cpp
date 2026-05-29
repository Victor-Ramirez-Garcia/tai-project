#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include "solution_proxy.h"

// Helper function to build a tree from a level-order vector (using -1 or a flag for null, 
// but since node values can be 0 or positive up to 100 based on typical BST problems, 
// we'll use -1 to represent null nodes in our test setup).
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

// Helper function to convert a tree back to a level-order vector for validation,
// truncating trailing -1 (null) values to match standard LeetCode representation.
std::vector<int> treeToVector(TreeNode* root) {
    std::vector<int> result;
    if (!root) return result;
    
    std::queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        TreeNode* curr = q.front();
        q.pop();
        
        if (curr) {
            result.push_back(curr->val);
            q.push(curr->left);
            q.push(curr->right);
        } else {
            result.push_back(-1);
        }
    }
    
    while (!result.empty() && result.back() == -1) {
        result.pop_back();
    }
    return result;
}

// Helper function to safely delete the allocated tree memory
void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

class BstToGstTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case: Example 1 from problem description
TEST_F(BstToGstTest, TestExample1) {
    std::vector<int> input = {4, 1, 6, 0, 2, 5, 7, -1, -1, -1, 3, -1, -1, -1, 8};
    std::vector<int> expected = {30, 36, 21, 36, 35, 26, 15, -1, -1, -1, 33, -1, -1, -1, 8};
    
    TreeNode* root = buildTree(input);
    TreeNode* resultRoot = solution.bstToGst(root);
    std::vector<int> result = treeToVector(resultRoot);
    
    EXPECT_EQ(result, expected);
    freeTree(resultRoot);
}

// Test Case: Example 2 from problem description
TEST_F(BstToGstTest, TestExample2) {
    std::vector<int> input = {0, -1, 1};
    std::vector<int> expected = {1, -1, 1};
    
    TreeNode* root = buildTree(input);
    TreeNode* resultRoot = solution.bstToGst(root);
    std::vector<int> result = treeToVector(resultRoot);
    
    EXPECT_EQ(result, expected);
    freeTree(resultRoot);
}

// Test Case: Edge case with an empty tree (nullptr)
TEST_F(BstToGstTest, TestEmptyTree) {
    TreeNode* root = nullptr;
    TreeNode* resultRoot = solution.bstToGst(root);
    
    EXPECT_EQ(resultRoot, nullptr);
}

// Test Case: Edge case with a single node
TEST_F(BstToGstTest, TestSingleNode) {
    std::vector<int> input = {5};
    std::vector<int> expected = {5};
    
    TreeNode* root = buildTree(input);
    TreeNode* resultRoot = solution.bstToGst(root);
    std::vector<int> result = treeToVector(resultRoot);
    
    EXPECT_EQ(result, expected);
    freeTree(resultRoot);
}

// Test Case: Minimal right-leaning skewed tree
TEST_F(BstToGstTest, TestRightSkewedTree) {
    std::vector<int> input = {1, -1, 2, -1, 3};
    std::vector<int> expected = {6, -1, 5, -1, 3};
    
    TreeNode* root = buildTree(input);
    TreeNode* resultRoot = solution.bstToGst(root);
    std::vector<int> result = treeToVector(resultRoot);
    
    EXPECT_EQ(result, expected);
    freeTree(resultRoot);
}

// Test Case: Minimal left-leaning skewed tree
TEST_F(BstToGstTest, TestLeftSkewedTree) {
    std::vector<int> input = {3, 2, -1, 1};
    std::vector<int> expected = {3, 5, -1, 6};
    
    TreeNode* root = buildTree(input);
    TreeNode* resultRoot = solution.bstToGst(root);
    std::vector<int> result = treeToVector(resultRoot);
    
    EXPECT_EQ(result, expected);
    freeTree(resultRoot);
}