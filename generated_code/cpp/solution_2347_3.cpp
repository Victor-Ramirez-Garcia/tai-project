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
    // Structure to return both the sum and the count of nodes in a subtree
    struct SubtreeInfo {
        int sum;
        int count;
    };

    int matchingNodesCount = 0;

    // Post-order traversal to calculate sum and count bottom-up
    // Time Complexity: O(N) - visits each node exactly once
    // Space Complexity: O(H) - where H is the height of the tree (recursion stack)
    SubtreeInfo calculateSubtree(TreeNode* node) {
        if (!node) {
            return {0, 0};
        }

        // Divide: Process left and right subtrees
        SubtreeInfo leftInfo = calculateSubtree(node->left);
        SubtreeInfo rightInfo = calculateSubtree(node->right);

        // Conquer: Combine results for the current subtree
        int totalSum = leftInfo.sum + rightInfo.sum + node->val;
        int totalCount = leftInfo.count + rightInfo.count + 1;

        // Check if the current node meets the condition (integer division truncates towards zero/rounds down)
        if (totalSum / totalCount == node->val) {
            matchingNodesCount++;
        }

        return {totalSum, totalCount};
    }

public:
    int averageOfSubtree(TreeNode* root) {
        matchingNodesCount = 0;
        calculateSubtree(root);
        return matchingNodesCount;
    }
};