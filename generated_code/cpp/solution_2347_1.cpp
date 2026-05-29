#include <algorithm>

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
private:
    int matching_nodes_count = 0;

    // Helper function that performs a post-order traversal.
    // It returns a pair: {sum_of_subtree_values, count_of_subtree_nodes}.
    std::pair<int, int> calculateSubtreeDetails(TreeNode* node) {
        if (!node) {
            return {0, 0};
        }

        // Post-order traversal: compute values for left and right subtrees first.
        auto [left_sum, left_count] = calculateSubtreeDetails(node->left);
        auto [right_sum, right_count] = calculateSubtreeDetails(node->right);

        // Aggregate current node's subtree sum and node count.
        int total_sum = left_sum + right_sum + node->val;
        int total_count = left_count + right_count + 1;

        // Integer division implicitly rounds down to the nearest integer for non-negative numbers.
        if (total_sum / total_count == node->val) {
            matching_nodes_count++;
        }

        return {total_sum, total_count};
    }

public:
    // Time Complexity: O(N) where N is the number of nodes in the binary tree. We visit each node exactly once.
    // Space Complexity: O(H) where H is the height of the tree, due to the implicit call stack during recursion.
    int averageOfSubtree(TreeNode* root) {
        matching_nodes_count = 0;
        calculateSubtreeDetails(root);
        return matching_nodes_count;
    }
};