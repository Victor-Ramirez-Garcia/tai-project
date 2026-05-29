#include <string>
#include <sstream>
#include <vector>

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
private:
    // Helper function for serialization using pre-order traversal (DFS).
    void serializeDFS(TreeNode* root, std::ostringstream& out) {
        if (!root) {
            out << "# "; // Use '#' to represent a null node, separated by a space
            return;
        }
        out << root->val << " ";
        serializeDFS(root->left, out);
        serializeDFS(root->right, out);
    }

    // Helper function for deserialization using pre-order traversal (DFS).
    TreeNode* deserializeDFS(std::istringstream& in) {
        std::string val_str;
        if (!(in >> val_str)) {
            return nullptr;
        }
        
        if (val_str == "#") {
            return nullptr;
        }

        // Reconstruct the current node and its subtrees recursively
        TreeNode* root = new TreeNode(std::stoi(val_str));
        root->left = deserializeDFS(in);
        root->right = deserializeDFS(in);
        return root;
    }

public:
    // Encodes a tree to a single string.
    // Time Complexity: O(N) where N is the number of nodes.
    // Space Complexity: O(N) for the recursion stack and output stream.
    std::string serialize(TreeNode* root) {
        std::ostringstream out;
        serializeDFS(root, out);
        return out.str();
    }

    // Decodes your encoded data to tree.
    // Time Complexity: O(N) where N is the number of nodes.
    // Space Complexity: O(N) for the recursion stack and input stream.
    TreeNode* deserialize(std::string data) {
        std::istringstream in(data);
        return deserializeDFS(in);
    }
};

// Your Codec object will be instantiated and called as such:
// Codec ser, deser;
// TreeNode* ans = deser.deserialize(ser.serialize(root));