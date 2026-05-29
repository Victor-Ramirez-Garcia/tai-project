#include <vector>
#include <cstdlib>
#include <ctime>

// Node definition for the Skiplist
struct SkiplistNode {
    int val;
    // Array of pointers to the next nodes at different levels
    std::vector<SkiplistNode*> next;
    
    SkiplistNode(int value, int level) : val(value), next(level, nullptr) {}
};

class Skiplist {
private:
    SkiplistNode* head;
    int maxLevel;
    float p;

    // Helper function to generate a random level for a new node
    int randomLevel() {
        int level = 1;
        while ((float)rand() / RAND_MAX < p && level < maxLevel) {
            level++;
        }
        return level;
    }

public:
    Skiplist() {
        // Standard max level chosen for the constraints (up to ~50,000 operations)
        maxLevel = 16;
        p = 0.5;
        // Head node acts as a sentinel with a minimum possible value
        head = new SkiplistNode(-1, maxLevel);
        srand(time(nullptr));
    }
    
    // Search for a target in O(log N) average time
    bool search(int target) {
        SkiplistNode* curr = head;
        // Traverse from the top level down to level 0
        for (int i = maxLevel - 1; i >= 0; --i) {
            while (curr->next[i] && curr->next[i]->val < target) {
                curr = curr->next[i];
            }
        }
        // Move to the next node at level 0
        curr = curr->next[0];
        return curr && curr->val == target;
    }
    
    // Insert a value into the Skiplist in O(log N) average time
    void add(int num) {
        // Track the nodes where we drop down a level
        std::vector<SkiplistNode*> update(maxLevel, nullptr);
        SkiplistNode* curr = head;
        
        for (int i = maxLevel - 1; i >= 0; --i) {
            while (curr->next[i] && curr->next[i]->val < num) {
                curr = curr->next[i];
            }
            update[i] = curr;
        }
        
        int lvl = randomLevel();
        SkiplistNode* newNode = new SkiplistNode(num, lvl);
        
        // Insert the new node into the linked lists up to 'lvl'
        for (int i = 0; i < lvl; ++i) {
            newNode->next[i] = update[i]->next[i];
            update[i]->next[i] = newNode;
        }
    }
    
    // Erase a single instance of a value in O(log N) average time
    bool erase(int num) {
        std::vector<SkiplistNode*> update(maxLevel, nullptr);
        SkiplistNode* curr = head;
        
        for (int i = maxLevel - 1; i >= 0; --i) {
            while (curr->next[i] && curr->next[i]->val < num) {
                curr = curr->next[i];
            }
            update[i] = curr;
        }
        
        // Check if the target node exists at level 0
        curr = curr->next[0];
        if (!curr || curr->val != num) {
            return false;
        }
        
        // Disconnect the target node from all levels it belongs to
        for (int i = 0; i < maxLevel; ++i) {
            if (update[i]->next[i] != curr) {
                break;
            }
            update[i]->next[i] = curr->next[i];
        }
        
        delete curr;
        return true;
    }
    
    ~Skiplist() {
        SkiplistNode* curr = head;
        while (curr) {
            SkiplistNode* nextNode = curr->next[0];
            delete curr;
            curr = nextNode;
        }
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */