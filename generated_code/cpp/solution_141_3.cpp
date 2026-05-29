#include <cstddef>

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
        
        // Edge case: empty list or single node with no cycle
        if (!head || !head->next) {
            return false;
        }
        
        ListNode *slow = head;
        ListNode *fast = head;
        
        // Move slow pointer by 1 step and fast pointer by 2 steps
        while (fast && fast->next) {
            slow = slow->next;
            fast = fast->next->next;
            
            // If there is a cycle, the fast pointer will eventually meet the slow pointer
            if (slow == fast) {
                return true;
            }
        }
        
        // If fast reaches the end, no cycle exists
        return false;
    }
};