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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        // Use a dummy head to simplify building the result linked list.
        ListNode dummy(0);
        ListNode* tail = &dummy;
        int carry = 0;

        // Iterate while there are nodes remaining in either list or there is a carry.
        // Time Complexity: O(max(N, M)) where N and M are lengths of l1 and l2.
        // Space Complexity: O(1) auxiliary space (excluding the output list).
        while (l1 != nullptr || l2 != nullptr || carry > 0) {
            int sum = carry;

            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }

            carry = sum / 10;
            tail->next = new ListNode(sum % 10);
            tail = tail->next;
        }

        return dummy.next;
    }
};