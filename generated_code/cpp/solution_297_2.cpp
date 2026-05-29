#include <string>
#include <sstream>
#include <vector>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
private:
    // Helper function for serialization using preorder traversal (DFS).
    void serializeHelper(TreeNode* root, stringstream& ss) {
        if (!root) {
            ss << "# ";
            return;
        }
        // Append the current node's value followed by a space delimiter.
        ss << root->val << " ";
        serializeHelper(root->left, ss);
        serializeHelper(root->right, ss);
    }

    // Helper function for deserialization using a stringstream iterator.
    TreeNode* deserializeHelper(stringstream& ss) {
        string val_str;
        if (!(ss >> val_str)) {
            return nullptr;
        }
        
        // '#' represents a null pointer.
        if (val_str == "#") {
            return nullptr;
        }
        
        // Reconstruct the node and recursively build its left and right subtrees.
        TreeNode* root = new TreeNode(stoi(val_str));
        root->left = deserializeHelper(ss);
        root->right = deserializeHelper(ss);
        return root;
    }

public:
    // Encodes a tree to a single string.
    // Time Complexity: O(N) where N is the number of nodes, as we visit each node once.
    // Space Complexity: O(N) for the recursion stack and the output stream.
    string serialize(TreeNode* root) {
        stringstream ss;
        serializeHelper(root, ss);
        return ss.str();
    }

    // Decodes your encoded data to tree.
    // Time Complexity: O(N) to process the tokens and reconstruct the tree.
    // Space Complexity: O(N) for the call stack during reconstruction and stringstream storage.
    TreeNode* deserialize(string data) {
        if (data.empty()) return nullptr;
        stringstream ss(data);
        return deserializeHelper(ss);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));