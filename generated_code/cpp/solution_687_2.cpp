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
public:
    int longestUnivaluePath(TreeNode* root) {
        int max_path = 0;
        dfs(root, max_path);
        return max_path;
    }

private:
    // This helper function returns the longest single-direction path starting 
    // from the current node going downwards, where all nodes have the same value.
    int dfs(TreeNode* node, int& max_path) {
        if (!node) return 0;

        // Recursively find the longest univalue path lengths in the left and right subtrees
        int left_len = dfs(node->left, max_path);
        int right_len = dfs(node->right, max_path);

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

        // Update the global maximum path which can combine both left and right directions
        max_path = std::max(max_path, left_arrow + right_arrow);

        // Return the max single-direction path extending from this node to its parent
        return std::max(left_arrow, right_arrow);
    }
};