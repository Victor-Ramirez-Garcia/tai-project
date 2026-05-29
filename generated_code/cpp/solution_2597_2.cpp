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
            int edges_count = 0;
            
            // Find the Lowest Common Ancestor (LCA) by moving the deeper node up.
            // Since it's a complete binary tree where parent of x is x / 2,
            // we can find the distance to LCA by dividing the larger value by 2
            // until both nodes meet. Each division represents traversing one edge.
            while (u != v) {
                if (u > v) {
                    u /= 2;
                } else {
                    v /= 2;
                }
                edges_count++;
            }
            
            // The cycle consists of the path from u to LCA, v to LCA, plus the new query edge.
            answer.push_back(edges_count + 1);
        }
        
        return answer;
    }
};