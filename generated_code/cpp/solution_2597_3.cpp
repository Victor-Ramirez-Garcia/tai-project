#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> cycleLengthQueries(int n, vector<vector<int>>& queries) {
        vector<int> answer;
        answer.reserve(queries.size());
        
        for (const auto& query : queries) {
            int u = query[0];
            int v = query[1];
            int distance = 0;
            
            // Move up the tree from both nodes until they meet at their Lowest Common Ancestor (LCA).
            // In a binary tree where the parent of node `val` is `val / 2`, we can find the LCA 
            // by repeatedly dividing the larger node value by 2. Each division corresponds to 
            // traversing one edge upward.
            while (u != v) {
                if (u > v) {
                    u /= 2;
                } else {
                    v /= 2;
                }
                distance++;
            }
            
            // The length of the cycle is the distance between the two nodes in the tree 
            // plus 1 for the newly added edge connecting them.
            answer.push_back(distance + 1);
        }
        
        return answer;
    }
};