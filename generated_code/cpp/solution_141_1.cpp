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
        // Floyd's Tortoise and Hare Algorithm (Two Pointers)
        // Time Complexity: O(N) where N is the number of nodes.
        // Space Complexity: O(1) auxiliary space.
        
        // Edge case: An empty list or a list with only one node cannot have a cycle.
        if (!head || !head->next) {
            return false;
        }
        
        ListNode *slow = head;
        ListNode *fast = head;
        
        // Move slow pointer by 1 step and fast pointer by 2 steps.
        // If there is a cycle, they will eventually meet.
        // If there is no cycle, fast pointer will hit the end of the list (NULL).
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            
            // Cycle detected
            if (slow == fast) {
                return true;
            }
        }
        
        // Fast reached the end, so no cycle exists.
        return false;
    }
};