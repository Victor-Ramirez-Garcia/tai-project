#include <vector>
#include <algorithm>
#include <queue>

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
    int rangeSumBST(TreeNode* root, int low, int high) {
        // Base case: if the node is null, it contributes 0 to the sum.
        if (!root) {
            return 0;
        }

        // Case 1: The current node value is smaller than 'low'.
        // Since it's a BST, all nodes in the left subtree will also be smaller than 'low'.
        // Therefore, we only need to search the right subtree.
        if (root->val < low) {
            return rangeSumBST(root->right, low, high);
        }

        // Case 2: The current node value is greater than 'high'.
        // All nodes in the right subtree will also be greater than 'high'.
        // Therefore, we only need to search the left subtree.
        if (root->val > high) {
            return rangeSumBST(root->left, low, high);
        }

        // Case 3: The current node value is within the inclusive range [low, high].
        // We include its value and recursively search both the left and right subtrees.
        return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
    }
};