#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <climits>

using namespace std;

// Definition for a binary tree node (included for self-containment/compilability).
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
    TreeNode* canMerge(vector<TreeNode*>& trees) {
        // Map to quickly look up root nodes by their value.
        unordered_map<int, TreeNode*> roots;
        // Set to collect all unique leaf values across all trees.
        unordered_set<int> leaves;

        for (TreeNode* tree : trees) {
            roots[tree->val] = tree;
            if (tree->left) leaves.insert(tree->left->val);
            if (tree->right) leaves.insert(tree->right->val);
        }

        // The overall root must be a root node that is NOT any other tree's leaf.
        TreeNode* globalRoot = nullptr;
        for (TreeNode* tree : trees) {
            if (leaves.find(tree->val) == leaves.end()) {
                if (globalRoot != nullptr) {
                    // More than one potential root means the components cannot be fully connected.
                    return nullptr;
                }
                globalRoot = tree;
            }
        }

        // If no root can act as the global root, it's impossible to merge them.
        if (!globalRoot) return nullptr;

        // Count of unique nodes visited during validation.
        int count = 0;

        // Traverse and validate the tree using strict min/max boundaries to ensure it's a BST.
        // Also perform the logical merging inline via the 'roots' map.
        if (!isValidBST(globalRoot, INT_MIN, INT_MAX, roots, count)) {
            return nullptr;
        }

        // If the number of processed roots matches the initial number of trees,
        // it means all trees were successfully attached to the single global tree.
        return count == trees.size() ? globalRoot : nullptr;
    }

private:
    bool isValidBST(TreeNode* node, int min_val, int max_val, 
                    unordered_map<int, TreeNode*>& roots, int& count) {
        if (!node) return true;

        // BST Property Check
        if (node->val <= min_val || node->val >= max_val) return false;

        // If this is a leaf node and there exists a tree rooted at this value, merge it.
        if (!node->left && !node->right && roots.count(node->val) && roots[node->val] != node) {
            TreeNode* nextRoot = roots[node->val];
            node->left = nextRoot->left;
            node->right = nextRoot->right;
            // Erase to prevent cycle/re-visitation and track unique roots processed
            roots.erase(node->val); 
        }

        // Base case increment: we only count when we evaluate a node that was a root.
        // Initially, the globalRoot itself counts. Any merged root counts when traversed.
        if (node->left == nullptr && node->right == nullptr) {
            // Leaf node processed
        }

        // For tracking total components merged: we can increment count when we successfully 
        // visit/verify a distinct root component structure. Since we erased from 'roots', 
        // we can track how many parts of the puzzle are joined.
        
        // Let's refine component counting: count the structural root nodes processed.
        // Since we check the left and right subtrees recursively:
        bool left_valid = true;
        if (node->left) {
            if (roots.count(node->left->val)) {
                count++;
                TreeNode* childRoot = roots[node->left->val];
                node->left->left = childRoot->left;
                node->left->right = childRoot->right;
                roots.erase(node->left->val);
            }
            left_valid = isValidBST(node->left, min_val, node->val, roots, count);
        }

        bool right_valid = true;
        if (node->right) {
            if (roots.count(node->right->val)) {
                count++;
                TreeNode* childRoot = roots[node->right->val];
                node->right->left = childRoot->left;
                node->right->right = childRoot->right;
                roots.erase(node->right->val);
            }
            right_valid = isValidBST(node->right, node->val, max_val, roots, count);
        }

        return left_valid && right_valid;
    }
};