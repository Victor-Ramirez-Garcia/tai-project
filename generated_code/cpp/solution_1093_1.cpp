#include <string>
#include <vector>
#include <cctype>

using namespace std;

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
    TreeNode* recoverFromPreorder(string traversal) {
        // We use a vector to act as a stack to keep track of the path from the root
        // to the current node. The size of the stack represents the depth of the 
        // nodes currently being processed.
        vector<TreeNode*> path;
        int i = 0;
        int n = traversal.length();
        
        while (i < n) {
            // Count the number of dashes to determine the depth of the current node.
            int depth = 0;
            while (i < n && traversal[i] == '-') {
                depth++;
                i++;
            }
            
            // Read the integer value of the current node.
            int val = 0;
            while (i < n && isdigit(traversal[i])) {
                val = val * 10 + (traversal[i] - '0');
                i++;
            }
            
            TreeNode* node = new TreeNode(val);
            
            // If the path depth is greater than the current node's depth,
            // it means we have finished processing the subtrees of the previous 
            // deeper nodes. Pop them from the path until we find the parent node.
            while (path.size() > depth) {
                path.pop_back();
            }
            
            // If the path is not empty, attach the current node to its parent.
            if (!path.empty()) {
                // Preorder traversal ensures the left child is always processed first.
                // If the left child is already populated, this node must be the right child.
                if (!path.back()->left) {
                    path.back()->left = node;
                } else {
                    path.back()->right = node;
                }
            }
            
            // Add the current node to the path stack.
            path.push_back(node);
        }
        
        // The first element in the path stack is the root of the recovered binary tree.
        return path.empty() ? nullptr : path[0];
    }
};