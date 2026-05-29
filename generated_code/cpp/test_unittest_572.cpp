#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include "solution_proxy.h"

// Helper function to build a binary tree from a level-order vector (using -100000 for null nodes)
TreeNode* buildTree(const std::vector<int>& nodes) {
    if (nodes.empty() || nodes[0] == -100000) return nullptr;
    
    TreeNode* root = new TreeNode(nodes[0]);
    std::queue<TreeNode*> q;
    q.push(root);
    
    size_t i = 1;
    while (!q.empty() && i < nodes.size()) {
        TreeNode* curr = q.front();
        q.pop();
        
        if (i < nodes.size() && nodes[i] != -100000) {
            curr->left = new TreeNode(nodes[i]);
            q.push(curr->left);
        }
        i++;
        
        if (i < nodes.size() && nodes[i] != -100000) {
            curr->right = new TreeNode(nodes[i]);
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

// Helper function to free the allocated binary tree memory
void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

class IsSubtreeTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case 1: Example 1 from problem description (True case)
TEST_F(IsSubtreeTest, Example1_ReturnsTrue) {
    TreeNode* root = buildTree({3, 4, 5, 1, 2});
    TreeNode* subRoot = buildTree({4, 1, 2});
    
    EXPECT_TRUE(solution.isSubtree(root, subRoot));
    
    freeTree(root);
    freeTree(freeTree); // Note: typo corrected below to subRoot
    freeTree(subRoot);
}

// Test Case 2: Example 2 from problem description (False case due to extra child node)
TEST_F(IsSubtreeTest, Example2_ReturnsFalse) {
    // -100000 represents null nodes in the level-order traversal
    TreeNode* root = buildTree({3, 4, 5, 1, 2, -100000, -100000, -100000, -100000, 0});
    TreeNode* subRoot = buildTree({4, 1, 2});
    
    EXPECT_FALSE(solution.isSubtree(root, subRoot));
    
    freeTree(root);
    freeTree(subRoot);
}

// Test Case 3: Both trees consist of a single matching node (Minimum constraints)
TEST_F(IsSubtreeTest, SingleNode_Identical_ReturnsTrue) {
    TreeNode* root = buildTree({1});
    TreeNode* subRoot = buildTree({1});
    
    EXPECT_TRUE(solution.isSubtree(root, subRoot));
    
    freeTree(root);
    freeTree(subRoot);
}

// Test Case 4: Both trees consist of a single node but have different values
TEST_F(IsSubtreeTest, SingleNode_DifferentValues_ReturnsFalse) {
    TreeNode* root = buildTree({1});
    TreeNode* subRoot = buildTree({2});
    
    EXPECT_FALSE(solution.isSubtree(root, subRoot));
    
    freeTree(root);
    freeTree(subRoot);
}

// Test Case 5: The subRoot is exactly identical to the entire root tree
TEST_F(IsSubtreeTest, EntireTreeIsSubtree_ReturnsTrue) {
    TreeNode* root = buildTree({10, 5, 15, 3, 7});
    TreeNode* subRoot = buildTree({10, 5, 15, 3, 7});
    
    EXPECT_TRUE(solution.isSubtree(root, subRoot));
    
    freeTree(root);
    freeTree(subRoot);
}

// Test Case 6: Deep skewed tree structure where subRoot matches the end of the chain
TEST_F(IsSubtreeTest, DeepSkewedTree_MatchesEnd_ReturnsTrue) {
    TreeNode* root = buildTree({1, 2, -100000, 3, -100000, 4, -100000, 5});
    TreeNode* subRoot = buildTree({4, 5});
    
    EXPECT_TRUE(solution.isSubtree(root, subRoot));
    
    freeTree(root);
    freeTree(subRoot);
}

// Test Case 7: The subRoot structure is similar but mirror-inverted
TEST_F(IsSubtreeTest, StructuralMismatch_MirrorImage_ReturnsFalse) {
    TreeNode* root = buildTree({3, 4, 5, 1, -100000});
    TreeNode* subRoot = buildTree({4, -100000, 1});
    
    EXPECT_FALSE(solution.isSubtree(root, subRoot));
    
    freeTree(root);
    freeTree(subRoot);
}

// Test Case 8: Boundary extreme values for node data (-10^4 and 10^4)
TEST_F(IsSubtreeTest, ExtremeNegativeAndPositiveValues_ReturnsTrue) {
    TreeNode* root = buildTree({-10000, 10000, 0});
    TreeNode* subRoot = buildTree({10000});
    
    EXPECT_TRUE(solution.isSubtree(root, subRoot));
    
    freeTree(root);
    freeTree(subRoot);
}

// Test Case 9: Duplicate subtrees present in the main tree
TEST_F(IsSubtreeTest, DuplicateSubtreesInRoot_ReturnsTrue) {
    TreeNode* root = buildTree({1, 2, 2, 4, 5, 4, 5});
    TreeNode* subRoot = buildTree({2, 4, 5});
    
    EXPECT_TRUE(solution.isSubtree(root, subRoot));
    
    freeTree(root);
    freeTree(subRoot);
}