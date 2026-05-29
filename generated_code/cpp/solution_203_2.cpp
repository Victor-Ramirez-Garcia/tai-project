#include <iostream>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    /**
     * Algorithm: Dummy Head Pointer
     * Time Complexity: O(N) where N is the number of nodes in the list.
     * Space Complexity: O(1) as we modify the list in-place without extra storage.
     * 
     * Using a dummy head simplifies edge cases where the head itself needs to be removed.
     */
    ListNode* removeElements(ListNode* head, int val) {
        // Create a dummy node that points to the head of the list.
        // This handles cases where the original head contains 'val'.
        ListNode dummy(0, head);
        ListNode* curr = &dummy;

        while (curr->next != nullptr) {
            if (curr->next->val == val) {
                // Node needs to be removed.
                ListNode* temp = curr->next;
                curr->next = curr->next->next;
                // In a competitive programming context, we assume memory is managed 
                // by the environment or ignored, but in production C++, we delete it.
                delete temp; 
            } else {
                // Node is valid, move the pointer forward.
                curr = curr->next;
            }
        }

        return dummy.next;
    }
};