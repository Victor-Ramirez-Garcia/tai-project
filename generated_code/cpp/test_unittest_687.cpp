#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include "solution_proxy.h"

// Helper function to build a tree from a level-order vector (using -1001 or a similar marker for null is avoided by using std::vector<int> with a convention, but since Node.val >= -1000, we can use a special constant like -9999 for null)
const int null_node = -9999;

TreeNode* buildTree(const std::vector<int>& nodes) {
    if (nodes.empty() || nodes[0] == null_node) return nullptr;
    
    TreeNode* root = new TreeNode(nodes[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    
    size_t i = 1;
    while (!q.empty() && i < nodes.size()) {
        TreeNode* curr = q.front();
        q.pop();
        
        if (i < nodes.size() && nodes[i] != null_node) {
            curr->left = new TreeNode(nodes[i]);
            q.push(curr->left);
        }
        i++;
        
        if (i < nodes.size() && nodes[i] != null_node) {
            curr->right = new TreeNode(nodes[i]);
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

class LongestUnivaluePathTest : public ::testing::Test {
protected:
    Solution solver;
};

// Test Example 1 from problem description
TEST_F(LongestUnivaluePathTest, Example1) {
    std::vector<int> nodes = {5, 4, 5, 1, 1, null_node, 5};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solver.longestUnivaluePath(root), 2);
    freeTree(root);
}

// Test Example 2 from problem description
TEST_F(LongestUnivaluePathTest, Example2) {
    std::vector<int> nodes = {1, 4, 5, 4, 4, null_node, 5};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solver.longestUnivaluePath(root), 2);
    freeTree(root);
}

// Test Edge Case: Empty tree (0 nodes)
TEST_F(LongestUnivaluePathTest, EmptyTree) {
    TreeNode* root = nullptr;
    EXPECT_EQ(solver.longestUnivaluePath(root), 0);
}

// Test Edge Case: Single node tree
TEST_F(LongestUnivaluePathTest, SingleNode) {
    TreeNode* root = new TreeNode(1);
    EXPECT_EQ(solver.longestUnivaluePath(root), 0);
    freeTree(root);
}

// Test Edge Case: Minimum possible node values (-1000)
TEST_F(LongestUnivaluePathTest, MinimumNodeValues) {
    std::vector<int> nodes = {-1000, -1000, -1000};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solver.longestUnivaluePath(root), 2);
    freeTree(root);
}

// Test Edge Case: Maximum possible node values (1000)
TEST_F(LongestUnivaluePathTest, MaximumNodeValues) {
    std::vector<int> nodes = {1000, 1000, 1000};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solver.longestUnivaluePath(root), 2);
    freeTree(root);
}

// Test Case: Tree with all different values
TEST_F(LongestUnivaluePathTest, AllDifferentValues) {
    std::vector<int> nodes = {1, 2, 3, 4, 5, 6, 7};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solver.longestUnivaluePath(root), 0);
    freeTree(root);
}

// Test Case: Longest path does not pass through the root
TEST_F(LongestUnivaluePathTest, PathNotThroughRoot) {
    std::vector<int> nodes = {1, 2, 3, 2, 2, null_node, null_node};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solver.longestUnivaluePath(root), 1);
    freeTree(root);
}

// Test Case: Linear skewed tree (all same values)
TEST_F(LongestUnivaluePathTest, SkewedTreeSameValues) {
    std::vector<int> nodes = {5, 5, null_node, 5, null_node, 5, null_node};
    TreeNode* root = buildTree(nodes);
    EXPECT_EQ(solver.longestUnivaluePath(root), 3);
    freeTree(root);
}