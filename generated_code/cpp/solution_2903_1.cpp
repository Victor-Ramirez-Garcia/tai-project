#include <numeric> // For std::gcd

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
     * Algorithm: Linear Traversal with In-place Insertion
     * 
     * We traverse the linked list using a pointer 'curr'. For each node, 
     * if a 'next' node exists, we calculate the GCD of the current and 
     * next node values. We then create a new node with this GCD and 
     * insert it between them.
     * 
     * Time Complexity: O(N * log(min(V))), where N is the number of nodes 
     * and V is the maximum value in a node (log factor due to GCD calculation).
     * Space Complexity: O(1) auxiliary space (ignoring the space for new nodes).
     */
    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        // If the list is empty or has only one node, no pairs exist to insert GCDs.
        if (!head || !head->next) {
            return head;
        }

        ListNode* curr = head;

        // Traverse until the second to last node
        while (curr != nullptr && curr->next != nullptr) {
            // Calculate GCD of the two adjacent nodes using C++17 std::gcd
            int commonDivisor = std::gcd(curr->val, curr->next->val);

            // Create the new node and link it: curr -> newNode -> nextNode
            ListNode* newNode = new ListNode(commonDivisor, curr->next);
            curr->next = newNode;

            // Move curr forward by two steps: Skip the newly inserted node 
            // to reach the original "next" node for the next iteration.
            curr = newNode->next;
        }

        return head;
    }
};