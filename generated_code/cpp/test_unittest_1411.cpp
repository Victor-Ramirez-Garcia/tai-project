#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Helper function to create a linked list from a vector of integers
ListNode* createLinkedList(const std::vector<int>& values) {
    if (values.empty()) return nullptr;
    ListNode* head = new ListNode(values[0]);
    ListNode* current = head;
    for (size_size i = 1; i < values.size(); ++i) {
        current->next = new ListNode(values[i]);
        current = current->next;
    }
    return head;
}

// Helper function to free the allocated memory for the linked list
void freeLinkedList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

class GetDecimalValueTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case 1: Standard Example 1 from problem description [1, 0, 1] -> 5
TEST_F(GetDecimalValueTest, Example1_StandardBinaryNumber) {
    ListNode* head = createLinkedList({1, 0, 1});
    EXPECT_EQ(solution.getDecimalValue(head), 5);
    freeLinkedList(head);
}

// Test Case 2: Standard Example 2 from problem description [0] -> 0
TEST_F(GetDecimalValueTest, Example2_SingleZeroNode) {
    ListNode* head = createLinkedList({0});
    EXPECT_EQ(solution.getDecimalValue(head), 0);
    freeLinkedList(head);
}

// Test Case 3: Edge Case - Single node with value 1 (Minimum length boundary)
TEST_F(GetDecimalValueTest, EdgeCase_SingleOneNode) {
    ListNode* head = createLinkedList({1});
    EXPECT_EQ(solution.getDecimalValue(head), 1);
    freeLinkedList(head);
}

// Test Case 4: Edge Case - Maximum length boundary (30 nodes, all 1s)
TEST_F(GetDecimalValueTest, EdgeCase_MaxNodesAllOnes) {
    std::vector<int> values(30, 1);
    ListNode* head = createLinkedList(values);
    // 30 bits of 1s equals (2^30) - 1 = 1073741823
    EXPECT_EQ(solution.getDecimalValue(head), 1073741823);
    freeLinkedList(head);
}

// Test Case 5: Edge Case - Maximum length boundary (30 nodes, trailing 1)
TEST_F(GetDecimalValueTest, EdgeCase_MaxNodesLeadingZeros) {
    std::vector<int> values(29, 0);
    values.push_back(1); // 29 zeros followed by a one
    ListNode* head = createLinkedList(values);
    EXPECT_EQ(solution.getDecimalValue(head), 1);
    freeLinkedList(head);
}

// Test Case 6: Regular Case - Large binary sequence mixed bits
TEST_F(GetDecimalValueTest, RegularCase_MixedBits) {
    ListNode* head = createLinkedList({1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1});
    // (11110110101101) in base 2 = 15789 in base 10
    EXPECT_EQ(solution.getDecimalValue(head), 15789);
    freeLinkedList(head);
}