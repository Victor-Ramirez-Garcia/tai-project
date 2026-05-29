#include <string>
#include <vector>
#include <cctype>

using namespace std;

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
    TreeNode* recoverFromPreorder(string traversal) {
        // A stack to keep track of the current path from the root down to the last processed node.
        // The size of the stack at any point matches the depth of the node being evaluated.
        vector<TreeNode*> path;
        int i = 0;
        int n = traversal.length();
        
        while (i < n) {
            // Count the number of dashes to determine the depth of the current node
            int depth = 0;
            while (i < n && traversal[i] == '-') {
                depth++;
                i++;
            }
            
            // Extract the value of the current node
            int val = 0;
            while (i < n && isdigit(traversal[i])) {
                val = val * 10 + (traversal[i] - '0');
                i++;
            }
            
            // Create the new node
            TreeNode* node = new TreeNode(val);
            
            // If the stack size is greater than the current depth, it means we have finished 
            // processing the subtrees of the deeper nodes, so we pop them until we reach the parent.
            while (path.size() > depth) {
                path.pop_back();
            }
            
            // If the path is not empty, attach the current node to its parent
            if (!path.empty()) {
                if (path.back()->left == nullptr) {
                    // The problem guarantees that if a node has only one child, it's the left child.
                    path.back()->left = node;
                } else {
                    path.back()->right = node;
                }
            }
            
            // Push the current node onto the stack path
            path.push_back(node);
        }
        
        // The first node pushed to the stack is the root of the tree
        return path.empty() ? nullptr : path.front();
    }
};