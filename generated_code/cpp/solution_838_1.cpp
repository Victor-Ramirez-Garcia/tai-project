#include <iostream>

// Definition for the linked list node.
struct Node {
    int val;
    Node* prev;
    Node* next;
    Node(int v) : val(v), prev(nullptr), next(nullptr) {}
};

/**
 * Doubly Linked List Implementation with Dummy Head and Tail.
 * This approach prevents edge cases related to updating head/tail pointers,
 * making insertion and deletion operations O(1) once the node position is reached.
 * Time Complexity:
 * - get, addAtIndex, deleteAtIndex: O(N) in the worst case (where N is the list size).
 * - addAtHead, addAtTail: O(1) since we maintain direct links via dummy nodes.
 * Space Complexity: O(N) to store the elements.
 */
class MyLinkedList {
private:
    Node* head;
    Node* tail;
    int size;

public:
    // Initializes the MyLinkedList object with dummy head and tail nodes.
    MyLinkedList() {
        head = new Node(-1);
        tail = new Node(-1);
        head->next = tail;
        tail->prev = head;
        size = 0;
    }
    
    // Destructor to prevent memory leaks by freeing allocated nodes.
    ~MyLinkedList() {
        Node* curr = head;
        while (curr != nullptr) {
            Node* nextNode = curr->next;
            delete curr;
            curr = nextNode;
        }
    }
    
    // Get the value of the index-th node. Returns -1 if the index is invalid.
    int get(int index) {
        if (index < 0 || index >= size) {
            return -1;
        }
        
        Node* curr;
        // Optimize search direction based on whether index is closer to head or tail
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
    
    // Add a node of value val before the first element of the linked list.
    void addAtHead(int val) {
        Node* newNode = new Node(val);
        Node* nextNode = head->next;
        
        newNode->next = nextNode;
        newNode->prev = head;
        head->next = newNode;
        nextNode->prev = newNode;
        
        size++;
    }
    
    // Append a node of value val as the last element of the linked list.
    void addAtTail(int val) {
        Node* newNode = new Node(val);
        Node* prevNode = tail->prev;
        
        newNode->next = tail;
        newNode->prev = prevNode;
        prevNode->next = newNode;
        tail->prev = newNode;
        
        size++;
    }
    
    // Add a node of value val before the index-th node. 
    // If index equals size, append to the end. If index > size, do nothing.
    void addAtIndex(int index, int val) {
        if (index < 0 || index > size) {
            return;
        }
        
        if (index == size) {
            addAtTail(val);
            return;
        }
        if (index == 0) {
            addAtHead(val);
            return;
        }
        
        Node* curr;
        // Search from head or tail to find the node currently at 'index'
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
        
        // Insert newNode before curr
        Node* newNode = new Node(val);
        Node* prevNode = curr->prev;
        
        newNode->next = curr;
        newNode->prev = prevNode;
        prevNode->next = newNode;
        curr->prev = newNode;
        
        size++;
    }
    
    // Delete the index-th node in the linked list, if the index is valid.
    void deleteAtIndex(int index) {
        if (index < 0 || index >= size) {
            return;
        }
        
        Node* curr;
        // Search from head or tail to find the node to delete
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
        
        // Unlink the node and free memory
        Node* prevNode = curr->prev;
        Node* nextNode = curr->next;
        
        prevNode->next = nextNode;
        nextNode->prev = prevNode;
        
        delete curr;
        size--;
    }
};