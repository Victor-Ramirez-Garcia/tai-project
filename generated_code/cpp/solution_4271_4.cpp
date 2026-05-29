#include <vector>

using namespace std;

class Solution {
public:
    /**
     * Problem: Find the degree of each vertex in an undirected graph given its adjacency matrix.
     * Algorithm: The degree of a vertex i in an adjacency matrix is the count of 1s in row i.
     * Time Complexity: O(n^2) - We must visit each element in the n x n matrix.
     * Space Complexity: O(1) - Excluding the output vector, we use constant extra space.
     */
    vector<int> findDegrees(vector<vector<int>>& matrix) {
        int n = matrix.size();
        vector<int> ans(n, 0);

        for (int i = 0; i < n; ++i) {
            int degree = 0;
            for (int j = 0; j < n; ++j) {
                // If matrix[i][j] is 1, there is an edge between vertex i and vertex j
                if (matrix[i][j] == 1) {
                    degree++;
                }
            }
            ans[i] = degree;
        }

        return ans;
    }
};