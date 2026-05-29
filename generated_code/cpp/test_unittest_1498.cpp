#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include "solution_proxy.h"

// Helper function to build a tree from a level-order vector (using -1 for null/empty nodes since values are unique and positive here, or a structured approach)
// For the sake of testing, we will implement a robust helper that accepts standard optional-like representation.
// Since node values are positive/unique in the examples, we can use -1 to represent null.
TreeNode* buildTree(const std::vector<int>& values) {
    if (values.empty() || values[0] == -1) return nullptr;
    
    TreeNode* root = new TreeNode(values[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    
    size_t i = 1;
    while (!q.empty() && i < values.size()) {
        TreeNode* curr = q.front();
        q.pop();
        
        if (i < values.size() && values[i] != -1) {
            curr->left = new TreeNode(values[i]);
            q.push(curr->left);
        }
        i++;
        
        if (i < values.size() && values[i] != -1) {
            curr->right = new TreeNode(values[i]);
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

// Helper to find a node with a specific value in the tree (to locate the target node in the original tree)
TreeNode* findNode(TreeNode* root, int val) {
    if (!root) return nullptr;
    if (root->val == val) return root;
    TreeNode* leftSearch = findNode(root->left, val);
    if (leftSearch) return leftSearch;
    return findNode(root->right, val);
}

// Helper to free memory
void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

class GetTargetCopyTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case 1: Example 1 from problem description
TEST_F(GetTargetCopyTest, Example1_NormalBinaryTree) {
    std::vector<int> treeProto = {7, 4, 3, -1, -1, 6, 19};
    TreeNode* original = buildTree(treeProto);
    TreeNode* cloned = buildTree(treeProto);
    
    TreeNode* target = findNode(original, 3);
    
    TreeNode* result = solution.getTargetCopy(original, cloned, target);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 3);
    // Ensure the returned reference belongs to the cloned tree, not the original tree
    EXPECT_NE(result, target);
    
    freeTree(original);
    freeTree(cloned);
}

// Test Case 2: Example 2 from problem description (Single node tree / Minimum size constraint)
TEST_F(GetTargetCopyTest, Example2_SingleNodeTree) {
    std::vector<int> treeProto = {7};
    TreeNode* original = buildTree(treeProto);
    TreeNode* cloned = buildTree(treeProto);
    
    TreeNode* target = findNode(original, 7);
    
    TreeNode* result = solution.getTargetCopy(original, cloned, target);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 7);
    EXPECT_NE(result, target);
    EXPECT_EQ(result, cloned); // In a single node tree, the result must be the cloned root itself
    
    freeTree(original);
    freeTree(cloned);
}

// Test Case 3: Example 3 from problem description (Skewed right tree)
TEST_F(GetTargetCopyTest, Example3_SkewedRightTree) {
    std::vector<int> treeProto = {8, -1, 6, -1, 5, -1, 4, -1, 3, -1, 2, -1, 1};
    TreeNode* original = buildTree(treeProto);
    TreeNode* cloned = buildTree(treeProto);
    
    TreeNode* target = findNode(original, 4);
    
    TreeNode* result = solution.getTargetCopy(original, cloned, target);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 4);
    EXPECT_NE(result, target);
    
    freeTree(original);
    freeTree(cloned);
}

// Test Case 4: Target is the root node in a larger tree
TEST_F(GetTargetCopyTest, TargetIsRootNode) {
    std::vector<int> treeProto = {10, 5, 15, 3, 7, -1, 18};
    TreeNode* original = buildTree(treeProto);
    TreeNode* cloned = buildTree(treeProto);
    
    TreeNode* target = original; // Root node
    
    TreeNode* result = solution.getTargetCopy(original, cloned, target);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 10);
    EXPECT_NE(result, target);
    EXPECT_EQ(result, cloned);
    
    freeTree(original);
    freeTree(cloned);
}

// Test Case 5: Target is a deeply nested leaf node (Skewed left tree)
TEST_F(GetTargetCopyTest, TargetDeeplyNestedLeftLeaf) {
    std::vector<int> treeProto = {5, 4, -1, 3, -1, 2, -1, 1, -1};
    TreeNode* original = buildTree(treeProto);
    TreeNode* cloned = buildTree(treeProto);
    
    TreeNode* target = findNode(original, 1);
    
    TreeNode* result = solution.getTargetCopy(original, cloned, target);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 1);
    EXPECT_NE(result, target);
    
    freeTree(original);
    freeTree(cloned);
}