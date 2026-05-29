#include <numeric>

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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        // If the list is empty or has only one node, no adjacent pairs exist.
        if (!head || !head->next) {
            return head;
        }
        
        ListNode* curr = head;
        
        // Traverse the list until we reach the last node
        while (curr && curr->next) {
            // Calculate the GCD of the current node and the next node
            int gcd_val = std::gcd(curr->val, curr->next->val);
            
            // Create a new node with the GCD value, pointing to the next node
            ListNode* gcd_node = new ListNode(gcd_val, curr->next);
            
            // Link the current node to the newly created GCD node
            curr->next = gcd_node;
            
            // Move curr forward by two steps to point to the original next node
            curr = gcd_node->next;
        }
        
        return head;
    }
};