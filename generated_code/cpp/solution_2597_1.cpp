#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> cycleLengthQueries(int n, vector<vector<int>>& queries) {
        vector<int> ans;
        ans.reserve(queries.size());
        
        for (const auto& q : queries) {
            int u = q[0];
            int v = q[1];
            int edges = 0;
            
            // Move up the tree until both nodes meet at their Lowest Common Ancestor (LCA).
            // In a standard binary heap indexing where parent of x is x / 2, 
            // the node with the larger value is deeper in the tree.
            while (u != v) {
                if (u > v) {
                    u /= 2;
                } else {
                    v /= 2;
                }
                edges++;
            }
            
            // The cycle consists of the path from u to LCA, v to LCA, plus the query edge.
            ans.push_back(edges + 1);
        }
        
        return ans;
    }
};