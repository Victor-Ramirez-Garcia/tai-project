#include <vector>
#include <string>
#include <unordered_map>
#include <map>
#include <algorithm>

using namespace std;

// Trie Node definition representing a folder in the file system
struct TrieNode {
    string name;
    // Use std::map to automatically keep children sorted by name.
    // This simplifies generating a unique, consistent sub-tree representation.
    map<string, TrieNode*> children;
    bool deleted = false;

    TrieNode(string n = "") : name(n) {}
};

class Solution {
private:
    TrieNode* root;
    // Map to keep track of the frequency of each sub-tree structure serialization
    unordered_map<string, int> serialization_counts;

    // Helper to insert a path into the Trie
    void insert(const vector<string>& path) {
        TrieNode* curr = root;
        for (const string& folder : path) {
            if (curr->children.find(folder) == curr->children.end()) {
                curr->children[folder] = new TrieNode(folder);
            }
            curr = curr->children[folder];
        }
    }

    // Step 1: Post-order traversal to serialize each sub-tree structure
    string serialize(TrieNode* node) {
        if (node->children.empty()) {
            return "";
        }

        string sub_tree_repr = "";
        for (auto& pair : node->children) {
            sub_tree_repr += "(" + pair.first + serialize(pair.second) + ")";
        }

        // Increment the count of this specific sub-tree structure
        serialization_counts[sub_tree_repr]++;
        return sub_tree_repr;
    }

    // Step 2: Post-order traversal to mark identical folders for deletion
    void markDuplicates(TrieNode* node) {
        if (node->children.empty()) {
            return;
        }

        // Reconstruct the same sub-tree representation
        string sub_tree_repr = "";
        for (auto& pair : node->children) {
            sub_tree_repr += "(" + pair.first + serialize_cached(pair.second) + ")";
        }

        // If this sub-tree structure is seen more than once, mark it as deleted
        if (serialization_counts[sub_tree_repr] > 1) {
            node->deleted = true;
            return; // Once marked, we can prune processing its children
        }

        for (auto& pair : node->children) {
            markDuplicates(pair.second);
        }
    }

    // Fast serialization utilizing already tracked child node structures for step 2
    string serialize_cached(TrieNode* node) {
        if (node->children.empty()) return "";
        string res = "";
        for (auto& pair : node->children) {
            res += "(" + pair.first + serialize_cached(pair.second) + ")";
        }
        return res;
    }

    // Step 3: DFS to gather all paths that are not deleted
    void gatherRemainingPaths(TrieNode* node, vector<string>& current_path, vector<vector<string>>& result) {
        if (node->deleted) {
            return; // Sub-tree is deleted, ignore it and all its children
        }

        if (node != root) {
            current_path.push_back(node->name);
            result.push_back(current_path);
        }

        for (auto& pair : node->children) {
            gatherRemainingPaths(pair.second, current_path, result);
        }

        if (node != root) {
            current_path.pop_back();
        }
    }

    // Helper to free allocated memory
    void deleteTree(TrieNode* node) {
        for (auto& pair : node->children) {
            deleteTree(pair.second);
        }
        delete node;
    }

public:
    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        root = new TrieNode();
        serialization_counts.clear();

        // 1. Build the Trie file system structure
        for (const auto& path : paths) {
            insert(path);
        }

        // 2. Serialize sub-trees and find duplication frequencies
        serialize(root);

        // 3. Mark the duplicated folder nodes
        markDuplicates(root);

        // 4. Collect paths of all non-deleted folders
        vector<vector<string>> result;
        vector<string> current_path;
        gatherRemainingPaths(root, current_path, result);

        // Clean up memory
        deleteTree(root);

        return result;
    }
};