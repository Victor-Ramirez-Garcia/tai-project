#include <iostream>

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
    // Helper function to check if two trees are completely identical
    bool isSameTree(TreeNode* p, TreeNode* q) {
    // Both are null, so they are identical
    if (!p && !q) return true;
    // One is null and the other isn't, so they aren't identical
    if (!p || !q) return false;
        // Check if current values match and structurally identical on left and right subtrees
        return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }

    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // A null tree cannot contain any subtree (given subRoot has at least 1 node per constraints)
        if (!root) return false;
        
        // If the tree rooted at 'root' is identical to 'subRoot', we found it
        if (isSameTree(root, subRoot)) return true;
        
        // Otherwise, recursively check if 'subRoot' is a subtree of the left or right child
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

};