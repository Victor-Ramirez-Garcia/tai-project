#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include <string>
#include "solution_proxy.h"

using namespace std;

// Helper function to serialize a binary tree into a level-order vector (LeetCode style)
// to make test assertions intuitive and robust.
vector<int> treeToVector(TreeNode* root) {
    if (!root) return {};
    
    vector<int> result;
    queue<TreeNode*> q;
    q.push(root);
    
    while (!q.empty()) {
        TreeNode* curr = q.front();
        q.pop();
        
        if (curr) {
            result.push_back(curr->val);
            q.push(curr->left);
            q.push(curr->right);
        } else {
            result.push_back(-1); // Use -1 to represent null nodes
        }
    }
    
    // Trim trailing -1s (nulls) to match standard LeetCode representation
    while (!result.empty() && result.back() == -1) {
        result.pop_back();
    }
    
    return result;
}

// Helper function to recursively delete the tree and prevent memory leaks
void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

class RecoverFromPreorderTest : public ::testing::Test {
protected:
    Solution solver;
};

// Test Case 1: Example 1 from problem description
TEST_F(RecoverFromPreorderTest, Example1_BalancedStructure) {
    string traversal = "1-2--3--4-5--6--7";
    TreeNode* root = solver.recoverFromPreorder(traversal);
    
    vector<int> expected = {1, 2, 5, 3, 4, 6, 7};
    EXPECT_EQ(treeToVector(root), expected);
    
    freeTree(root);
}

// Test Case 2: Example 2 from problem description (Deeply skewed subtrees)
TEST_F(RecoverFromPreorderTest, Example2_DeepSkewedSubtrees) {
    string traversal = "1-2--3---4-5--6---7";
    TreeNode* root = solver.recoverFromPreorder(traversal);
    
    // LeetCode vector representation uses -1 for null here
    vector<int> expected = {1, 2, 5, 3, -1, 6, -1, 4, -1, -1, 7};
    EXPECT_EQ(treeToVector(root), expected);
    
    freeTree(root);
}

// Test Case 3: Example 3 from problem description (Multi-digit node values)
TEST_F(RecoverFromPreorderTest, Example3_MultiDigitValues) {
    string traversal = "1-401--349---90--88";
    TreeNode* root = solver.recoverFromPreorder(traversal);
    
    vector<int> expected = {1, 401, -1, 349, 88, 90};
    EXPECT_EQ(treeToVector(root), expected);
    
    freeTree(root);
}

// Test Case 4: Edge Case - Single node tree (Minimum input constraints)
TEST_F(RecoverFromPreorderTest, EdgeCase_SingleNode) {
    string traversal = "99";
    TreeNode* root = solver.recoverFromPreorder(traversal);
    
    vector<int> expected = {99};
    EXPECT_EQ(treeToVector(root), expected);
    
    freeTree(root);
}

// Test Case 5: Edge Case - Large node value up to upper bound (10^9)
TEST_F(RecoverFromPreorderTest, EdgeCase_MaxNodeValue) {
    string traversal = "1000000000-5--10";
    TreeNode* root = solver.recoverFromPreorder(traversal);
    
    vector<int> expected = {1000000000, 5, -1, 10};
    EXPECT_EQ(treeToVector(root), expected);
    
    freeTree(root);
}

// Test Case 6: Edge Case - Completely left-skewed tree (Straight line)
// Validates constraint rule: "If a node has only one child, that child is guaranteed to be the left child."
// Depth increases sequentially up to a chain of nodes.
TEST_F(RecoverFromPreorderTest, EdgeCase_StrictlyLeftSkewed) {
    string traversal = "1-2--3---4";
    TreeNode* root = solver.recoverFromPreorder(traversal);
    
    vector<int> expected = {1, 2, -1, 3, -1, 4};
    EXPECT_EQ(treeToVector(root), expected);
    
    freeTree(root);
}

// Test Case 7: Edge Case - Right-skewed lookalike reconstructed correctly
// A node with two children where the right child itself has children, validating depth tracking resetting.
TEST_F(RecoverFromPreorderTest, EdgeCase_RightBranchBacktrack) {
    string traversal = "1-2-3--4";
    TreeNode* root = solver.recoverFromPreorder(traversal);
    
    vector<int> expected = {1, 2, 3, -1, -1, 4};
    EXPECT_EQ(treeToVector(root), expected);
    
    freeTree(root);
}