#include <iostream>

// Definition for a binary tree node if not already defined by the runner environment.
// The problem statement requires a self-contained compilable structure.
#ifndef TREE_NODE_DEFINED
#define TREE_NODE_DEFINED
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
#endif

class Solution {
private:
    int running_sum = 0;

    // Helper function for reverse in-order traversal (Right -> Node -> Left).
    // In a BST, this visits nodes in descending order, allowing us to maintain
    // a running sum of all greater elements processed so far.
    void reverseInorder(TreeNode* node) {
        if (!node) {
            return;
        }

        // Traverse the right subtree first (larger elements)
        reverseInorder(node->right);

        // Update the running sum and the current node's value
        running_sum += node->val;
        node->val = running_sum;

        // Traverse the left subtree (smaller elements)
        reverseInorder(node->left);
    }

public:
    TreeNode* bstToGst(TreeNode* root) {
        running_sum = 0;
        reverseInorder(root);
        return root;
    }
};