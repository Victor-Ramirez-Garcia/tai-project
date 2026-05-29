#include <iostream>

/**
 * Doubly Linked List Node Structure.
 * Doubly linked list allows for O(1) tail additions if we keep a tail pointer,
 * and generally more flexible deletions, though singly is sufficient here.
 * We'll use a Doubly Linked List with sentinel (dummy) nodes for head and tail
 * to simplify edge case logic (empty list, insertion at boundaries).
 */
struct Node {
    int val;
    Node* prev;
    Node* next;
    Node(int v) : val(v), prev(nullptr), next(nullptr) {}
};

class MyLinkedList {
private:
    int size;
    Node* head; // Dummy head
    Node* tail; // Dummy tail

public:
    /** Initialize your data structure here. */
    MyLinkedList() {
        size = 0;
        head = new Node(0);
        tail = new Node(0);
        head->next = tail;
        tail->prev = head;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if (index < 0 || index >= size) return -1;
        
        Node* curr = head;
        // Optimization: if index is in the second half, search from tail.
        if (index + 1 < size - index) {
            for (int i = 0; i <= index; ++i) curr = curr->next;
        } else {
            curr = tail;
            for (int i = 0; i < size - index; ++i) curr = curr->prev;
        }
        return curr->val;
    }
    
    /** Add a node of value val before the first element of the linked list. */
    void addAtHead(int val) {
        addAtIndex(0, val);
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        addAtIndex(size, val);
    }
    
    /** Add a node of value val before the index-th node. 
        If index equals to the length of linked list, the node will be appended to the end.
        If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        if (index > size) return;
        if (index < 0) index = 0;
        
        Node *pred, *succ;
        // Find predecessor and successor of the new node
        if (index < size - index) {
            pred = head;
            for (int i = 0; i < index; ++i) pred = pred->next;
            succ = pred->next;
        } else {
            succ = tail;
            for (int i = 0; i < size - index; ++i) succ = succ->prev;
            pred = succ->prev;
        }
        
        size++;
        Node* toAdd = new Node(val);
        toAdd->prev = pred;
        toAdd->next = succ;
        pred->next = toAdd;
        succ->prev = toAdd;
    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) return;
        
        Node *pred, *succ;
        // Find predecessor and successor of the node to be deleted
        if (index < size - index) {
            pred = head;
            for (int i = 0; i < index; ++i) pred = pred->next;
            succ = pred->next->next;
        } else {
            succ = tail;
            for (int i = 0; i < size - index - 1; ++i) succ = succ->prev;
            pred = succ->prev->prev;
        }
        
        size--;
        Node* toDelete = pred->next;
        pred->next = succ;
        succ->prev = pred;
        delete toDelete;
    }
    
    /** Destructor to clean up memory. */
    ~MyLinkedList() {
        Node* curr = head;
        while (curr) {
            Node* next = curr->next;
            delete curr;
            curr = next;
        }
    }
};