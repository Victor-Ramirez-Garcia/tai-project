#include <gtest/gtest.h>
#include <vector>
#include <queue>
#include <sstream>
#include <string>
#include <memory>
#include "solution_proxy.h"

using namespace std;

// Helper function to build a tree from a serialized vector representation (Level Order)
// E.g., {3, 2, 5, 1, -1, 4} where -1 denotes null
TreeNode* buildTree(const vector<int>& nodes) {
    if (nodes.empty() || nodes[0] == -1) return nullptr;
    TreeNode* root = new TreeNode(nodes[0]);
    queue<TreeNode*> q;
    q.push(root);
    int i = 1;
    while (!q.empty() && i < nodes.size()) {
        TreeNode* curr = q.front();
        q.pop();
        
        if (i < nodes.size() && nodes[i] != -1) {
            curr->left = new TreeNode(nodes[i]);
            q.push(curr->left);
        }
        i++;
        
        if (i < nodes.size() && nodes[i] != -1) {
            curr->right = new TreeNode(nodes[i]);
            q.push(curr->right);
        }
        i++;
    }
    return root;
}

// Helper function to free the dynamically allocated tree memory
void freeTree(TreeNode* root) {
    if (!root) return;
    freeTree(root->left);
    freeTree(root->right);
    delete root;
}

// Helper function to check if two trees are structurally and values-wise identical
bool isSameTree(TreeNode* p, TreeNode* q) {
    if (!p && !q) return true;
    if (!p || !q) return false;
    return (p->val == q->val) && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
}

class CanMergeTreesTest : public ::testing::Test {
protected:
    Solution solution;
    vector<TreeNode*> treeList;

    void TearDown() override {
        for (auto* root : treeList) {
            freeTree(root);
        }
        treeList.clear();
    }
};

// Example 1: Valid merger of three trees forming a larger valid BST
TEST_F(CanMergeTreesTest, Example1ValidMerger) {
    // trees = [[2,1],[3,2,5],[5,4]]
    TreeNode* t1 = buildTree({2, 1});
    TreeNode* t2 = buildTree({3, 2, 5});
    TreeNode* t3 = buildTree({5, 4});
    treeList = {t1, t2, t3};

    TreeNode* expected = buildTree({3, 2, 5, 1, -1, 4});
    TreeNode* result = solution.canMerge(treeList);

    EXPECT_TRUE(isSameTree(result, expected));
    
    // Clear list from TearDown tracking if it was consumed/modified, 
    // but free expected since it's local
    freeTree(expected);
    freeTree(result);
    treeList.clear(); 
}

// Example 2: Merger results in an invalid BST violation (6 is placed under 3 via 5, but 6 > 5 is valid, wait: 6 is right of 3, but under 5? Let's check logic: 5's left is 3, 3's right is 6. 6 is in 5's left subtree, violating 6 < 5)
TEST_F(CanMergeTreesTest, Example2InvalidBSTResult) {
    // trees = [[5,3,8],[3,2,6]]
    TreeNode* t1 = buildTree({5, 3, 8});
    TreeNode* t2 = buildTree({3, 2, 6});
    treeList = {t1, t2};

    TreeNode* result = solution.canMerge(treeList);
    EXPECT_EQ(result, nullptr);
    
    freeTree(result);
}

// Example 3: No valid operations can be performed (disjoint roots/leaves)
TEST_F(CanMergeTreesTest, Example3NoOperationsPossible) {
    // trees = [[5,4],[3]]
    TreeNode* t1 = buildTree({5, 4});
    TreeNode* t2 = buildTree({3});
    treeList = {t1, t2};

    TreeNode* result = solution.canMerge(treeList);
    EXPECT_EQ(result, nullptr);
    
    freeTree(result);
}

// Edge Case: Minimum constraints (Single tree input)
TEST_F(CanMergeTreesTest, SingleTreeInput) {
    // A single tree is already a completed operation of n-1 = 0 steps.
    TreeNode* t1 = buildTree({10, 5, 15});
    treeList = {t1};

    TreeNode* expected = buildTree({10, 5, 15});
    TreeNode* result = solution.canMerge(treeList);

    EXPECT_TRUE(isSameTree(result, expected));

    freeTree(expected);
    freeTree(result);
    treeList.clear();
}

// Edge Case: Cyclic dependency among tree leaves and roots (cannot form a single root)
TEST_F(CanMergeTreesTest, CyclicDependency) {
    // t1 root=1, leaf=2; t2 root=2, leaf=1 -> forms a cycle, no clear single root.
    TreeNode* t1 = buildTree({1, -1, 2});
    TreeNode* t2 = buildTree({2, 1, -1});
    treeList = {t1, t2};

    TreeNode* result = solution.canMerge(treeList);
    EXPECT_EQ(result, nullptr);

    freeTree(result);
}

// Edge Case: Multiple separate components (disconnected sub-graphs)
TEST_F(CanMergeTreesTest, DisconnectedComponents) {
    // Two independent valid pairs that can't join into a single tree
    TreeNode* t1 = buildTree({2, 1});
    TreeNode* t2 = buildTree({1});
    TreeNode* t3 = buildTree({5, 4});
    TreeNode* t4 = buildTree({4});
    treeList = {t1, t2, t3, t4};

    TreeNode* result = solution.canMerge(treeList);
    EXPECT_EQ(result, nullptr);

    freeTree(result);
}

// Edge Case: Multiple leaves matching the same root value (invalid structure/ambiguity)
TEST_F(CanMergeTreesTest, DuplicateLeafValuesAcrossTrees) {
    // Two different trees have a leaf value of 2, aiming to merge with a single root 2
    TreeNode* t1 = buildTree({3, 2, -1});
    TreeNode* t2 = buildTree({4, 2, -1});
    TreeNode* t3 = buildTree({2});
    treeList = {t1, t2, t3};

    TreeNode* result = solution.canMerge(treeList);
    EXPECT_EQ(result, nullptr);

    freeTree(result);
}