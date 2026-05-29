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
        // Base case: if we reach a null node, target is not in this path.
        if (original == nullptr) {
            return nullptr;
        }
        
        // If the current node in the original tree is the target,
        // the corresponding node in the cloned tree is our answer.
        if (original == target) {
            return cloned;
        }
        
        // Recursively search the left subtree.
        TreeNode* leftResult = getTargetCopy(original->left, cloned->left, target);
        if (leftResult != nullptr) {
            return leftResult;
        }
        
        // If not found in the left subtree, search and return the result from the right subtree.
        return getTargetCopy(original->right, cloned->right, target);
    }
};