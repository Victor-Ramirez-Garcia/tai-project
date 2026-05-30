#include <algorithm>
#include <climits>

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
    int max_sum;

    // Helper function that returns the maximum path sum starting from the current node
    // and extending down into one of its subtrees.
    int calculateMaxGain(TreeNode* node) {
        if (!node) {
            return 0;
        }

        // Recursively find the maximum path sum of the left and right subtrees.
        // If a subtree returns a negative sum, we choose not to include it (hence std::max(..., 0)).
        int left_gain = std::max(calculateMaxGain(node->left), 0);
        int right_gain = std::max(calculateMaxGain(node->right), 0);

        // Price of a new path where the current node is the highest node (the "turn" point).
        int current_path_sum = node->val + left_gain + right_gain;

        // Update the global maximum path sum found so far.
        max_sum = std::max(max_sum, current_path_sum);

        // For the parent call, we can only choose one child path to maintain a valid path.
        return node->val + std::max(left_gain, right_gain);
    }

public:
    int maxPathSum(TreeNode* root) {
        max_sum = INT_MIN;
        calculateMaxGain(root);
        return max_sum;
    }
};