#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    vector<int> findDegrees(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> ans(n, 0);
        
        // The degree of a vertex i in an adjacency matrix is the sum of its row elements.
        // For an undirected graph without self-loops, summing matrix[i][j] gives the count of edges connected to i.
        for (int i = 0; i < n; ++i) {
            ans[i] = std::accumulate(matrix[i].begin(), matrix[i].end(), 0);
        }
        
        return ans;
    }
};