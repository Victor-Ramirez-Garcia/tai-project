#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Helper function to create a linked list from a vector
ListNode* createLinkedList(const std::vector<int>& values) {
    if (values.empty()) return nullptr;
    ListNode* head = new ListNode(values[0]);
    ListNode* curr = head;
    for (size_t i = 1; i < values.size(); ++i) {
        curr->next = new ListNode(values[i]);
        curr = curr->next;
    }
    return head;
}

// Helper function to convert a linked list to a vector
std::vector<int> linkedListToVector(ListNode* head) {
    std::vector<int> result;
    ListNode* curr = head;
    while (curr != nullptr) {
        result.push_back(curr->val);
        curr = curr->next;
    }
    return result;
}

// Helper function to free the allocated linked list memory
void freeLinkedList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

class ReverseKGroupTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Example 1: head = [1,2,3,4,5], k = 2 -> Output: [2,1,4,3,5]
TEST_F(ReverseKGroupTest, Example1) {
    ListNode* head = createLinkedList({1, 2, 3, 4, 5});
    int k = 2;
    ListNode* resultHead = solution.reverseKGroup(head, k);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {2, 1, 4, 3, 5};
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Test Example 2: head = [1,2,3,4,5], k = 3 -> Output: [3,2,1,4,5]
TEST_F(ReverseKGroupTest, Example2) {
    ListNode* head = createLinkedList({1, 2, 3, 4, 5});
    int k = 3;
    ListNode* resultHead = solution.reverseKGroup(head, k);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {3, 2, 1, 4, 5};
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: Single node list (n = 1, k = 1)
TEST_F(ReverseKGroupTest, SingleNodeList) {
    ListNode* head = createLinkedList({100});
    int k = 1;
    ListNode* resultHead = solution.reverseKGroup(head, k);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {100};
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: k equals the length of the list (n = 4, k = 4)
TEST_F(ReverseKGroupTest, KEqualsLengthOfList) {
    ListNode* head = createLinkedList({1, 2, 3, 4});
    int k = 4;
    ListNode* resultHead = solution.reverseKGroup(head, k);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {4, 3, 2, 1};
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: k = 1, list should remain unchanged
TEST_F(ReverseKGroupTest, KEqualsOne) {
    ListNode* head = createLinkedList({1, 2, 3, 4, 5, 6});
    int k = 1;
    ListNode* resultHead = solution.reverseKGroup(head, k);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {1, 2, 3, 4, 5, 6};
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: List size is a perfect multiple of k
TEST_F(ReverseKGroupTest, PerfectMultipleOfK) {
    ListNode* head = createLinkedList({1, 2, 3, 4, 5, 6});
    int k = 2;
    ListNode* resultHead = solution.reverseKGroup(head, k);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {2, 1, 4, 3, 6, 5};
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: List size is less than k (No changes expected)
TEST_F(ReverseKGroupTest, ListLengthLessThanK) {
    ListNode* head = createLinkedList({1, 2});
    int k = 3;
    ListNode* resultHead = solution.reverseKGroup(head, k);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {1, 2};
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}