#include <string>
#include <unordered_map>
#include <unordered_set>
#include <list>

using namespace std;

class AllOne {
private:
    // Node structure for the doubly linked list.
    // Each node represents a specific frequency (count) and stores all keys with that frequency.
    struct Node {
        int count;
        unordered_set<string> keys;
        Node(int c) : count(c) {}
    };

    // Doubly linked list to maintain sorted order of frequencies.
    list<Node> bucketList;
    
    // Maps each key to its corresponding iterator in the bucketList.
    unordered_map<string, list<Node>::iterator> keyToBucket;

public:
    AllOne() {
        // Initialize the object. The bucketList is initially empty.
    }
    
    void inc(string key) {
        if (keyToBucket.find(key) == keyToBucket.end()) {
            // Case 1: Key does not exist. It needs to be inserted with count 1.
            if (bucketList.empty() || bucketList.front().count != 1) {
                bucketList.push_front(Node(1));
            }
            bucketList.front().keys.insert(key);
            keyToBucket[key] = bucketList.begin();
        } else {
            // Case 2: Key exists. Move it to the bucket with count + 1.
            auto curBucket = keyToBucket[key];
            auto nextBucket = next(curBucket);
            int nextCount = curBucket->count + 1;
            
            // Create a new bucket if the bucket with nextCount doesn't exist.
            if (nextBucket == bucketList.end() || nextBucket->count != nextCount) {
                nextBucket = bucketList.insert(nextBucket, Node(nextCount));
            }
            
            nextBucket->keys.insert(key);
            keyToBucket[key] = nextBucket;
            
            // Remove the key from the old bucket.
            curBucket->keys.erase(key);
            if (curBucket->keys.empty()) {
                bucketList.erase(curBucket);
            }
        }
    }
    
    void dec(string key) {
        // It is guaranteed that key exists in the data structure before decrement.
        auto curBucket = keyToBucket[key];
        int nextCount = curBucket->count - 1;
        
        if (nextCount == 0) {
            // If count becomes 0, completely remove the key.
            keyToBucket.erase(key);
        } else {
            // Move the key to the bucket with count - 1.
            auto prevBucket = curBucket;
            if (prevBucket == bucketList.begin()) {
                bucketList.push_front(Node(nextCount));
                prevBucket = bucketList.begin();
            } else {
                prevBucket = prev(curBucket);
                if (prevBucket->count != nextCount) {
                    prevBucket = bucketList.insert(curBucket, Node(nextCount));
                }
            }
            
            prevBucket->keys.insert(key);
            keyToBucket[key] = prevBucket;
        }
        
        // Remove the key from the old bucket.
        curBucket->keys.erase(key);
        if (curBucket->keys.empty()) {
            bucketList.erase(curBucket);
        }
    }
    
    string getMaxKey() {
        // The last node in bucketList contains keys with the maximum frequency.
        if (bucketList.empty()) {
            return "";
        }
        return *(bucketList.back().keys.begin());
    }
    
    string getMinKey() {
        // The first node in bucketList contains keys with the minimum frequency.
        if (bucketList.empty()) {
            return "";
        }
        return *(bucketList.front().keys.begin());
    }
};

/**
 * Your AllOne object will be instantiated and called as such:
 * AllOne* obj = new AllOne();
 * obj->inc(key);
 * obj->dec(key);
 * string param_3 = obj->getMaxKey();
 * string param_4 = obj->getMinKey();
 */