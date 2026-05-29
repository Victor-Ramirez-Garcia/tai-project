#include <gtest/gtest.h>
#include <vector>
#include "solution_proxy.h"

// Helper function to create a linked list with an optional cycle
ListNode* createLinkedList(const std::vector<int>& values, int pos) {
    if (values.empty()) {
        return nullptr;
    }

    ListNode* head = new ListNode(values[0]);
    ListNode* current = head;
    ListNode* cycleNode = (pos == 0) ? head : nullptr;

    for (size_t i = 1; i < values.size(); ++i) {
        current->next = new ListNode(values[i]);
        current = current->next;
        if (static_cast<int>(i) == pos) {
            cycleNode = current;
        }
    }

    if (pos != -1 && cycleNode != nullptr) {
        current->next = cycleNode;
    }

    return head;
}

// Helper function to safely free memory for non-cyclic lists
void freeLinkedList(ListNode* head) {
    ListNode* current = head;
    while (current != nullptr) {
        ListNode* nextNode = current->next;
        delete current;
        current = nextNode;
    }
}

// Helper function to free memory for cyclic lists
void freeCyclicLinkedList(ListNode* head, int size) {
    ListNode* current = head;
    for (int i = 0; i < size; ++i) {
        if (!current) break;
        ListNode* nextNode = current->next;
        delete current;
        current = nextNode;
    }
}

TEST(LinkedListCycleTest, Example1_HasCycleInMiddle) {
    std::vector<int> values = {3, 2, 0, -4};
    int pos = 1;
    ListNode* head = createLinkedList(values, pos);

    Solution solution;
    EXPECT_TRUE(solution.hasCycle(head));

    freeCyclicLinkedList(head, values.size());
}

TEST(LinkedListCycleTest, Example2_HasCycleToHead) {
    std::vector<int> values = {1, 2};
    int pos = 0;
    ListNode* head = createLinkedList(values, pos);

    Solution solution;
    EXPECT_TRUE(solution.hasCycle(head));

    freeCyclicLinkedList(head, values.size());
}

TEST(LinkedListCycleTest, Example3_SingleNodeNoCycle) {
    std::vector<int> values = {1};
    int pos = -1;
    ListNode* head = createLinkedList(values, pos);

    Solution solution;
    EXPECT_FALSE(solution.hasCycle(head));

    freeLinkedList(head);
}

TEST(LinkedListCycleTest, EdgeCase_EmptyList) {
    ListNode* head = nullptr;

    Solution solution;
    EXPECT_FALSE(solution.hasCycle(head));
}

TEST(LinkedListCycleTest, EdgeCase_SingleNodeWithSelfCycle) {
    std::vector<int> values = {42};
    int pos = 0;
    ListNode* head = createLinkedList(values, pos);

    Solution solution;
    EXPECT_TRUE(solution.hasCycle(head));

    freeCyclicLinkedList(head, values.size());
}

TEST(LinkedListCycleTest, Constraint_LargeListNoCycle) {
    std::vector<int> values(1000, 5);
    int pos = -1;
    ListNode* head = createLinkedList(values, pos);

    Solution solution;
    EXPECT_FALSE(solution.hasCycle(head));

    freeLinkedList(head);
}

TEST(LinkedListCycleTest, Constraint_LargeListWithCycle) {
    std::vector<int> values(1000, 7);
    int pos = 500;
    ListNode* head = createLinkedList(values, pos);

    Solution solution;
    EXPECT_TRUE(solution.hasCycle(head));

    freeCyclicLinkedList(head, values.size());
}