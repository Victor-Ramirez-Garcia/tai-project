#include <gtest/gtest.h>
#include <vector>

// Definition for singly-linked list provided by the problem
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

// Solution class to be tested
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode dummy(0);
        ListNode* tail = &dummy;
        int carry = 0;

        while (l1 != nullptr || l2 != nullptr || carry != 0) {
            int digit1 = (l1 != nullptr) ? l1->val : 0;
            int digit2 = (l2 != nullptr) ? l2->val : 0;

            int sum = digit1 + digit2 + carry;
            carry = sum / 10;
            tail->next = new ListNode(sum % 10);
            tail = tail->next;

            if (l1 != nullptr) l1 = l1->next;
            if (l2 != nullptr) l2 = l2->next;
        }

        return dummy.next;
    }
};

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

// Helper function to convert a linked list back to a vector for verification
std::vector<int> linkedListToVector(ListNode* head) {
    std::vector<int> result;
    while (head != nullptr) {
        result.push_back(head->val);
        head = head->next;
    }
    return result;
}

// Helper function to free allocated linked list memory
void freeLinkedList(ListNode* head) {
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

// Test Case 1: Example 1 from problem description
TEST_F(AddTwoNumbersTest, TestExample1) {
    ListNode* l1 = createLinkedList({2, 4, 3});
    ListNode* l2 = createLinkedList({5, 6, 4});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {7, 0, 8};
    
    EXPECT_EQ(linkedListToVector(result), expected);
    
    freeLinkedList(l1);
    freeLinkedList(l2);
    freeLinkedList(result);
}

// Test Case 2: Example 2 from problem description (Single elements, zeros)
TEST_F(AddTwoNumbersTest, TestExample2) {
    ListNode* l1 = createLinkedList({0});
    ListNode* l2 = createLinkedList({0});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {0};
    
    EXPECT_EQ(linkedListToVector(result), expected);
    
    freeLinkedList(l1);
    freeLinkedList(l2);
    freeLinkedList(result);
}

// Test Case 3: Example 3 from problem description (Different lengths, multiple carries)
TEST_F(AddTwoNumbersTest, TestExample3) {
    ListNode* l1 = createLinkedList({9, 9, 9, 9, 9, 9, 9});
    ListNode* l2 = createLinkedList({9, 9, 9, 9});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {8, 9, 9, 9, 0, 0, 0, 1};
    
    EXPECT_EQ(linkedListToVector(result), expected);
    
    freeLinkedList(l1);
    freeLinkedList(l2);
    freeLinkedList(result);
}

// Test Case 4: Edge Case - One list is shorter than the other (L1 < L2)
TEST_F(AddTwoNumbersTest, TestShorterFirstList) {
    ListNode* l1 = createLinkedList({1, 2});
    ListNode* l2 = createLinkedList({9, 7, 9});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {0, 0, 0, 1}; // 21 + 979 = 1000 -> [0, 0, 0, 1]
    
    EXPECT_EQ(linkedListToVector(result), expected);
    
    freeLinkedList(l1);
    freeLinkedList(l2);
    freeLinkedList(result);
}

// Test Case 5: Edge Case - Minimum node constraints (1 node each, non-zero values)
TEST_F(AddTwoNumbersTest, TestMinimumNodeConstraint) {
    ListNode* l1 = createLinkedList({5});
    ListNode* l2 = createLinkedList({5});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {0, 1};
    
    EXPECT_EQ(linkedListToVector(result), expected);
    
    freeLinkedList(l1);
    freeLinkedList(l2);
    freeLinkedList(result);
}

// Test Case 6: Edge Case - Final addition creates an extra carry node
TEST_F(AddTwoNumbersTest, TestFinalCarryCreation) {
    ListNode* l1 = createLinkedList({1});
    ListNode* l2 = createLinkedList({9, 9});
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    std::vector<int> expected = {0, 0, 1}; // 1 + 99 = 100 -> [0, 0, 1]
    
    EXPECT_EQ(linkedListToVector(result), expected);
    
    freeLinkedList(l1);
    freeLinkedList(l2);
    freeLinkedList(result);
}

// Test Case 7: Edge Case - High capacity input representation (Maximum constraints up to 100 nodes simulated)
TEST_F(AddTwoNumbersTest, TestLargeValueConstraint) {
    std::vector<int> largeNum1(100, 9); // 100 nodes of 9s
    std::vector<int> largeNum2(100, 9); // 100 nodes of 9s
    
    ListNode* l1 = createLinkedList(largeNum1);
    ListNode* l2 = createLinkedList(largeNum2);
    
    ListNode* result = solution.addTwoNumbers(l1, l2);
    
    // 99...99 + 99...99 results in 8 followed by ninety-nine 9s followed by 1
    std::vector<int> expected(101, 9);
    expected[0] = 8;
    expected[100] = 1;
    
    EXPECT_EQ(linkedListToVector(result), expected);
    
    freeLinkedList(l1);
    freeLinkedList(l2);
    freeLinkedList(result);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}