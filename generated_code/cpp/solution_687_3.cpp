#include <algorithm>

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
    int max_path = 0;

    // Post-order traversal dfs returns the longest univalue path starting from the current node
    // and extending into one of its subtrees.
    int dfs(TreeNode* node) {
        if (!node) return 0;

        // Recursively find the longest univalue paths in the left and right subtrees
        int left_length = dfs(node->left);
        int right_length = dfs(node->right);

        int left_arrow = 0;
        int right_arrow = 0;

        // If left child exists and has the same value, extend the path
        if (node->left && node->left->val == node->val) {
            left_arrow = left_length + 1;
        }

        // If right child exists and has the same value, extend the path
        if (node->right && node->right->val == node->val) {
            right_arrow = right_length + 1;
        }

        // Update the global maximum path length which can combine both left and right directions
        max_path = std::max(max_path, left_arrow + right_arrow);

        // Return the longest single path extending to a subtree to the parent call
        return std::max(left_arrow, right_arrow);
    }

public:
    int longestUnivaluePath(TreeNode* root) {
        max_path = 0;
        dfs(root);
        return max_path;
    }
};