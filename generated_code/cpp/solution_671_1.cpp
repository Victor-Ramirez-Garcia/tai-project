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
        // Base case: if the node is a leaf, it cannot have a strictly larger child value.
        // Also, if root is null (though the constraints state non-empty), return -1.
        if (!root || !root->left) return -1;
        
        // The root always holds the absolute minimum value of the entire tree.
        int rootVal = root->val;
        
        // If a child's value is greater than the root's value, that child's value 
        // is a candidate for the second minimum value in its subtree.
        // Otherwise, if the child's value equals the root's value, the second minimum 
        // value could be deeper in that child's subtree.
        int leftVal = (root->left->val > rootVal) ? root->left->val : findSecondMinimumValue(root->left);
        int rightVal = (root->right->val > rootVal) ? root->right->val : findSecondMinimumValue(root->right);
        
        // If both subtrees found a valid second minimum candidate, return the smaller one.
        if (leftVal != -1 && rightVal != -1) {
            return std::min(leftVal, rightVal);
        }
        
        // If only one subtree returned a valid candidate, return that candidate.
        // If neither found one, returns -1.
        return (leftVal != -1) ? leftVal : rightVal;
    }
};