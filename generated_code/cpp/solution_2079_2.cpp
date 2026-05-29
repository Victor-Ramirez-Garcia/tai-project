#include <vector>
#include <string>
#include <unordered_map>
#include <map>
#include <algorithm>

using namespace std;

// Trie node structure to represent the file system hierarchy
struct TrieNode {
    string name;
    // Use std::map to automatically keep children sorted by name.
    // This simplifies generating consistent serialized sub-tree strings.
    map<string, TrieNode*> children;
    bool del = false; // Flag to mark if this folder should be deleted

    TrieNode(string n = "") : name(n) {}
};

class Solution {
private:
    // Global frequency map for sub-tree serializations
    unordered_map<string, int> seen;

    // Helper to insert a path into the Trie
    void insert(TrieNode* root, const vector<string>& path) {
        TrieNode* curr = root;
        for (const string& s : path) {
            if (curr->children.find(s) == curr->children.end()) {
                curr->children[s] = new TrieNode(s);
            }
            curr = curr->children[s];
        }
    }

    // Step 1: Serialize the sub-tree structures and count frequencies.
    // An empty or leaf folder returns an empty string because it has no subfolders.
    string serialize(TrieNode* node) {
        if (node->children.empty()) return "";

        string sub_tree = "";
        for (auto& pair : node->children) {
            sub_tree += "(" + pair.first + serialize(pair.second) + ")";
        }

        // Only track frequencies of folders that actually contain subfolders
        seen[sub_tree]++;
        return sub_tree;
    }

    // Step 2: Mark duplicate sub-trees for deletion
    void mark_duplicates(TrieNode* node) {
        if (node->children.empty()) return;

        string sub_tree = "";
        for (auto& pair : node->children) {
            sub_tree += "(" + pair.first + serialize(pair.second) + ")";
        }

        // If this exact sub-tree structure has been seen more than once,
        // mark this node for deletion.
        if (seen[sub_tree] > 1) {
            node->del = true;
        }

        for (auto& pair : node->children) {
            mark_duplicates(pair.second);
        }
    }

    // Step 3: Walk the Trie to collect all paths that survived deletion
    void collect_paths(TrieNode* node, vector<string>& current_path, vector<vector<string>>& result) {
        if (node->del) return; // If marked for deletion, stop traversing this branch

        if (!current_path.empty()) {
            result.push_back(current_path);
        }

        for (auto& pair : node->children) {
            current_path.push_back(pair.first);
            collect_paths(pair.second, current_path, result);
            current_path.pop_back(); // Backtrack
        }
    }

    // Helper to free allocated memory
    void clear(TrieNode* node) {
        for (auto& pair : node->children) {
            clear(pair.second);
        }
        delete node;
    }

public:
    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        TrieNode* root = new TrieNode();
        seen.clear();

        // Build the Trie structure
        for (const auto& path : paths) {
            insert(root, path);
        }

        // Post-order serialization to populate the frequency map
        serialize(root);

        // Pre-order / structural traversal to mark duplicates
        mark_duplicates(root);

        // Collect all valid paths
        vector<vector<string>> result;
        vector<string> current_path;
        collect_paths(root, current_path, result);

        // Clean up memory
        clear(root);

        return result;
    }
};