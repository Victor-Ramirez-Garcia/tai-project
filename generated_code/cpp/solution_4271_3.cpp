#include <vector>

using namespace std;

class Solution {
public:
    /**
     * Problem: Calculate the degree of each vertex in an undirected graph given its adjacency matrix.
     * * Algorithm:
     * In an adjacency matrix of an undirected graph, the degree of vertex i is the count 
     * of neighbors connected to it. This corresponds to the sum of the i-th row (or i-th column).
     * * Time Complexity: O(n^2) - We must visit each element in the n x n matrix once.
     * Space Complexity: O(1) - Excluding the output array, we use constant extra space.
     */
    vector<int> findDegrees(vector<vector<int>>& matrix) {
        int n = matrix.size();
        if (n == 0) return {};

        vector<int> ans(n, 0);

        for (int i = 0; i < n; ++i) {
            int current_degree = 0;
            for (int j = 0; j < n; ++j) {
                // Since matrix[i][j] is 1 for an edge and 0 otherwise, 
                // we can simply accumulate the value.
                current_degree += matrix[i][j];
            }
            ans[i] = current_degree;
        }

        return ans;
    }
};