#include <iostream>

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
    ListNode* removeElements(ListNode* head, int val) {
        // Use a dummy node to seamlessly handle deletion of the head node.
        ListNode dummy(0, head);
        ListNode* prev = &dummy;
        ListNode* curr = head;
        
        // Traverse through the linked list.
        while (curr != nullptr) {
            if (curr->val == val) {
                // Bypass the current node.
                prev->next = curr->next;
                
                // In a production/strict memory environment, delete curr to prevent memory leaks:
                // ListNode* toDelete = curr;
                // curr = curr->next;
                // delete toDelete;
                
                curr = curr->next;
            } else {
                // Move the prev pointer forward only if we didn't delete a node.
                prev = curr;
                curr = curr->next;
            }
        }
        
        // Return the actual head of the modified list.
        return dummy.next;
    }
};