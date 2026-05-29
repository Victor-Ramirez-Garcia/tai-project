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
     * Algorithm: Dummy Node (Sentinel) approach.
     * Time Complexity: O(N) where N is the number of nodes in the list.
     * Space Complexity: O(1) as we modify the list in-place.
     */
    ListNode* removeElements(ListNode* head, int val) {
        // Create a dummy node that points to the head.
        // This simplifies logic for removing the head node itself.
        ListNode dummy(0, head);
        ListNode* current = &dummy;

        while (current->next != nullptr) {
            if (current->next->val == val) {
                // Node needs to be removed.
                ListNode* temp = current->next;
                current->next = current->next->next;
                // In a competitive programming environment, we often omit 'delete' 
                // to save time, but it is best practice for memory management.
                delete temp; 
            } else {
                // Move to the next node only if we didn't perform a deletion.
                current = current->next;
            }
        }

        return dummy.next;
    }
};