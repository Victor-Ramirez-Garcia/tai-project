#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include "solution_proxy.h"

// Helper function to build a tree from a level-order vector with -1 representing null
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

// Helper function to free the allocated memory for the tree
void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

class AverageOfSubtreeTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case: Example 1 from problem description
TEST_F(AverageOfSubtreeTest, Example1_NormalTree) {
    // Tree: [4,8,5,0,1,-1,6] -> -1 represents null
    std::vector<int> nodes = {4, 8, 5, 0, 1, -1, 6};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.averageOfSubtree(root), 5);
    
    freeTree(root);
}

// Test Case: Example 2 from problem description (Single node tree)
TEST_F(AverageOfSubtreeTest, Example2_SingleNode) {
    std::vector<int> nodes = {1};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.averageOfSubtree(root), 1);
    
    freeTree(root);
}

// Test Case: Empty tree boundary condition
TEST_F(AverageOfSubtreeTest, EdgeCase_EmptyTree) {
    TreeNode* root = nullptr;
    
    EXPECT_EQ(solution.averageOfSubtree(root), 0);
}

// Test Case: Node values resulting in rounding down operations
TEST_F(AverageOfSubtreeTest, Scenario_RoundingDownAverage) {
    // Subtree at root 5 has children 6 and 7. Total sum = 18, count = 3. Avg = 6. 
    // Subtree at 6 has child 4. Total sum = 10, count = 2. Avg = 5. (6 != 5)
    // Leaf nodes 7 and 4 match their averages.
    std::vector<int> nodes = {5, 6, 7, 4};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.averageOfSubtree(root), 2); // only 7 and 4 match
    
    freeTree(root);
}

// Test Case: Deep skewed tree (All left children) to test deep recursion or straight paths
TEST_F(AverageOfSubtreeTest, Scenario_SkewedLeftTree) {
    // Tree: 3 -> 2 -> 1
    // Node 1: sum=1, count=1, avg=1 (Match)
    // Node 2: sum=3, count=2, avg=1 (No Match)
    // Node 3: sum=6, count=3, avg=2 (No Match)
    std::vector<int> nodes = {3, 2, -1, 1};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.averageOfSubtree(root), 1);
    
    freeTree(root);
}

// Test Case: Node values equal to 0 to test zero handling in division/summation
TEST_F(AverageOfSubtreeTest, Scenario_AllZeroNodes) {
    std::vector<int> nodes = {0, 0, 0, 0};
    TreeNode* root = buildTree(nodes);
    
    EXPECT_EQ(solution.averageOfSubtree(root), 4); // All nodes will match 0 == 0/count
    
    freeTree(root);
}