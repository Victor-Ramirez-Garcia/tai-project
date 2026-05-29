#include <numeric>

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
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        // If the list has 0 or 1 nodes, there are no adjacent pairs to process.
        if (!head || !head->next) {
            return head;
        }
        
        ListNode* curr = head;
        
        // Traverse the list until we reach the last node
        while (curr && curr->next) {
            // Calculate the greatest common divisor of the current and next node values
            int gcd_val = std::gcd(curr->val, curr->next->val);
            
            // Create a new node with the GCD value, pointing to the next node
            ListNode* gcd_node = new ListNode(gcd_val, curr->next);
            
            // Insert the new node after the current node
            curr->next = gcd_node;
            
            // Move current pointer past the inserted node to the original next node
            curr = gcd_node->next;
        }
        
        return head;
    }
};