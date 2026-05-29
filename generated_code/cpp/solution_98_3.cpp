#include <iostream>
#include <limits>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    /**
     * Algorithm: Recursive Range Validation
     * Time Complexity: O(N) where N is the number of nodes in the tree, as we visit each node once.
     * Space Complexity: O(H) where H is the height of the tree, representing the recursion stack depth.
     * 
     * To be a valid BST, every node must satisfy a specific range (min, max).
     * Using long long handles edge cases where node values are INT_MIN or INT_MAX.
     */
    bool isValidBST(TreeNode* root) {
        return validate(root, std::numeric_limits<long long>::min(), std::numeric_limits<long long>::max());
    }

private:
    bool validate(TreeNode* node, long long min_val, long long max_val) {
        // Base case: An empty tree/leaf child is a valid BST
        if (!node) {
            return true;
        }

        // The current node's value must be strictly within the range (min_val, max_val)
        if (node->val <= min_val || node->val >= max_val) {
            return false;
        }

        // Recursively check subtrees:
        // Left child must be less than current node value (updates max_val)
        // Right child must be greater than current node value (updates min_val)
        return validate(node->left, min_val, node->val) && 
               validate(node->right, node->val, max_val);
    }
};