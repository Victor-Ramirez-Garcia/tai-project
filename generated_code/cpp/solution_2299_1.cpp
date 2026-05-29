#include <iostream>

// Definition for singly-linked list, included as mandated for self-contained compilation.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeNodes(ListNode* head) {
        // Two-pointer approach: modify the list in-place to achieve O(1) extra space.
        // 'modify' tracks where the merged sum node will be placed.
        // 'curr' scans through the nodes to calculate the block sums.
        ListNode* modify = head->next;
        ListNode* curr = modify;
        
        while (curr != nullptr) {
            int current_sum = 0;
            // Accumulate the sum of all nodes until the next 0 node is reached.
            while (curr->val != 0) {
                current_sum += curr->val;
                curr = curr->next;
            }
            
            // Assign the accumulated sum to the modify node.
            modify->val = current_sum;
            // Move curr past the 0 node to the start of the next block.
            curr = curr->next;
            // Link the current merged node to the next segment's modified node.
            modify->next = curr;
            // Advance the modify pointer to prepare for the next sum block.
            modify = modify->next;
        }
        
        // The first block started at head->next, which is the new head of the processed list.
        return head->next;
    }
};