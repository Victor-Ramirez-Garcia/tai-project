#include <iostream>

// Definition for a binary tree node if not already defined by the environment.
// The problem statement provides this definition, so we ensure it is available.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        // Base case: if we reach a null node, return null.
        if (original == nullptr) {
            return nullptr;
        }
        
        // If the current node in the original tree is the target,
        // then the corresponding node in the cloned tree is our answer.
        if (original == target) {
            return cloned;
        }
        
        // Recurse on the left subtree.
        TreeNode* leftResult = getTargetCopy(original->left, cloned->left, target);
        if (leftResult != nullptr) {
            return leftResult;
        }
        
        // Recurse on the right subtree if target wasn't found in the left subtree.
        return getTargetCopy(original->right, cloned->right, target);
    }
};