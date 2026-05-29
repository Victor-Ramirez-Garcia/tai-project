#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <climits>

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
    TreeNode* canMerge(vector<TreeNode*>& trees) {
        // Map to quickly find the root node of a tree by its root value.
        unordered_map<int, TreeNode*> valueToRoot;
        // Set to collect all unique leaf values across all initial trees.
        unordered_set<int> leaves;

        for (TreeNode* tree : trees) {
            valueToRoot[tree->val] = tree;
            if (tree->left) leaves.insert(tree->left->val);
            if (tree->right) leaves.insert(tree->right->val);
        }

        // The root of the final merged tree must be a root that is NOT a leaf in any other tree.
        TreeNode* globalRoot = nullptr;
        for (TreeNode* tree : trees) {
            if (leaves.find(tree->val) == leaves.end()) {
                if (globalRoot != nullptr) {
                    // More than one potential global root means the trees cannot be fully connected into one.
                    return nullptr;
                }
                globalRoot = tree;
            }
        }

        // If no candidate for a global root is found, a valid single merged tree is impossible.
        if (!globalRoot) return nullptr;

        // Track how many unique roots we successfully traverse/merge.
        int visitedRootsCount = 0;

        // Validate the merged structure using an in-order traversal style (min/max constraints)
        // while dynamically stitching the trees together.
        if (!isValidBSTAndMerge(globalRoot, INT_MIN, INT_MAX, valueToRoot, visitedRootsCount)) {
            return nullptr;
        }

        // Ensure that all trees given in the input have been successfully merged into the single component.
        return (visitedRootsCount == trees.size()) ? globalRoot : nullptr;
    }

private:
    bool isValidBSTAndMerge(TreeNode* node, int minVal, int maxVal, 
                            unordered_map<int, TreeNode*>& valueToRoot, int& visitedRootsCount) {
        if (!node) return true;

        // Current node's value must strictly satisfy the BST range properties.
        if (node->val <= minVal || node->val >= maxVal) return false;

        // If this is a leaf node, check if there's another tree's root that can be grafted here.
        if (!node->left && !node->right) {
            auto it = valueToRoot.find(node->val);
            if (it != valueToRoot.end() && it->second != node) {
                TreeNode* nextTree = it->second;
                // Stitch the next tree's children onto this leaf placeholder.
                node->left = nextTree->left;
                node->right = nextTree->right;
                // Remove from the map to prevent infinite cycles/re-visitations.
                valueToRoot.erase(it);
                visitedRootsCount++;
            }
        } else {
            // Count the root of the individual small tree components when we first visit their structures.
            // If it's the global root, or if it was stitched previously, it represents an individual component.
            // We can alternatively increment when we enter a known initial root.
            // To simplify, we count the root if it matches the current node when we process its children.
            auto it = valueToRoot.find(node->val);
            if (it != valueToRoot.end() && it->second == node) {
                valueToRoot.erase(it);
                visitedRootsCount++;
            }
        }

        // Recursively validate left and right subtrees with narrowed BST bounds.
        return isValidBSTAndMerge(node->left, minVal, node->val, valueToRoot, visitedRootsCount) &&
               isValidBSTAndMerge(node->right, node->val, maxVal, valueToRoot, visitedRootsCount);
    }
};