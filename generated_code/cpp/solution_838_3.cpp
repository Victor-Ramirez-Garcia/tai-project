#include <iostream>

// Definition for doubly-linked list node.
struct Node {
    int val;
    Node* prev;
    Node* next;
    Node(int v) : val(v), prev(nullptr), next(nullptr) {}
};

class MyLinkedList {
private:
    int size;
    Node* head;
    Node* tail;

public:
    // Initializes the MyLinkedList object with dummy head and tail nodes to simplify insertions/deletions.
    MyLinkedList() {
        size = 0;
        head = new Node(0);
        tail = new Node(0);
        head->next = tail;
        tail->prev = head;
    }
    
    // Destructor to clean up memory and prevent leaks.
    ~MyLinkedList() {
        Node* curr = head;
        while (curr != nullptr) {
            Node* nextNode = curr->next;
            delete curr;
            curr = nextNode;
        }
    }
    
    // Time Complexity: O(min(index, size - index))
    int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        
        Node* curr;
        // Optimize search direction based on proximity to head or tail
        if (index < size / 2) {
            curr = head->next;
            for (int i = 0; i < index; ++i) {
                curr = curr->next;
            }
        } else {
            curr = tail->prev;
            for (int i = 0; i < size - 1 - index; ++i) {
                curr = curr->prev;
            }
        }
        return curr->val;
    }
    
    // Time Complexity: O(1)
    void addAtHead(int val) {
        Node* newNode = new Node(val);
        Node* succ = head->next;
        
        newNode->prev = head;
        newNode->next = succ;
        head->next = newNode;
        succ->prev = newNode;
        
        size++;
    }
    
    // Time Complexity: O(1)
    void addAtTail(int val) {
        Node* newNode = new Node(val);
        Node* pred = tail->prev;
        
        newNode->prev = pred;
        newNode->next = tail;
        pred->next = newNode;
        tail->prev = newNode;
        
        size++;
    }
    
    // Time Complexity: O(min(index, size - index))
    void addAtIndex(int index, int val) {
        if (index < 0 || index > size) {
            return;
        }
        
        Node* pred;
        Node* succ;
        
        // Find predecessor and successor for insertion point
        if (index < size / 2) {
            pred = head;
            for (int i = 0; i < index; ++i) {
                pred = pred->next;
            }
            succ = pred->next;
        } else {
            succ = tail;
            for (int i = 0; i < size - index; ++i) {
                succ = succ->prev;
            }
            pred = succ->prev;
        }
        
        Node* newNode = new Node(val);
        newNode->prev = pred;
        newNode->next = succ;
        pred->next = newNode;
        succ->prev = newNode;
        
        size++;
    }
    
    // Time Complexity: O(min(index, size - index))
    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        
        Node* pred;
        Node* succ;
        
        // Find predecessor and successor of the node to be deleted
        if (index < size / 2) {
            pred = head;
            for (int i = 0; i < index; ++i) {
                pred = pred->next;
            }
            succ = pred->next->next;
        } else {
            succ = tail;
            for (int i = 0; i < size - 1 - index; ++i) {
                succ = succ->prev;
            }
            pred = succ->prev->prev;
        }
        
        Node* toDelete = pred->next;
        pred->next = succ;
        succ->prev = pred;
        
        delete toDelete;
        size--;
    }
};