#include <vector>
#include <algorithm>

using namespace std;

class Solution {
private:
    int totalPaths = 0;
    int targetEmptySpaces = 0;
    int rows = 0;
    int cols = 0;

    // Helper function for backtracking/DFS
    void dfs(vector<vector<int>>& grid, int r, int c, int visitedCount) {
        // Base Case: Reached the destination square
        if (grid[r][c] == 2) {
            // Check if we visited all non-obstacle squares (including start and end)
            if (visitedCount == targetEmptySpaces) {
                totalPaths++;
            }
            return;
        }

        // Mark the current cell as visited by changing it to an obstacle
        int temp = grid[r][c];
        grid[r][c] = -1;

        // Explore 4-directional neighbors
        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            // Validate boundaries and check if the neighbor is walkable (0 or 2)
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] != -1) {
                dfs(grid, nr, nc, visitedCount + 1);
            }
        }

        // Backtrack: Restore the original cell value
        grid[r][c] = temp;
    }

public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        rows = grid.size();
        cols = grid.size();
        totalPaths = 0;
        targetEmptySpaces = 0;

        int startRow = -1, startCol = -1;

        // Scan the grid to find the start position and count total walkable squares
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] != -1) {
                    targetEmptySpaces++; // Total squares to visit (0, 1, and 2)
                }
                if (grid[r][c] == 1) {
                    startRow = r;
                    startCol = c;
                }
            }
        }

        // Start Backtracking from the starting square, initial count is 1 (the start square itself)
        dfs(grid, startRow, startCol, 1);

        return totalPaths;
    }
};