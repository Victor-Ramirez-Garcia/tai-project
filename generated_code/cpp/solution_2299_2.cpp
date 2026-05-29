#include <iostream>

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    /**
     * Algorithm: In-place Two-Pointer approach.
     * We use a 'writer' pointer to modify the existing nodes of the list to save space
     * and a 'reader' pointer to traverse and sum the values between zeros.
     * 
     * Time Complexity: O(n) - We traverse the list exactly once.
     * Space Complexity: O(1) - We modify the list in-place (excluding the return result).
     */
    ListNode* mergeNodes(ListNode* head) {
        // Start 'writer' at the first node that will hold a sum (head->next).
        // The original head is a 0, so we ignore it.
        ListNode* writer = head->next;
        ListNode* reader = head->next;
        
        while (reader != nullptr) {
            int currentSum = 0;
            
            // Traverse until we hit the next 0 node.
            // Since the problem guarantees no two consecutive zeros and ends with a 0,
            // we will always find a sequence of non-zero nodes.
            while (reader != nullptr && reader->val != 0) {
                currentSum += reader->val;
                reader = reader->next;
            }
            
            // Assign the sum to the writer node.
            writer->val = currentSum;
            
            // Move reader to the node immediately after the 0 we just encountered.
            reader = reader->next;
            
            // If reader is null, we reached the end of the original list.
            if (reader == nullptr) {
                writer->next = nullptr;
                break;
            }
            
            // Otherwise, link the current writer to the next available slot and move forward.
            writer->next = reader;
            writer = writer->next;
        }
        
        // Return head->next because the original head was a 0.
        return head->next;
    }
};