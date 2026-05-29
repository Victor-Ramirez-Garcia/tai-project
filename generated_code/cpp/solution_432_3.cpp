#include <string>
#include <unordered_map>
#include <unordered_set>
#include <list>

using namespace std;

class AllOne {
private:
    // Bucket structure to group keys with the same frequency
    struct Bucket {
        int count;
        unordered_set<string> keys;
        Bucket(int c) : count(c) {}
    };

    // Doubly linked list to maintain buckets sorted by count
    list<Bucket> buckets;
    
    // Maps each key to its corresponding bucket iterator in the linked list
    unordered_map<string, list<Bucket>::iterator> keyToBucket;

public:
    AllOne() {
        // No initialization needed; list and map default construct to empty
    }
    
    // Time Complexity: O(1) average
    void inc(string key) {
        if (keyToBucket.find(key) == keyToBucket.end()) {
            // Key is new, it should go into a bucket with count 1
            if (buckets.empty() || buckets.front().count != 1) {
                buckets.push_front(Bucket(1));
            }
            buckets.front().keys.insert(key);
            keyToBucket[key] = buckets.begin();
        } else {
            // Key exists, move it to the bucket with count + 1
            auto curBucket = keyToBucket[key];
            auto nextBucket = next(curBucket);
            
            if (nextBucket == buckets.end() || nextBucket->count != curBucket->count + 1) {
                nextBucket = buckets.insert(nextBucket, Bucket(curBucket->count + 1));
            }
            
            nextBucket->keys.insert(key);
            keyToBucket[key] = nextBucket;
            
            // Clean up current bucket
            curBucket->keys.erase(key);
            if (curBucket->keys.empty()) {
                buckets.erase(curBucket);
            }
        }
    }
    
    // Time Complexity: O(1) average
    void dec(string key) {
        // Guaranteed that key exists according to constraints
        auto curBucket = keyToBucket[key];
        
        if (curBucket->count == 1) {
            // If current count is 1, decrementing means removing it completely
            keyToBucket.erase(key);
        } else {
            // Move it to the bucket with count - 1
            auto prevBucket = prev(curBucket);
            
            if (curBucket == buckets.begin() || prevBucket->count != curBucket->count - 1) {
                prevBucket = buckets.insert(curBucket, Bucket(curBucket->count - 1));
            }
            
            prevBucket->keys.insert(key);
            keyToBucket[key] = prevBucket;
        }
        
        // Clean up current bucket
        curBucket->keys.erase(key);
        if (curBucket->keys.empty()) {
            buckets.erase(curBucket);
        }
    }
    
    // Time Complexity: O(1)
    string getMaxKey() {
        if (buckets.empty()) {
            return "";
        }
        return *(buckets.back().keys.begin());
    }
    
    // Time Complexity: O(1)
    string getMinKey() {
        if (buckets.empty()) {
            return "";
        }
        return *(buckets.front().keys.begin());
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