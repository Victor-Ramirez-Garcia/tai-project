#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Helper function to create a linked list from a vector
ListNode* createList(const std::vector<int>& values) {
    if (values.empty()) return nullptr;
    ListNode* head = new ListNode(values[0]);
    ListNode* current = head;
    for (size_t i = 1; i < values.size(); ++i) {
        current->next = new ListNode(values[i]);
        current = current->next;
    }
    return head;
}

// Helper function to free the allocated memory of a linked list
void freeList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

// Test case for Example 1: Odd number of nodes
TEST(MiddleNodeTest, Example1_OddNumberOfNodes) {
    Solution solution;
    ListNode* head = createList({1, 2, 3, 4, 5});
    
    ListNode* result = solution.middleNode(head);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 3);
    
    freeList(head);
}

// Test case for Example 2: Even number of nodes (should return second middle)
TEST(MiddleNodeTest, Example2_EvenNumberOfNodes) {
    Solution solution;
    ListNode* head = createList({1, 2, 3, 4, 5, 6});
    
    ListNode* result = solution.middleNode(head);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 4);
    
    freeList(head);
}

// Edge case: Minimum number of nodes (exactly 1 node)
TEST(MiddleNodeTest, EdgeCase_SingleNodeList) {
    Solution solution;
    ListNode* head = createList({1});
    
    ListNode* result = solution.middleNode(head);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 1);
    EXPECT_EQ(result->next, nullptr);
    
    freeList(head);
}

// Edge case: Smallest even list (exactly 2 nodes)
TEST(MiddleNodeTest, EdgeCase_TwoNodesList) {
    Solution solution;
    ListNode* head = createList({1, 2});
    
    ListNode* result = solution.middleNode(head);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 2);
    EXPECT_EQ(result->next, nullptr);
    
    freeList(head);
}

// Edge case: Maximum scale constraint check (100 nodes, odd-like boundary evaluation via 99 nodes)
TEST(MiddleNodeTest, ConstraintBoundary_99Nodes) {
    Solution solution;
    std::vector<int> values;
    for (int i = 1; i <= 99; ++i) {
        values.push_back(i);
    }
    ListNode* head = createList(values);
    
    ListNode* result = solution.middleNode(head);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 50); // Middle of 99 is the 50th node (1-indexed)
    
    freeList(head);
}

// Edge case: Maximum allowed nodes according to constraints (100 nodes)
TEST(MiddleNodeTest, ConstraintBoundary_100Nodes) {
    Solution solution;
    std::vector<int> values;
    for (int i = 1; i <= 100; ++i) {
        values.push_back(i);
    }
    ListNode* head = createList(values);
    
    ListNode* result = solution.middleNode(head);
    
    ASSERT_NE(result, nullptr);
    EXPECT_EQ(result->val, 51); // Second middle of 100 is the 51st node (1-indexed)
    
    freeList(head);
}