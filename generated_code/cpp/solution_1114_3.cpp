#include <iostream>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    int running_sum = 0;

    // Helper function to perform reverse in-order traversal (Right -> Root -> Left).
    // In a BST, standard in-order visits nodes in ascending order.
    // Reverse in-order visits nodes in descending order, allowing us to maintain
    // a running sum of all larger keys processed so far.
    void traverse(TreeNode* node) {
        if (!node) {
            return;
        }

        // 1. Visit the right subtree first (all values greater than current node)
        traverse(node->right);

        // 2. Process the current node
        running_sum += node->val;
        node->val = running_sum;

        // 3. Visit the left subtree (all values smaller than current node)
        traverse(node->left);
    }

public:
    TreeNode* bstToGst(TreeNode* root) {
        running_sum = 0;
        traverse(root);
        return root;
    }
};