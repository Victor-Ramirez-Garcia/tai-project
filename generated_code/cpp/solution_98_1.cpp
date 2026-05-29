#include <climits>

// Definition for a binary tree node.
// Included to make the code fully self-contained and compilable.
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
        // We use long long tracking boundaries to prevent integer overflow issues 
        // with INT_MIN and INT_MAX node values.
        return validate(root, LLONG_MIN, LLONG_MAX);
    }

private:
    // Helper function that leverages a top-down DFS approach to pass down 
    // valid open-ended intervals for each node.
    // Time Complexity: O(N) where N is the number of nodes, as we visit each node once.
    // Space Complexity: O(H) where H is the height of the tree, due to the recursion stack.
    bool validate(TreeNode* node, long long low, long long high) {
        // An empty tree/sub-tree is inherently a valid BST.
        if (node == nullptr) {
            return true;
        }

        // The current node's value must strictly fall within the range (low, high).
        if (node->val <= low || node->val >= high) {
            return false;
        }

        // Recursively validate left and right subtrees:
        // For the left child, the upper limit updates to the current node's value.
        // For the right child, the lower limit updates to the current node's value.
        return validate(node->left, low, node->val) && validate(node->right, node->val, high);
    }
};