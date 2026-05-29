#include <vector>

using namespace std;

class Solution {
private:
    int totalPaths = 0;
    int emptyCells = 0;
    int startRow = 0, startCol = 0;
    int numRows, numCols;

    // Backtracking function to explore all valid paths
    void backtrack(vector<vector<int>>& grid, int r, int c, int visitedCount) {
        // Base case: Reached the ending square
        if (grid[r][c] == 2) {
            // Check if all non-obstacle cells (including the start cell) have been visited
            if (visitedCount == emptyCells + 1) {
                totalPaths++;
            }
            return;
        }

        // Mark the current cell as visited using an obstacle placeholder (-1)
        int temp = grid[r][c];
        grid[r][c] = -1;

        // 4-directional displacements
        int dRow[] = {-1, 1, 0, 0};
        int dCol[] = {0, 0, -1, 1};

        for (int i = 0; i < 4; ++i) {
            int nextR = r + dRow[i];
            int nextC = c + dCol[i];

            // Validate boundaries and check if the cell is unvisited/empty or the destination
            if (nextR >= 0 && nextR < numRows && nextC >= 0 && nextC < numCols) {
                if (grid[nextR][nextC] == 0 || grid[nextR][nextC] == 2) {
                    backtrack(grid, nextR, nextC, visitedCount + 1);
                }
            }
        }

        // Restore the cell state for other paths (backtrack step)
        grid[r][c] = temp;
    }

public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        numRows = grid.size();
        numCols = grid[0].size();
        totalPaths = 0;
        emptyCells = 0;

        // Identify starting point and count total empty squares to visit
        for (int i = 0; i < numRows; ++i) {
            for (int j = 0; j < numCols; ++j) {
                if (grid[i][j] == 1) {
                    startRow = i;
                    startCol = j;
                } else if (grid[i][j] == 0) {
                    emptyCells++;
                }
            }
        }

        // Kick off backtracking starting at count 1 (counting the start cell itself)
        backtrack(grid, startRow, startCol, 1);

        return totalPaths;
    }
};