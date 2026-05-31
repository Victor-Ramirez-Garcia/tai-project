#include <iostream>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 * int val;
 * ListNode *next;
 * ListNode() : val(0), next(nullptr) {}
 * ListNode(int x) : val(x), next(nullptr) {}
 * ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        // We use the Tortoise and Hare (Two Pointers) algorithm.
        // 'slow' moves 1 step at a time, while 'fast' moves 2 steps at a time.
        ListNode* slow = head;
        ListNode* fast = head;
        
        // When 'fast' reaches the end (or past the end), 'slow' will be at the middle.
        // For even-length lists, this naturally stops at the second middle node.
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Time Complexity: O(N) where N is the number of nodes in the linked list.
        // Space Complexity: O(1) auxiliary space.
        return slow;
    }
};