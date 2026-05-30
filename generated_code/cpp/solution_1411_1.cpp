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
    int getDecimalValue(ListNode* head) {
        int result = 0;
        
        // Traverse the linked list from head to tail.
        // Since the most significant bit is at the head, for each new node,
        // we shift the current accumulated value to the left by 1 bit (multiply by 2)
        // and add the current node's value.
        // Time Complexity: O(N) where N is the number of nodes.
        // Space Complexity: O(1) auxiliary space.
        while (head != nullptr) {
            result = (result << 1) | head->val;
            head = head->next;
        }
        
        return result;
    }
};