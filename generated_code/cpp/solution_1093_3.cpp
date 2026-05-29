#include <string>
#include <vector>
#include <stack>

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
        // Stack to keep track of the path from the root to the current node.
        // The size of the stack matches the depth of the next node to be inserted.
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
            while (i < n && traversal[i] != '-') {
                val = val * 10 + (traversal[i] - '0');
                i++;
            }
            
            TreeNode* node = new TreeNode(val);
            
            // If the stack size is greater than the current depth, it means we have 
            // finished processing the subtree of the deeper nodes, so we pop them.
            while (path.size() > depth) {
                path.pop_back();
            }
            
            // Attach the node to its parent if the stack is not empty
            if (!path.empty()) {
                if (!path.back()->left) {
                    path.back()->left = node;
                } else {
                    path.back()->right = node;
                }
            }
            
            // Push the current node onto the path stack
            path.push_back(node);
        }
        
        // The first element in the path is always the root of the tree
        return path[0];
    }
};