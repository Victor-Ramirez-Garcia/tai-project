#include <vector>
#include <cstdlib>
#include <ctime>

// Node definition for the Skiplist
struct Node {
    int val;
    // forward[i] stores the pointer to the next node at level i
    std::vector<Node*> forward;
    
    Node(int v, int level) : val(v), forward(level, nullptr) {}
};

class Skiplist {
private:
    static const int MAX_LEVEL = 16; // Maximum level for the skiplist
    const double P = 0.5;            // Probability factor for coin flips
    Node* head;                      // Dummy head node
    int level;                       // Current maximum level of the skiplist

    // Helper function to generate a random level for a new node
    int randomLevel() {
        int lvl = 1;
        while ((rand() & 0xFFFF) < (P * 0xFFFF) && lvl < MAX_LEVEL) {
            lvl++;
        }
        return lvl;
    }

public:
    Skiplist() {
        // Initialize random seed and dummy head node
        srand(time(nullptr));
        head = new Node(-1, MAX_LEVEL);
        level = 1;
    }
    
    ~Skiplist() {
        // Clean up memory
        Node* curr = head;
        while (curr) {
            Node* next = curr->forward[0];
            delete curr;
            curr = next;
        }
    }
    
    // Time Complexity: O(log N) average, O(N) worst case
    // Space Complexity: O(1)
    bool search(int target) {
        Node* curr = head;
        // Traverse from the top level down to level 0
        for (int i = level - 1; i >= 0; i--) {
            while (curr->forward[i] && curr->forward[i]->val < target) {
                curr = curr->forward[i];
            }
        }
        // Move to the next node at level 0
        curr = curr->forward[0];
        return curr && curr->val == target;
    }
    
    // Time Complexity: O(log N) average, O(N) worst case
    // Space Complexity: O(MAX_LEVEL) to store the update vector
    void add(int num) {
        // update array keeps track of the nodes where the search path drops down
        std::vector<Node*> update(MAX_LEVEL, nullptr);
        Node* curr = head;
        
        for (int i = level - 1; i >= 0; i--) {
            while (curr->forward[i] && curr->forward[i]->val < num) {
                curr = curr->forward[i];
            }
            update[i] = curr;
        }
        
        int rLevel = randomLevel();
        // If the random level exceeds the current max level, initialize update pointers
        if (rLevel > level) {
            for (int i = level; i < rLevel; i++) {
                update[i] = head;
            }
            level = rLevel;
        }
        
        // Insert the new node into the levels
        Node* newNode = new Node(num, rLevel);
        for (int i = 0; i < rLevel; i++) {
            newNode->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = newNode;
        }
    }
    
    // Time Complexity: O(log N) average, O(N) worst case
    // Space Complexity: O(MAX_LEVEL) to store the update vector
    bool erase(int num) {
        std::vector<Node*> update(MAX_LEVEL, nullptr);
        Node* curr = head;
        
        for (int i = level - 1; i >= 0; i--) {
            while (curr->forward[i] && curr->forward[i]->val < num) {
                curr = curr->forward[i];
            }
            update[i] = curr;
        }
        
        curr = curr->forward[0];
        // If the target element is found, proceed to remove it
        if (curr && curr->val == num) {
            for (int i = 0; i < level; i++) {
                if (update[i]->forward[i] != curr) {
                    break;
                }
                update[i]->forward[i] = curr->forward[i];
            }
            delete curr; // Free memory of the erased node
            
            // Recalculate the active levels in the skiplist
            while (level > 1 && head->forward[level - 1] == nullptr) {
                level--;
            }
            return true;
        }
        return false;
    }
};