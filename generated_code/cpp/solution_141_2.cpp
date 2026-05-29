#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        // Using Floyd's Tortoise and Hare algorithm (Two Pointers)
        // Time Complexity: O(N) where N is the number of nodes in the linked list
        // Space Complexity: O(1) auxiliary space
        
        if (!head || !head->next) {
            return false;
        }
        
        ListNode *slow = head;
        ListNode *fast = head;
        
        while (fast && fast->next) {
            slow = slow->next;          // Move slow pointer by 1 step
            fast = fast->next->next;    // Move fast pointer by 2 steps
            
            // If there is a cycle, the fast pointer will eventually catch up to the slow pointer
            if (slow == fast) {
                return true;
            }
        }
        
        // If fast reaches the end, there is no cycle
        return false;
    }
};