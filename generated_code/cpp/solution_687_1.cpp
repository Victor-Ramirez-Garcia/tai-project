#include <algorithm>

// Definition for a binary tree node if not already defined by the environment.
// (Included here to satisfy the self-contained compilation requirement)
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
    int max_path = 0;

    // This helper function returns the length of the longest single-direction 
    // path starting from the current 'node' where all nodes have the same value.
    int dfs(TreeNode* node) {
        if (!node) return 0;

        // Recursively find the longest univalue paths in the left and right subtrees
        int left_len = dfs(node->left);
        int right_len = dfs(node->right);

        int left_arrow = 0;
        int right_arrow = 0;

        // If left child exists and has the same value, extend the left path
        if (node->left && node->left->val == node->val) {
            left_arrow = left_len + 1;
        }

        // If right child exists and has the same value, extend the right path
        if (node->right && node->right->val == node->val) {
            right_arrow = right_len + 1;
        }

        // Update the global maximum path which combines both left and right directions
        max_path = std::max(max_path, left_arrow + right_arrow);

        // Return the maximum single-direction path to the parent node
        return std::max(left_arrow, right_arrow);
    }

public:
    int longestUnivaluePath(TreeNode* root) {
        max_path = 0;
        dfs(root);
        return max_path;
    }
};