#include <algorithm>

// Definition for a binary tree node provided for compilability.
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
    // Helper structure to hold the accumulated sum and count of nodes in a subtree.
    struct SubtreeResult {
        int sum;
        int count;
    };

    int matchingNodesCount = 0;

    // Post-order traversal (Bottom-Up DP) to compute subtree sums and counts efficiently.
    // Time Complexity: O(N) where N is the number of nodes, as each node is visited once.
    // Space Complexity: O(H) where H is the height of the tree, due to the recursion stack.
    SubtreeResult calculateSubtree(TreeNode* node) {
        if (!node) {
            return {0, 0};
        }

        // Recursively find the sum and count of the left and right subtrees
        SubtreeResult leftResult = calculateSubtree(node->left);
        SubtreeResult rightResult = calculateSubtree(node->right);

        // Current subtree metrics include the current node's value
        int currentSum = leftResult.sum + rightResult.sum + node->val;
        int currentCount = leftResult.count + rightResult.count + 1;

        // Calculate average using integer division (automatically truncates towards zero/rounds down for non-negative values)
        if (currentSum / currentCount == node->val) {
            matchingNodesCount++;
        }

        return {currentSum, currentCount};
    }

public:
    int averageOfSubtree(TreeNode* root) {
        matchingNodesCount = 0;
        calculateSubtree(root);
        return matchingNodesCount;
    }
};