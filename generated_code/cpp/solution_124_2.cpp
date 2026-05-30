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
    int max_sum;

    // Helper function that returns the maximum path sum starting from the current node
    // and extending into one of its subtrees. It also updates the global maximum path sum.
    int maxGain(TreeNode* node) {
        if (node == nullptr) {
            return 0;
        }

        // Recursively get the max gain from left and right subtrees.
        // If a subtree returns a negative gain, we choose not to include it (hence max(..., 0)).
        int leftGain = std::max(maxGain(node->left), 0);
        int rightGain = std::max(maxGain(node->right), 0);

        // Price of the new path would be the parent node value plus the gains from both children
        int currentPathSum = node->val + leftGain + rightGain;

        // Update the global maximum if the path rooted at the current node is better
        max_sum = std::max(max_sum, currentPathSum);

        // For the parent call, a path can only extend to one of the children
        return node->val + std::max(leftGain, rightGain);
    }

public:
    int maxPathSum(TreeNode* root) {
        max_sum = INT_MIN;
        maxGain(root);
        return max_sum;
    }
};