#include <optional>

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
    bool isValidBST(TreeNode* root) {
        // Use std::optional<int> to handle the full range of int values safely without overflow risks.
        return validate(root, std::nullopt, std::nullopt);
    }

private:
    // Helper function that uses recursion with strict upper and lower bounds.
    // Time Complexity: O(N) where N is the number of nodes, as we visit each node exactly once.
    // Space Complexity: O(H) where H is the height of the tree, representing the recursion stack depth.
    bool validate(TreeNode* node, std::optional<int> low, std::optional<int> high) {
        // An empty tree/node is a valid BST.
        if (!node) {
            return true;
        }

        // The current node's value must be strictly greater than the lower bound (if it exists).
        if (low && node->val <= *low) {
            return false;
        }
        // The current node's value must be strictly less than the upper bound (if it exists).
        if (high && node->val >= *high) {
            return false;
        }

        // Recursively validate the left and right subtrees with updated bounds.
        // Left subtree values must be strictly less than the current node's value.
        // Right subtree values must be strictly greater than the current node's value.
        return validate(node->left, low, node->val) && validate(node->right, node->val, high);
    }
};