#include <vector>
#include <string>
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
    ListNode* middleNode(ListNode* head) {
        // We use Floyd's Tortoise and Hare algorithm (Two Pointers approach).
        // Time Complexity: O(N) where N is the number of nodes in the linked list.
        // Space Complexity: O(1) as we only use two pointers.
        ListNode* slow = head;
        ListNode* fast = head;
        
        // Advance 'fast' by two steps and 'slow' by one step.
        // When 'fast' reaches the end, 'slow' will be exactly at the middle node.
        // For an even number of nodes, this correctly stops at the second middle node.
        while (fast != nullptr && fast->next != nullptr) {
            slow = slow->next;
            fast = fast->next->next;
        }
        
        return slow;
    }
};