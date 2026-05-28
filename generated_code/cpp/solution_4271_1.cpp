#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findDegrees(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> ans(n, 0);
        
        // The degree of a vertex i in an adjacency matrix is the sum of elements in its row.
        // For an undirected graph, self-loops (matrix[i][i] == 1) contribute to the count 
        // depending on definition, but typically matrix[i][j] == 1 means an edge.
        // We iterate through the matrix and count the number of 1s in each vertex's row.
        for (int i = 0; i < n; ++i) {
            int degree = 0;
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] == 1) {
                    degree++;
                }
            }
            ans[i] = degree;
        }
        
        return ans;
    }
};