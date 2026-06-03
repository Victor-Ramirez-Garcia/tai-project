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

// Helper function to convert a linked list to a vector
std::vector<int> listToVector(ListNode* head) {
    std::vector<int> result;
    ListNode* current = head;
    while (current != nullptr) {
        result.push_back(current->val);
        current = current->next;
    }
    return result;
}

// Helper function to free the allocated linked list memory
void freeList(ListNode* head) {
    while (head != nullptr) {
        ListNode* temp = head;
        head = head->next;
        delete temp;
    }
}

class MergeNodesTest : public ::testing::Test {
protected:
    Solution solution;
};

// Test Case: Example 1 from problem description
TEST_F(MergeNodesTest, Example1) {
    std::vector<int> input = {0, 3, 1, 0, 4, 5, 2, 0};
    std::vector<int> expected = {4, 11};
    
    ListNode* head = createList(input);
    ListNode* resultHead = solution.mergeNodes(head);
    std::vector<int> result = listToVector(resultHead);
    
    EXPECT_EQ(result, expected);
    freeList(resultHead);
}

// Test Case: Example 2 from problem description
TEST_F(MergeNodesTest, Example2) {
    std::vector<int> input = {0, 1, 0, 3, 0, 2, 2, 0};
    std::vector<int> expected = {1, 3, 4};
    
    ListNode* head = createList(input);
    ListNode* resultHead = solution.mergeNodes(head);
    std::vector<int> result = listToVector(resultHead);
    
    EXPECT_EQ(result, expected);
    freeList(resultHead);
}

// Test Case: Minimum constraints (3 nodes: [0, X, 0])
TEST_F(MergeNodesTest, MinimumNodes) {
    std::vector<int> input = {0, 5, 0};
    std::vector<int> expected = {5};
    
    ListNode* head = createList(input);
    ListNode* resultHead = solution.mergeNodes(head);
    std::vector<int> result = listToVector(resultHead);
    
    EXPECT_EQ(result, expected);
    freeList(resultHead);
}

// Test Case: Node values are 0 (e.g., [0, 0, 0] is invalid per constraints, but nodes between 0s can be 0)
TEST_F(MergeNodesTest, ZeroValuesBetweenZeros) {
    std::vector<int> input = {0, 0, 0, 0}; // Wait, constraint says "no two consecutive nodes with Node.val == 0"
    // So valid input with 0 value between 0s must be separated like: [0, 0, 1, 0] -> invalid consecutive.
    // "0 <= Node.val <= 1000". If value is 0, it cannot be consecutive. Thus, {0, 0...} is invalid.
    // Correct interpretation of node values being 0 means an actual sequence like [0, 5, 0, 0] is invalid.
    // However, if Node.val is 0, it acts as a separator. The constraint says "no two consecutive nodes with Node.val == 0".
    // This implies all block separators are non-empty. So values between 0s are strictly > 0 due to the constraint.
    // Let's test a single element that reaches max constraint value.
    std::vector<int> inputMaxVal = {0, 1000, 1000, 0, 1000, 0};
    std::vector<int> expectedMaxVal = {2000, 1000};

    ListNode* head = createList(inputMaxVal);
    ListNode* resultHead = solution.mergeNodes(head);
    std::vector<int> result = listToVector(resultHead);
    
    EXPECT_EQ(result, expectedMaxVal);
    freeList(resultHead);
}

// Test Case: Large number of nodes to ensure no stack overflow or timeout (within limit)
TEST_F(MergeNodesTest, LargeList) {
    std::vector<int> input = {0};
    std::vector<int> expected;
    
    // Creating a chain of 10000 blocks of [1, 0] -> 20001 nodes total
    for (int i = 0; i < 10000; ++i) {
        input.push_back(1);
        input.push_back(0);
        expected.push_back(1);
    }
    
    ListNode* head = createList(input);
    ListNode* resultHead = solution.mergeNodes(head);
    std::vector<int> result = listToVector(resultHead);
    
    EXPECT_EQ(result, expected);
    freeList(resultHead);
}

// Test Case: Multiple nodes between zeros summing up to a large value
TEST_F(MergeNodesTest, ManyNodesInSingleBlock) {
    std::vector<int> input = {0};
    int expected_sum = 0;
    for (int i = 0; i < 1000; ++i) {
        input.push_back(5);
        expected_sum += 5;
    }
    input.push_back(0);
    std::vector<int> expected = {expected_sum};
    
    ListNode* head = createList(input);
    ListNode* resultHead = solution.mergeNodes(head);
    std::vector<int> result = listToVector(resultHead);
    
    EXPECT_EQ(result, expected);
    freeList(resultHead);
}