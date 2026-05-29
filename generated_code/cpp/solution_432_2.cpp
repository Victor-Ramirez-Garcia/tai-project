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
        // No explicit initialization needed as standard containers handle themselves.
    }
    
    // Increments the count of the string key by 1.
    void inc(string key) {
        if (keyToBucket.find(key) == keyToBucket.end()) {
            // Key does not exist, insert it with count 1.
            if (bucketList.empty() || bucketList.front().count != 1) {
                bucketList.push_front(Node(1));
            }
            bucketList.front().keys.insert(key);
            keyToBucket[key] = bucketList.begin();
        } else {
            // Key already exists, move it to the node with count + 1.
            auto curBucket = keyToBucket[key];
            auto nextBucket = next(curBucket);
            int nextCount = curBucket->count + 1;
            
            if (nextBucket == bucketList.end() || nextBucket->count != nextCount) {
                nextBucket = bucketList.insert(nextBucket, Node(nextCount));
            }
            
            nextBucket->keys.insert(key);
            keyToBucket[key] = nextBucket;
            
            // Clean up the original bucket.
            curBucket->keys.erase(key);
            if (curBucket->keys.empty()) {
                bucketList.erase(curBucket);
            }
        }
    }
    
    // Decrements the count of the string key by 1.
    void dec(string key) {
        // It is guaranteed that key exists in the data structure before the decrement.
        auto curBucket = keyToBucket[key];
        int prevCount = curBucket->count - 1;
        
        if (prevCount == 0) {
            // Remove the key from the data structure completely.
            keyToBucket.erase(key);
        } else {
            // Move the key to the node with count - 1.
            auto prevBucket = prev(curBucket);
            if (curBucket == bucketList.begin() || prevBucket->count != prevCount) {
                prevBucket = bucketList.insert(curBucket, Node(prevCount));
            }
            
            prevBucket->keys.insert(key);
            keyToBucket[key] = prevBucket;
        }
        
        // Clean up the original bucket.
        curBucket->keys.erase(key);
        if (curBucket->keys.empty()) {
            bucketList.erase(curBucket);
        }
    }
    
    // Returns one of the keys with the maximal count. O(1) time complexity.
    string getMaxKey() {
        if (bucketList.empty()) {
            return "";
        }
        return *(bucketList.back().keys.begin());
    }
    
    // Returns one of the keys with the minimum count. O(1) time complexity.
    string getMinKey() {
        if (bucketList.empty()) {
            return "";
        }
        return *(bucketList.front().keys.begin());
    }
};