#include <iostream>

/*
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
        // Fast and Slow Pointer Approach (Tortoise and Hare)
        // Time Complexity: O(N) where N is the number of nodes in the linked list.
        // Space Complexity: O(1) auxiliary space.

        ListNode* slow = head;
        ListNode* fast = head;
        
        // Move 'fast' by two steps and 'slow' by one step.
        // When 'fast' reaches the end, 'slow' will be at the middle.
        // For even-length lists, this naturally stops at the second middle node.
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }

};