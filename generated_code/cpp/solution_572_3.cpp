#include <vector>
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
public:
    // Main function to check if subRoot is a subtree of root.
    // Time Complexity: O(N * M) in the worst case, where N is the number of nodes in 'root'
    // and M is the number of nodes in 'subRoot'.
    // Space Complexity: O(H_root) due to the recursion stack, where H_root is the height of 'root'.
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        // If the main tree is empty, it cannot contain any non-empty subtree.
        if (!root) {
            return false;
        }
        
        // If the current structures match, return true.
        if (isSameTree(root, subRoot)) {
            return true;
        }
        
        // Otherwise, recursively check the left and right subtrees of the main tree.
        return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    }

private:
    // Helper function to check if two trees are identical in structure and values.
    bool isSameTree(TreeNode* p, TreeNode* q) {
        // If both nodes are null, they are identical.
        if (!p && !q) {
            return true;
        }
        // If only one of them is null, or their values differ, they are not identical.
        if (!p || !q || p->val != q->val) {
            return false;
        }
        // Recursively check both left and right children.
        return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};