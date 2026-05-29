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
    int findSecondMinimumValue(TreeNode* root) {
        // Base case: if the root is null or a leaf node, there's no second minimum.
        if (!root || !root->left) return -1;
        
        // Since root.val is the minimum of its children, the smallest value in the 
        // whole tree is always root->val.
        int left_val = root->left->val;
        int right_val = root->right->val;
        
        // If the left child's value equals the root's value, the second minimum 
        // could be located deeper in the left subtree. We recursively search for it.
        if (left_val == root->val) {
            left_val = findSecondMinimumValue(root->left);
        }
        
        // Similarly, if the right child's value equals the root's value, the second 
        // minimum could be located deeper in the right subtree.
        if (right_val == root->val) {
            right_val = findSecondMinimumValue(root->right);
        }
        
        // If both subtrees returned a valid second minimum, the overall second 
        // minimum for the current root is the smaller of the two.
        if (left_val != -1 && right_val != -1) {
            return std::min(left_val, right_val);
        }
        
        // If only one subtree returned a valid second minimum, return that one.
        // If both returned -1, then -1 is returned.
        return left_val != -1 ? left_val : right_val;
    }
};