#include <vector>
#include <algorithm>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        // If k is 1, no reversing is needed.
        if (!head || k == 1) return head;

        // Count total nodes to determine how many groups can be reversed.
        int count = 0;
        ListNode* curr = head;
        while (curr) {
            count++;
            curr = curr->next;
        }

        // Dummy node to simplify head manipulation.
        ListNode* dummy = new ListNode(0);
        dummy->next = head;

        // Pointers to manage the reversal of groups.
        ListNode* prevGroupTail = dummy;
        curr = head;

        // Loop for each full group of size k.
        for (int i = 0; i < count / k; ++i) {
            ListNode* groupHead = curr;
            ListNode* prev = nullptr;
            ListNode* nextNode = nullptr;

            // Standard iterative linked list reversal for k nodes.
            for (int j = 0; j < k; ++j) {
                nextNode = curr->next;
                curr->next = prev;
                prev = curr;
                curr = nextNode;
            }

            // Connect the previous group's tail to the new head of this reversed group.
            prevGroupTail->next = prev;
            // The original group head becomes the tail of the reversed group.
            groupHead->next = curr;
            // Update prevGroupTail for the next iteration.
            prevGroupTail = groupHead;
        }

        ListNode* newHead = dummy->next;
        delete dummy; // Free the allocated dummy node.
        return newHead;
    }
};