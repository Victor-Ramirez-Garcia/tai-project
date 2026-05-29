#include <iostream>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        // Base case: if we reach a null node, return null
        if (original == nullptr) {
            return nullptr;
        }
        
        // If the current node in the original tree is the target,
        // then the corresponding node in the cloned tree is our answer.
        if (original == target) {
            return cloned;
        }
        
        // Search in the left subtree
        TreeNode* left_result = getTargetCopy(original->left, cloned->left, target);
        if (left_result != nullptr) {
            return left_result;
        }
        
        // If not found in the left subtree, search and return the result from the right subtree
        return getTargetCopy(original->right, cloned->right, target);
    }
};