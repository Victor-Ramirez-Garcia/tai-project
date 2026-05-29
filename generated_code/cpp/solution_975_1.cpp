#include <vector>
#include <algorithm>

// Definition for a binary tree node if not already defined by the environment.
// Included to ensure self-contained compilability.
#ifndef TREE_NODE_DEFINE
#define TREE_NODE_DEFINE
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
#endif

class Solution {
public:
    int rangeSumBST(TreeNode* root, int low, int high) {
        // Base case: if the node is null, it contributes 0 to the sum.
        if (!root) {
            return 0;
        }
        
        // If the current node's value is strictly less than 'low', 
        // then its entire left subtree will also be less than 'low' due to BST properties.
        // Thus, we only need to search the right subtree.
        if (root->val < low) {
            return rangeSumBST(root->right, low, high);
        }
        
        // If the current node's value is strictly greater than 'high',
        // then its entire right subtree will also be greater than 'high'.
        // Thus, we only need to search the left subtree.
        if (root->val > high) {
            return rangeSumBST(root->left, low, high);
        }
        
        // If the current node's value is within [low, high], it contributes to the sum.
        // We then recursively add the valid range sums from both its left and right subtrees.
        return root->val + rangeSumBST(root->left, low, high) + rangeSumBST(root->right, low, high);
    }
};