#include

// Definition for singly-linked list if not already defined externally.
// Included here to ensure the code is self-contained and compilable.
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    int getDecimalValue(ListNode* head) {
        // Time Complexity: O(N) where N is the number of nodes in the linked list.
        // Space Complexity: O(1) as we only use a single integer to accumulate the result.
        int result = 0;

        // Traverse the linked list from head to tail.
        // Since the head represents the most significant bit, each step shifts 
        // the current accumulated value to the left by 1 (equivalent to multiplying by 2)
        // and adds the current node's value using a bitwise OR operation.
        while (head != nullptr) {
            result = (result << 1) | head->val;
            head = head->next;
        }
        
        return result;
    }
};