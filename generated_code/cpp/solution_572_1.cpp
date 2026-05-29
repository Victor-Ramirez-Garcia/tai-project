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
    // Helper function to check if two trees are structurally identical with the same values.
    // Time Complexity: O(M), where M is the number of nodes in subRoot.
    // Space Complexity: O(H_sub), where H_sub is the height of subRoot (due to the recursion stack).
    bool isSameTree(TreeNode* s, TreeNode* t) {
        if (!s && !t) return true;
        if (!s || !t) return false;
        return (s->val == t->val) && isSameTree(s->left, t->left) && isSameTree(s->right, t->right);
    }

    // Main function to check if subRoot is a subtree of root.
    // Algorithm: Depth First Search (DFS) / Preorder Traversal.
    // Time Complexity: O(N * M) in the worst case (e.g., all nodes have the same value),
    // where N is the number of nodes in root and M is the number of nodes in subRoot.
    // Space Complexity: O(H_root) for the recursion stack, where H_root is the height of root.
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // If the main tree is null, it cannot contain a non-empty subRoot.
        if (!root) return false;
        
        // Check if the current tree rooted at 'root' is identical to 'subRoot'.
        if (isSameTree(root, subRoot)) return true;
        
        // Otherwise, recursively check the left and right subtrees.
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }
};