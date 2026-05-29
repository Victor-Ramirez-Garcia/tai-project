#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include "solution_proxy.h"

// Helper function to build a tree from a level-order vector (using -1 for null/empty nodes as per constraint Node.val >= 1)
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

class SecondMinimumValueTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case 1: Provided Example 1
// Tree: [2, 2, 5, null, null, 5, 7]
// Expected: 5
TEST_F(SecondMinimumValueTest, Example1_StandardCase) {
    std::vector<int> nodes = {2, 2, 5, -1, -1, 5, 7};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.findSecondMinimumValue(root), 5);
    
    freeTree(root);
}

// Test Case 2: Provided Example 2
// Tree: [2, 2, 2]
// Expected: -1 (No second minimum exists)
TEST_F(SecondMinimumValueTest, Example2_AllNodesEqual) {
    std::vector<int> nodes = {2, 2, 2};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.findSecondMinimumValue(root), -1);
    
    freeTree(root);
}

// Test Case 3: Minimum size constraint (Single node tree)
// Tree: [5]
// Expected: -1
TEST_F(SecondMinimumValueTest, EdgeCase_SingleNodeTree) {
    std::vector<int> nodes = {5};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.findSecondMinimumValue(root), -1);
    
    freeTree(root);
}

// Test Case 4: Values at maximum boundary (2^31 - 1)
// Tree: [2, 2, 2147483647]
// Expected: 2147483647
TEST_F(SecondMinimumValueTest, EdgeCase_MaxIntValue) {
    std::vector<int> nodes = {2, 2, 2147483647};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.findSecondMinimumValue(root), 2147483647);
    
    freeTree(root);
}

// Test Case 5: Second minimum is on the left subtree instead of right
// Tree: [3, 4, 3, 4, 5]
// Expected: 4
TEST_F(SecondMinimumValueTest, Scenario_SecondMinimumOnLeft) {
    std::vector<int> nodes = {3, 4, 3, 4, 5};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.findSecondMinimumValue(root), 4);
    
    freeTree(root);
}

// Test Case 6: Deep skewed tree property holding root.val == min(left, right)
// Tree: [1, 1, 3, 1, 2]
// Expected: 2
TEST_F(SecondMinimumValueTest, Scenario_DeepTreeMultipleValues) {
    std::vector<int> nodes = {1, 1, 3, 1, 2};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.findSecondMinimumValue(root), 2);
    
    freeTree(root);
}