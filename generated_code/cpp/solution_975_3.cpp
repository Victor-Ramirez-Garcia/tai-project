#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

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
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        // Base case: if the current node is null, its contribution to the sum is 0.
        if (root == nullptr) {
            return 0;
        }

        // Case 1: Current node's value is greater than 'high'.
        // Since it's a BST, all nodes in the right subtree will also be greater than 'high'.
        // Therefore, we only need to search the left subtree.
        if (root->val > high) {
            return rangeSumBST(root->left, low, high);
        }

        // Case 2: Current node's value is less than 'low'.
        // Since it's a BST, all nodes in the left subtree will also be less than 'low'.
        // Therefore, we only need to search the right subtree.
        if (root->val < low) {
            return rangeSumBST(root->right, low, high);
        }

        // Case 3: Current node's value is within the inclusive range [low, high].
        // We include the current node's value and recursively search both subtrees.
        return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
    }
};