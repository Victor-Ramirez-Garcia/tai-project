#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Helper function to create a linked list from a vector
ListNode* createLinkedList(const std::vector<int>& values) {
    if (values.empty()) return nullptr;
    ListNode* head = new ListNode(values[0]);
    ListNode* current = head;
    for (size_t i = 1; i < values.size(); ++i) {
        current->next = new ListNode(values[i]);
        current = current->next;
    }
    return head;
}

// Helper function to convert a linked list back to a vector
std::vector<int> linkedListToVector(ListNode* head) {
    std::vector<int> result;
    ListNode* current = head;
    while (current != nullptr) {
        result.push_back(current->val);
        current = current->next;
    }
    return result;
}

// Helper function to free the memory of a linked list
void freeLinkedList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

// Test Class Setup
class RemoveElementsTest : public ::testing::Test {
protected:
    Solution solution;
};

// Example 1: Standard case with some target elements in the middle and end
TEST_F(RemoveElementsTest, Example1_MixedElements) {
    ListNode* head = createLinkedList({1, 2, 6, 3, 4, 5, 6});
    int val = 6;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {1, 2, 3, 4, 5};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Example 2: Empty list input
TEST_F(RemoveElementsTest, Example2_EmptyList) {
    ListNode* head = createLinkedList({});
    int val = 1;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Example 3: All elements in the list match the target value
TEST_F(RemoveElementsTest, Example3_AllElementsMatch) {
    ListNode* head = createLinkedList({7, 7, 7, 7});
    int val = 7;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: Target value appears at the head of the list
TEST_F(RemoveElementsTest, TargetAtHeadOnly) {
    ListNode* head = createLinkedList({5, 1, 2, 3});
    int val = 5;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {1, 2, 3};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: Target value appears consecutively at the start
TEST_F(RemoveElementsTest, ConsecutiveTargetsAtHead) {
    ListNode* head = createLinkedList({5, 5, 5, 1, 2});
    int val = 5;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {1, 2};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: Target value appears consecutively in the middle
TEST_F(RemoveElementsTest, ConsecutiveTargetsInMiddle) {
    ListNode* head = createLinkedList({1, 5, 5, 5, 2});
    int val = 5;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {1, 2};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: Target value is not present in the list
TEST_F(RemoveElementsTest, TargetValueNotFound) {
    ListNode* head = createLinkedList({1, 2, 3, 4});
    int val = 9;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {1, 2, 3, 4};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: Single element list matching the target value
TEST_F(RemoveElementsTest, SingleElementMatches) {
    ListNode* head = createLinkedList({42});
    int val = 42;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Edge Case: Single element list not matching the target value
TEST_F(RemoveElementsTest, SingleElementDoesNotMatch) {
    ListNode* head = createLinkedList({42});
    int val = 24;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {42};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}

// Constraint Test: Node values and val parameter edge combinations (min/max boundaries)
TEST_F(RemoveElementsTest, BoundaryValueConstraints) {
    ListNode* head = createLinkedList({1, 50, 1, 50});
    int val = 50;
    
    ListNode* resultHead = solution.removeElements(head, val);
    std::vector<int> resultVec = linkedListToVector(resultHead);
    std::vector<int> expected = {1, 1};
    
    EXPECT_EQ(resultVec, expected);
    freeLinkedList(resultHead);
}