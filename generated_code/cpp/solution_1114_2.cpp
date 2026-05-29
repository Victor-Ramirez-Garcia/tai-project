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

    // Helper function for reverse in-order traversal (Right -> Node -> Left)
    // This allows us to visit nodes in descending order of their values.
    void convert(TreeNode* node) {
        if (!node) {
            return;
        }

        // 1. Traverse the right subtree first (larger values)
        convert(node->right);

        // 2. Process the current node
        running_sum += node->val;
        node->val = running_sum;

        // 3. Traverse the left subtree (smaller values)
        convert(node->left);
    }

public:
    TreeNode* bstToGst(TreeNode* root) {
        running_sum = 0;
        convert(root);
        return root;
    }
};