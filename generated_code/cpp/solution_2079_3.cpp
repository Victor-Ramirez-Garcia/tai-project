#include <vector>
#include <string>
#include <unordered_map>
#include <map>
#include <algorithm>

using namespace std;

// Trie node structure representing a folder in the file system
struct TrieNode {
    string name;
    // Map to keep subfolders sorted by name to generate a unique, consistent subfolder structure string
    map<string, TrieNode*> children;
    bool deleted = false;

    TrieNode(string n = "") : name(n) {}
};

class Solution {
private:
    TrieNode* root;
    // Map to keep track of the frequency of each subfolder structure representation
    unordered_map<string, int> subfolderStructureCount;
    // Map to store all nodes associated with a specific subfolder structure representation
    unordered_map<string, vector<TrieNode*>> structureToNodes;

    // Helper to insert a path into the Trie
    void insertPath(const vector<string>& path) {
        TrieNode* curr = root;
        for (const string& folder : path) {
            if (curr->children.find(folder) == curr->children.end()) {
                curr->children[folder] = new TrieNode(folder);
            }
            curr = curr->children[folder];
        }
    }

    // Post-order traversal to serialize the subfolder structure of each node
    string serializeStructures(TrieNode* node) {
        if (!node) return "";
        
        string subStructure = "";
        // Process children in sorted order (guaranteed by std::map)
        for (auto& pair : node->children) {
            subStructure += "(" + pair.first + serializeStructures(pair.second) + ")";
        }

        // Only consider nodes that actually have subfolders for duplicate detection
        if (!subStructure.empty()) {
            subfolderStructureCount[subStructure]++;
            structureToNodes[subStructure].push_back(node);
        }

        return subStructure;
    }

    // DFS to extract all paths that haven't been marked for deletion
    void extractPaths(TrieNode* node, vector<string>& currentPath, vector<vector<string>>& result) {
        if (node->deleted) return;

        if (node != root) {
            currentPath.push_back(node->name);
            result.push_back(currentPath);
        }

        for (auto& pair : node->children) {
            extractPaths(pair.second, currentPath, result);
        }

        if (node != root) {
            currentPath.pop_back();
        }
    }

    // Helper to delete the dynamically allocated Trie memory
    void deleteTrie(TrieNode* node) {
        if (!node) return;
        for (auto& pair : node->children) {
            deleteTrie(pair.second);
        }
        delete node;
    }

public:
    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        root = new TrieNode();

        // Step 1: Build the Trie from the input paths
        for (const auto& path : paths) {
            insertPath(path);
        }

        // Step 2: Serialize the structures and identify duplicates via post-order traversal
        serializeStructures(root);

        // Step 3: Mark nodes as deleted if their subfolder structure appears more than once
        for (auto& pair : subfolderStructureCount) {
            if (pair.second > 1) {
                for (TrieNode* node : structureToNodes[pair.first]) {
                    node->deleted = true;
                }
            }
        }

        // Step 4: Reconstruct the remaining non-deleted paths
        vector<vector<string>> result;
        vector<string> currentPath;
        extractPaths(root, currentPath, result);

        // Clean up memory to avoid leaks
        deleteTrie(root);

        return result;
    }
};