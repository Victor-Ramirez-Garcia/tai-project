#include <algorithm>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 * int val;
 * TreeNode *left;
 * TreeNode *right;
 * TreeNode() : val(0), left(nullptr), right(nullptr) {}
 * TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 * TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    /**
     * Algorithm Choice: Optimized DFS
     * * Key Property: The root value is the absolute minimum of the entire tree.
     * To find the second minimum, we look for the smallest value strictly greater than root->val.
     * * Pruning: If a node's value is already greater than the root's value, that node (and its entire subtree) 
     * cannot contain a smaller "second minimum candidate" than itself, because the root of any subtree
     * is the minimum of that subtree. Thus, we don't need to traverse deeper once we find a value > root->val.
     * * Time Complexity: O(N) in worst case (traversing all nodes), though often less due to pruning.
     * Space Complexity: O(H) where H is the height of the tree (recursion stack).
     */
    int findSecondMinimumValue(TreeNode* root) {
        if (!root) return -1;
        return dfs(root, root->val);
    }

private:
    long dfs(TreeNode* node, int minVal) {
        // Base case: if we reach a null or find a value greater than the tree minimum
        if (!node) return -1;
        
        if (node->val > minVal) {
            // This node is a candidate for the second minimum.
            // Since subtrees only contain values >= this node's value, we stop here.
            return node->val;
        }
        
        // If node->val == minVal, we must check its children to find a larger value
        long left = dfs(node->left, minVal);
        long right = dfs(node->right, minVal);
        
        // If both children return valid second minimum candidates, take the smaller one
        if (left != -1 && right != -1) {
            return std::min(left, right);
        }
        
        // If only one child (or neither) returned a valid candidate, return the non- -1 value
        return (left != -1) ? left : right;
    }
};