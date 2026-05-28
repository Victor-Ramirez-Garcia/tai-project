#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Helper function to create a linked list from a vector
ListNode* createList(const std::vector<int>& nums) {
    if (nums.empty()) return nullptr;
    ListNode* head = new ListNode(nums[0]);
    ListNode* curr = head;
    for (size_t i = 1; i < nums.size(); ++i) {
        curr->next = new ListNode(nums[i]);
        curr = curr->next;
    }
    return head;
}

// Helper function to convert a linked list back to a vector for verification
std::vector<int> listToVector(ListNode* head) {
    std::vector<int> result;
    ListNode* curr = head;
    while (curr != nullptr) {
        result.push_back(curr->val);
        curr = curr->next;
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

class AddTwoNumbersTest : public ::testing::Test {
protected:
    Solution solution;
};

// Example 1: l1 = [2,4,3], l2 = [5,6,4] -> Output: [7,0,8]
TEST_F(AddTwoNumbersTest, TestExample1) {
    ListNode* l1 = createList({2, 4, 3});
    ListNode* l2 = createList({5, 6, 4});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {7, 0, 8};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

// Example 2: l1 = [0], l2 = [0] -> Output: [0]
TEST_F(AddTwoNumbersTest, TestExample2SingleZeros) {
    ListNode* l1 = createList({0});
    ListNode* l2 = createList({0});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {0};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

// Example 3: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9] -> Output: [8,9,9,9,0,0,0,1]
TEST_F(AddTwoNumbersTest, TestExample3VaryingLengthsWithCarries) {
    ListNode* l1 = createList({9, 9, 9, 9, 9, 9, 9});
    ListNode* l2 = createList({9, 9, 9, 9});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {8, 9, 9, 9, 0, 0, 0, 1};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

// Edge Case: One list is significantly longer than the other, ending with additional carry
TEST_F(AddTwoNumbersTest, TestOneListLongerWithFinalCarry) {
    ListNode* l1 = createList({1});
    ListNode* l2 = createList({9, 9, 9});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {0, 0, 0, 1};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

// Edge Case: Maximum constraint length simulation (100 nodes of 9s)
TEST_F(AddTwoNumbersTest, TestMaxConstraintLength) {
    std::vector<int> longNum(100, 9);
    ListNode* l1 = createList(longNum);
    ListNode* l2 = createList({1});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    
    std::vector<int> expected(100, 0);
    expected.push_back(1); // 1 followed by 100 zeros in reverse order
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

// Edge Case: Minimum constraint length (1 node each, no carry)
TEST_F(AddTwoNumbersTest, TestMinConstraintLengthNoCarry) {
    ListNode* l1 = createList({5});
    ListNode* l2 = createList({3});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {8};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}