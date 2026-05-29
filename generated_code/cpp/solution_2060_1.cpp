#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <climits>

using namespace std;

// Definition for a binary tree node (self-contained requirement)
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
private:
    // Helper function to validate if the combined tree is a valid BST
    // and to count total unique nodes traversed during the process.
    bool isValidBST(TreeNode* root, long min_val, long max_val, int& count) {
        if (!root) return true;
        if (root->val <= min_val || root->val >= max_val) return false;
        
        count++; // Increment the count of visited nodes
        
        return isValidBST(root->left, min_val, root->val, count) &&
               isValidBST(root->right, root->val, max_val, count);
    }

public:
    TreeNode* canMerge(vector<TreeNode*>& trees) {
        // Map to store root value to its corresponding TreeNode pointer
        unordered_map<int, TreeNode*> root_map;
        // Set to track all leaf values across all trees
        unordered_set<int> leaves;
        
        // Step 1: Populate the root map and the leaves set
        for (TreeNode* tree : trees) {
            root_map[tree->val] = tree;
            if (tree->left) leaves.insert(tree->left->val);
            if (tree->right) leaves.insert(tree->right->val);
        }
        
        // Step 2: Find the global root.
        // The global root must be a root of one of the trees but cannot be a leaf of any tree.
        TreeNode* global_root = nullptr;
        for (TreeNode* tree : trees) {
            if (leaves.find(tree->val) == leaves.end()) {
                if (global_root != nullptr) {
                    // Multiple potential roots found, meaning the trees are disjoint
                    return nullptr;
                }
                global_root = tree;
            }
        }
        
        // If no root can be the global root, a single valid tree cannot be formed
        if (!global_root) return nullptr;
        
        // Step 3: Stitch the trees together by replacing leaves with corresponding roots
        for (TreeNode* tree : trees) {
            if (tree->left && root_map.count(tree->left->val)) {
                tree->left = root_map[tree->left->val];
            }
            if (tree->right && root_map.count(tree->right->val)) {
                tree->right = root_map[tree->right->val];
            }
        }
        
        // Step 4: Validate the final structure.
        // It must be a valid BST and must contain all unique nodes expected.
        int total_visited_nodes = 0;
        if (!isValidBST(global_root, LONG_MIN, LONG_MAX, total_visited_nodes)) {
            return nullptr;
        }
        
        // The total number of unique nodes in a correctly merged tree should equal
        // the total roots plus all leaves that weren't replaced by roots.
        // Alternatively, since each valid merge operation reduces the number of components by 1,
        // and we have n trees, we must ensure all trees are connected into a single component.
        // The number of unique values in root_map + leaves is exactly the total expected unique nodes.
        unordered_set<int> unique_vals;
        for (TreeNode* tree : trees) {
            unique_vals.insert(tree->val);
            if (tree->left) unique_vals.insert(tree->left->val);
            if (tree->right) unique_vals.insert(tree->right->val);
        }
        
        if (total_visited_nodes != unique_vals.size()) {
            return nullptr; // Cyclical or disconnected components exist
        }
        
        return global_root;
    }
};