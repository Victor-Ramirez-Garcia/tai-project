#include <gtest/gtest.h>
#include <vector>
#include "program_2_1.cpp" // Assuming a generic ID placeholder like 2 for the Add Two Numbers problem

// Helper function to create a linked list from a vector
ListNode* createList(const std::vector<int>& nums) {
    if (nums.empty()) return nullptr;
    ListNode* head = new ListNode(nums[0]);
    ListNode* current = head;
    for (size_t i = 1; i < nums.size(); ++i) {
        current->next = new ListNode(nums[i]);
        current = current->next;
    }
    return head;
}

// Helper function to convert a linked list to a vector for easy comparison
std::vector<int> listToVector(ListNode* head) {
    std::vector<int> result;
    while (head != nullptr) {
        result.push_back(head->val);
        head = head->next;
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

// Test Case: Example 1 from problem description
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

// Test Case: Example 2 from problem description (Single zero elements)
TEST_F(AddTwoNumbersTest, TestExample2_Zeros) {
    ListNode* l1 = createList({0});
    ListNode* l2 = createList({0});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {0};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

// Test Case: Example 3 from problem description (Different lengths and multiple carries)
TEST_F(AddTwoNumbersTest, TestExample3_DifferentLengthsWithCarries) {
    ListNode* l1 = createList({9, 9, 9, 9, 9, 9, 9});
    ListNode* l2 = createList({9, 9, 9, 9});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {8, 9, 9, 9, 0, 0, 0, 1};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

// Test Case: One list is significantly shorter than the other without extra carry at the end
TEST_F(AddTwoNumbersTest, TestOneListShorterNoFinalCarry) {
    ListNode* l1 = createList({1});
    ListNode* l2 = createList({9, 8, 7});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {0, 9, 7};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

// Test Case: Single digit addition causing a carry
TEST_F(AddTwoNumbersTest, TestSingleDigitsWithCarry) {
    ListNode* l1 = createList({5});
    ListNode* l2 = createList({7});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {2, 1};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

// Test Case: Max constraint simulation logic check (Continuous carrying up to a new node)
TEST_F(AddTwoNumbersTest, TestContinuousCarriesCreatesNewNode) {
    ListNode* l1 = createList({9, 9, 9});
    ListNode* l2 = createList({1});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {0, 0, 0, 1};
    
    EXPECT_EQ(listToVector(result), expected);
    
    freeList(l1);
    freeList(l2);
    freeList(result);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}