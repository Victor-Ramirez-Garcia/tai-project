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

// Helper function to convert a linked list back to a vector
std::vector<int> listToVector(ListNode* head) {
    std::vector<int> result;
    ListNode* current = head;
    while (current != nullptr) {
        result.push_back(current->val);
        current = current->next;
    }
    return result;
}

// Helper function to safely delete a linked list to prevent memory leaks
void freeList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

class InsertGCDTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Example 1: Multiple elements with varying GCDs
TEST_F(InsertGCDTest, Example1_MultipleElements) {
    std::vector<int> inputValues = {18, 6, 10, 3};
    std::vector<int> expectedValues = {18, 6, 6, 2, 10, 1, 3};
    
    ListNode* head = createList(inputValues);
    ListNode* resultHead = solution.insertGreatestCommonDivisors(head);
    std::vector<int> resultValues = listToVector(resultHead);
    
    EXPECT_EQ(resultValues, expectedValues);
    freeList(resultHead);
}

// Test Example 2: Single element (Minimum node constraint)
TEST_F(InsertGCDTest, Example2_SingleElement) {
    std::vector<int> inputValues = {7};
    std::vector<int> expectedValues = {7};
    
    ListNode* head = createList(inputValues);
    ListNode* resultHead = solution.insertGreatestCommonDivisors(head);
    std::vector<int> resultValues = listToVector(resultHead);
    
    EXPECT_EQ(resultValues, expectedValues);
    freeList(resultHead);
}

// Test Edge Case: Two elements with a GCD of 1 (Coprime numbers)
TEST_F(InsertGCDTest, TwoElementsCoprime) {
    std::vector<int> inputValues = {13, 7};
    std::vector<int> expectedValues = {13, 1, 7};
    
    ListNode* head = createList(inputValues);
    ListNode* resultHead = solution.insertGreatestCommonDivisors(head);
    std::vector<int> resultValues = listToVector(resultHead);
    
    EXPECT_EQ(resultValues, expectedValues);
    freeList(resultHead);
}

// Test Edge Case: Two elements where one divides the other completely
TEST_F(InsertGCDTest, TwoElementsMultiples) {
    std::vector<int> inputValues = {5, 25};
    std::vector<int> expectedValues = {5, 5, 25};
    
    ListNode* head = createList(inputValues);
    ListNode* resultHead = solution.insertGreatestCommonDivisors(head);
    std::vector<int> resultValues = listToVector(resultHead);
    
    EXPECT_EQ(resultValues, expectedValues);
    freeList(resultHead);
}

// Test Edge Case: Identical elements (GCD is the number itself)
TEST_F(InsertGCDTest, IdenticalElements) {
    std::vector<int> inputValues = {12, 12, 12};
    std::vector<int> expectedValues = {12, 12, 12, 12, 12};
    
    ListNode* head = createList(inputValues);
    ListNode* resultHead = solution.insertGreatestCommonDivisors(head);
    std::vector<int> resultValues = listToVector(resultHead);
    
    EXPECT_EQ(resultValues, expectedValues);
    freeList(resultHead);
}

// Test Edge Case: Boundary node values (1 and 1000 based on constraints)
TEST_F(InsertGCDTest, BoundaryNodeValues) {
    std::vector<int> inputValues = {1, 1000};
    std::vector<int> expectedValues = {1, 1, 1000};
    
    ListNode* head = createList(inputValues);
    ListNode* resultHead = solution.insertGreatestCommonDivisors(head);
    std::vector<int> resultValues = listToVector(resultHead);
    
    EXPECT_EQ(resultValues, expectedValues);
    freeList(resultHead);
}

// Test Case: Maximum constraint value pair (1000 and 1000)
TEST_F(InsertGCDTest, MaxConstraintValues) {
    std::vector<int> inputValues = {1000, 1000};
    std::vector<int> expectedValues = {1000, 1000, 1000};
    
    ListNode* head = createList(inputValues);
    ListNode* resultHead = solution.insertGreatestCommonDivisors(head);
    std::vector<int> resultValues = listToVector(resultHead);
    
    EXPECT_EQ(resultValues, expectedValues);
    freeList(resultHead);
}