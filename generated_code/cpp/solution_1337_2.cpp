#include <vector>
#include <cstdlib>
#include <ctime>

// Node definition for the Skiplist
struct Node {
    int val;
    // forward[i] stores the pointer to the next node at level i
    std::vector<Node*> forward;
    
    Node(int val, int level) : val(val), forward(level, nullptr) {}
};

class Skiplist {
private:
    static const int MAX_LEVEL = 16; // O(log N) for N up to ~65536, sufficient for LeetCode constraints
    const double P = 0.5;            // Probability factor for coin flipping
    Node* head;
    int level;                       // Current maximum level of the skiplist

    // Helper to generate a random level for a new node
    int randomLevel() {
        int lvl = 1;
        while ((rand() & 0xFFFF) < (P * 0xFFFF) && lvl < MAX_LEVEL) {
            lvl++;
        }
        return lvl;
    }

public:
    Skiplist() {
        // Seed the random number generator
        srand(time(nullptr));
        // Initialize head node with a sentinel value and maximum level
        head = new Node(-1, MAX_LEVEL);
        level = 1;
    }
    
    // Deconstructor to free allocated memory
    ~Skiplist() {
        Node* curr = head;
        while (curr) {
            Node* next = curr->forward[0];
            delete curr;
            curr = next;
        }
    }

    bool search(int target) {
        Node* curr = head;
        // Start from the highest level and move down
        for (int i = level - 1; i >= 0; i--) {
            while (curr->forward[i] && curr->forward[i]->val < target) {
                curr = curr->forward[i];
            }
        }
        // Move to the next node at level 0
        curr = curr->forward[0];
        return curr && curr->val == target;
    }
    
    void add(int num) {
        // update array stores the pointers to nodes where the forward references need updating
        std::vector<Node*> update(MAX_LEVEL, nullptr);
        Node* curr = head;
        
        for (int i = level - 1; i >= 0; i--) {
            while (curr->forward[i] && curr->forward[i]->val < num) {
                curr = curr->forward[i];
            }
            update[i] = curr;
        }
        
        int rlevel = randomLevel();
        // If the random level is greater than the current maximum level,
        // initialize the update pointers for the new levels to head
        if (rlevel > level) {
            for (int i = level; i < rlevel; i++) {
                update[i] = head;
            }
            level = rlevel;
        }
        
        // Create the new node and insert it into the levels
        Node* newNode = new Node(num, rlevel);
        for (int i = 0; i < rlevel; i++) {
            newNode->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = newNode;
        }
    }
    
    bool erase(int num) {
        std::vector<Node*> update(MAX_LEVEL, nullptr);
        Node* curr = head;
        
        for (int i = level - 1; i >= 0; i--) {
            while (curr->forward[i] && curr->forward[i]->val < num) {
                curr = curr->forward[i];
            }
            update[i] = curr;
        }
        
        // Move to the potential target node
        curr = curr->forward[0];
        
        // If the target node is found, remove it
        if (curr && curr->val == num) {
            for (int i = 0; i < level; i++) {
                // If at level i, the next node is not the target, stop updating
                if (update[i]->forward[i] != curr) {
                    break;
                }
                update[i]->forward[i] = curr->forward[i];
            }
            delete curr; // Free memory
            
            // Adjust the current maximum level if the top levels become empty
            while (level > 1 && head->forward[level - 1] == nullptr) {
                level--;
            }
            return true;
        }
        
        return false;
    }
};