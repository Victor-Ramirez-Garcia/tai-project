#include <gtest/gtest.h>
#include <limits>
#include <vector>
#include "solution_proxy.h"

/**
 * Test suite for the Validate Binary Search Tree problem.
 * Validates the Solution::isValidBST(TreeNode* root) method.
 */

class ValidateBSTTest : public ::testing::Test {
protected:
    // Helper function to clean up tree memory to prevent leaks
    void deleteTree(TreeNode* root) {
        if (!root) return;
        deleteTree(root->left);
        deleteTree(root->right);
        delete root;
    }
};

TEST_F(ValidateBSTTest, Example1_SimpleValidBST) {
    // Input: root = [2,1,3]
    TreeNode* root = new TreeNode(2);
    root->left = new TreeNode(1);
    root->right = new TreeNode(3);

    Solution sol;
    EXPECT_TRUE(sol.isValidBST(root));

    deleteTree(root);
}

TEST_F(ValidateBSTTest, Example2_InvalidBSTSubtree) {
    // Input: root = [5,1,4,null,null,3,6]
    // 4 is the right child of 5, but its left child is 3 (invalid)
    TreeNode* root = new TreeNode(5);
    root->left = new TreeNode(1);
    root->right = new TreeNode(4);
    root->right->left = new TreeNode(3);
    root->right->right = new TreeNode(6);

    Solution sol;
    EXPECT_FALSE(sol.isValidBST(root));

    deleteTree(root);
}

TEST_F(ValidateBSTTest, SingleNode_Valid) {
    // A single node is a valid BST
    TreeNode* root = new TreeNode(1);

    Solution sol;
    EXPECT_TRUE(sol.isValidBST(root));

    deleteTree(root);
}

TEST_F(ValidateBSTTest, DuplicateValues_Invalid) {
    // BST must be strictly less than/greater than
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(1);

    Solution sol;
    EXPECT_FALSE(sol.isValidBST(root));

    deleteTree(root);
}

TEST_F(ValidateBSTTest, OutOfBoundsSubtree_Invalid) {
    // Node is valid relative to parent but invalid relative to ancestor
    //      10
    //     /  \
    //    5    15
    //        /  \
    //       6    20
    // 6 is in the right subtree of 10, but 6 < 10 (invalid)
    TreeNode* root = new TreeNode(10);
    root->left = new TreeNode(5);
    root->right = new TreeNode(15);
    root->right->left = new TreeNode(6);
    root->right->right = new TreeNode(20);

    Solution sol;
    EXPECT_FALSE(sol.isValidBST(root));

    deleteTree(root);
}

TEST_F(ValidateBSTTest, INT_MIN_INT_MAX_Constraints) {
    // Testing boundary values for integer overflow issues
    TreeNode* root = new TreeNode(std::numeric_limits<int>::max());
    root->left = new TreeNode(std::numeric_limits<int>::min());

    Solution sol;
    EXPECT_TRUE(sol.isValidBST(root));

    // Adding an invalid node at the boundary
    root->left->left = new TreeNode(std::numeric_limits<int>::min());
    EXPECT_FALSE(sol.isValidBST(root));

    deleteTree(root);
}

TEST_F(ValidateBSTTest, EmptyTree_Valid) {
    // Depending on interpretation, an empty tree is usually considered a valid BST
    Solution sol;
    EXPECT_TRUE(sol.isValidBST(nullptr));
}

TEST_F(ValidateBSTTest, LeftSkewed_Valid) {
    TreeNode* root = new TreeNode(3);
    root->left = new TreeNode(2);
    root->left->left = new TreeNode(1);

    Solution sol;
    EXPECT_TRUE(sol.isValidBST(root));

    deleteTree(root);
}

TEST_F(ValidateBSTTest, RightSkewed_Valid) {
    TreeNode* root = new TreeNode(1);
    root->right = new TreeNode(2);
    root->right->right = new TreeNode(3);

    Solution sol;
    EXPECT_TRUE(sol.isValidBST(root));

    deleteTree(root);
}