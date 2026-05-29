#include <vector>
#include <algorithm>

// Definition for singly-linked list.
// Included for compilability as mandated by guidelines.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* reverseKGroup(ListNode* head, int k) {
        if (!head || k == 1) return head;
        
        // Dummy node to simplify handling the new head of the list
        ListNode dummy(0);
        dummy.next = head;
        
        ListNode* prevGroupTail = &dummy;
        ListNode* curr = head;
        
        while (curr) {
            // Check if there are at least k nodes left to reverse
            ListNode* groupTail = prevGroupTail;
            for (int i = 0; i < k; ++i) {
                groupTail = groupTail->next;
                if (!groupTail) {
                    // Less than k nodes left, keep them as is and finish
                    return dummy.next;
                }
            }
            
            // Track the next group's head before we disconnect/reverse
            ListNode* nextGroupHead = groupTail->next;
            
            // Reverse the current group of k nodes
            ListNode* prev = nextGroupHead; // Connect the tail of reversed group to nextGroupHead
            ListNode* groupHead = curr;
            while (curr != nextGroupHead) {
                ListNode* nextNode = curr->next;
                curr->next = prev;
                prev = curr;
                curr = nextNode;
            }
            
            // Connect the previous group's tail to the new head of this reversed group
            prevGroupTail->next = prev;
            
            // The original head of this group is now the tail of this reversed group
            prevGroupTail = groupHead;
        }
        
        return dummy.next;
    }
};