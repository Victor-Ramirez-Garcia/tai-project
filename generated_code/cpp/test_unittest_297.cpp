#include <gtest/gtest.h>
#include <string>
#include <vector>
#include <queue>
#include "solution_proxy.h"

// Helper function to compare two binary trees for equality.
bool isSameTree(TreeNode* p, TreeNode* q) {
    if (!p && !q) return true;
    if (!p || !q) return false;
    return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

// Helper function to delete a dynamically allocated binary tree.
void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

// Test case for Example 1: Standard asymmetric binary tree.
TEST(CodecTest, Example1_StandardTree) {
    TreeNode* root = new TreeNode(1);
    root->left = new TreeNode(2);
    root->right = new TreeNode(3);
    root->right->left = new TreeNode(4);
    root->right->right = new TreeNode(5);

    Codec ser, deser;
    std::string serialized = ser.serialize(root);
    TreeNode* deserializedRoot = deser.deserialize(serialized);

    EXPECT_TRUE(isSameTree(root, deserializedRoot));

    freeTree(root);
    freeTree(deserializedRoot);
}

// Test case for Example 2: Empty tree (Edge case: minimum number of nodes).
TEST(CodecTest, Example2_EmptyTree) {
    TreeNode* root = nullptr;

    Codec ser, deser;
    std::string serialized = ser.serialize(root);
    TreeNode* deserializedRoot = deser.deserialize(serialized);

    EXPECT_TRUE(isSameTree(root, deserializedRoot));

    freeTree(root);
    freeTree(deserializedRoot);
}

// Test case for Edge Case: Single node tree.
TEST(CodecTest, EdgeCase_SingleNode) {
    TreeNode* root = new TreeNode(42);

    Codec ser, deser;
    std::string serialized = ser.serialize(root);
    TreeNode* deserializedRoot = deser.deserialize(serialized);

    EXPECT_TRUE(isSameTree(root, deserializedRoot));

    freeTree(root);
    freeTree(deserializedRoot);
}

// Test case for Edge Case: Negative and minimum/maximum constraint node values.
TEST(CodecTest, EdgeCase_BoundaryNodeValues) {
    TreeNode* root = new TreeNode(-1000);
    root->left = new TreeNode(1000);
    root->right = new TreeNode(0);

    Codec ser, deser;
    std::string serialized = ser.serialize(root);
    TreeNode* deserializedRoot = deser.deserialize(serialized);

    EXPECT_TRUE(isSameTree(root, deserializedRoot));

    freeTree(root);
    freeTree(deserializedRoot);
}

// Test case for Edge Case: Skewed tree (left-leaning chain simulating maximum depth scenario).
TEST(CodecTest, EdgeCase_LeftSkewedTree) {
    TreeNode* root = new TreeNode(1);
    TreeNode* curr = root;
    for (int i = 2; i <= 10; ++i) {
        curr->left = new TreeNode(i);
        curr = curr->left;
    }

    Codec ser, deser;
    std::string serialized = ser.serialize(root);
    TreeNode* deserializedRoot = deser.deserialize(serialized);

    EXPECT_TRUE(isSameTree(root, deserializedRoot));

    freeTree(root);
    freeTree(deserializedRoot);
}

// Test case for Edge Case: Skewed tree (right-leaning chain simulating maximum depth scenario).
TEST(CodecTest, EdgeCase_RightSkewedTree) {
    TreeNode* root = new TreeNode(1);
    TreeNode* curr = root;
    for (int i = 2; i <= 10; ++i) {
        curr->right = new TreeNode(i);
        curr = curr->right;
    }

    Codec ser, deser;
    std::string serialized = ser.serialize(root);
    TreeNode* deserializedRoot = deser.deserialize(serialized);

    EXPECT_TRUE(isSameTree(root, deserializedRoot));

    freeTree(root);
    freeTree(deserializedRoot);
}