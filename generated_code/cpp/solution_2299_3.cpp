#include <vector>
#include <algorithm>
#include <iostream>

// Definition for singly-linked list.
// Provided in problem statement; explicitly defined here to ensure self-contained, compilable code.
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
        // Algorithm: Two Pointers / In-place Modification
        // Time Complexity: O(N) where N is the number of nodes. We traverse the list exactly once.
        // Space Complexity: O(1) auxiliary space as we modify the existing list in-place.
        
        ListNode* modify = head; // Pointer to overwrite values and rebuild the sequence
        ListNode* curr = head->next; // Pointer to traverse the original linked list
        
        int current_sum = 0;
        
        while (curr != nullptr) {
            if (curr->val == 0) {
                // We reached a 0 separator. Update the value of the modify node,
                // and advance the modify pointer to its next available position.
                modify->val = current_sum;
                
                // If this 0 is the absolute end of the list, we decouple the remaining nodes.
                if (curr->next == nullptr) {
                    modify->next = nullptr;
                } else {
                    modify = modify->next;
                }
                
                // Reset sum for the next segment
                current_sum = 0;
            } else {
                // Accumulate the segment sum
                current_sum += curr->val;
            }
            curr = curr->next;
        }
        
        return head;
    }
};