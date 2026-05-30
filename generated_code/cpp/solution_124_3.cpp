#include <algorithm>
#include <climits>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * TreeNode *left;
 * TreeNode *right;
 * TreeNode() : val(0), left(nullptr), right(nullptr) {}
 * TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
private:
    int global_max_sum;

    // Helper function that returns the maximum path sum starting from the current node
    // and extending down into one of its subtrees.
    int calculateMaxGain(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }

        // Recursively find the max gain from left and right subtrees.
        // If the path sum from a subtree is negative, we drop it (take 0).
        int left_gain = std::max(calculateMaxGain(node->left), 0);
        int right_gain = std::max(calculateMaxGain(node->right), 0);

        // Price of a new path with the current node as the highest bridge node
        int current_path_sum = node->val + left_gain + right_gain;

        // Update the global maximum path sum found so far
        global_max_sum = std::max(global_max_sum, current_path_sum);

        // For the parent call, a path can only extend through one child
        return node->val + std::max(left_gain, right_gain);
    }

public:
    int maxPathSum(TreeNode* root) {
        // Initialize global maximum with the smallest possible integer to handle strictly negative nodes
        global_max_sum = INT_MIN;
        calculateMaxGain(root);
        return global_max_sum;
    }
};