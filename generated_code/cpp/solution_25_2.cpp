#include <vector>
#include <algorithm>

// Definition for singly-linked list.
// Included for compilability as mandated by the instructions.
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
        // Base case: if list is empty or k is 1, no structural change is needed.
        if (!head || k == 1) return head;

        // Use a dummy node to simplify handling the new head of the list.
        ListNode dummy(0);
        dummy.next = head;

        ListNode* groupPrev = &dummy;
        ListNode* curr = head;

        // Count total number of nodes to handle groups efficiently.
        int count = 0;
        while (curr) {
            count++;
            curr = curr->next;
        }

        // Loop runs for every complete group of size k.
        // Time Complexity: O(N) since each node is visited at most twice.
        // Space Complexity: O(1) auxiliary space as we reverse in-place.
        while (count >= k) {
            curr = groupPrev->next;
            ListNode* nextNode = curr->next;

            // Standard in-place reversal for k-1 links within the current group.
            for (int i = 1; i < k; ++i) {
                curr->next = nextNode->next;
                nextNode->next = groupPrev->next;
                groupPrev->next = nextNode;
                nextNode = curr->next;
            }

            // Move groupPrev to the end of the reversed group (which is 'curr').
            groupPrev = curr;
            count -= k;
        }

        return dummy.next;
    }
};