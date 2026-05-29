#include <string>
#include <sstream>
#include <queue>
#include <vector>

using namespace std;

// Definition for a binary tree node.
// Included to ensure the file is entirely self-contained and compilable.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Codec {
public:
    // Encodes a tree to a single string using Level Order Traversal (BFS).
    // Time Complexity: O(N) where N is the number of nodes.
    // Space Complexity: O(N) to store the nodes in the queue and the result string.
    string serialize(TreeNode* root) {
        if (!root) return "#";
        
        string result = "";
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* curr = q.front();
            q.pop();
            
            if (curr) {
                result += to_string(curr->val) + ",";
                q.push(curr->left);
                q.push(curr->right);
            } else {
                result += "#,";
            }
        }
        
        // Remove the trailing comma for clean parsing
        if (!result.empty()) result.pop_back();
        return result;
    }

    // Decodes your encoded data to tree using a queue to reconstruct the level order.
    // Time Complexity: O(N) where N is the number of elements in the string.
    // Space Complexity: O(N) for storing the split values and the reconstruction queue.
    TreeNode* deserialize(string data) {
        if (data == "#") return nullptr;
        
        stringstream ss(data);
        string item;
        vector<string> values;
        
        // Split the CSV string into individual tokens
        while (getline(ss, item, ',')) {
            values.push_back(item);
        }
        
        TreeNode* root = new TreeNode(stoi(values[0]));
        queue<TreeNode*> q;
        q.push(root);
        
        int i = 1; // Pointer to iterate through the values vector
        while (!q.empty() && i < values.size()) {
            TreeNode* parent = q.front();
            q.pop();
            
            // Process the left child
            if (values[i] != "#") {
                TreeNode* leftChild = new TreeNode(stoi(values[i]));
                parent->left = leftChild;
                q.push(leftChild);
            }
            i++;
            
            // Ensure we don't out-of-bounds check if string is malformed
            if (i >= values.size()) break;
            
            // Process the right child
            if (values[i] != "#") {
                TreeNode* rightChild = new TreeNode(stoi(values[i]));
                parent->right = rightChild;
                q.push(rightChild);
            }
            i++;
        }
        
        return root;
    }
};