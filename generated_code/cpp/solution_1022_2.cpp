#include <vector>

using namespace std;

class Solution {
private:
    int totalPaths = 0;
    int emptySquaresCount = 0;
    int targetRow = 0;
    int targetCol = 0;
    int rows = 0;
    int cols = 0;

    void backtrack(vector<vector<int>>& grid, int r, int c, int visitedCount) {
        // Base Case: If we reach the destination
        if (r == targetRow && c == targetCol) {
            // Check if we visited all non-obstacle squares (including the start square)
            if (visitedCount == emptySquaresCount) {
                totalPaths++;
            }
            return;
        }

        // 4-directional choices
        int dr[] = {-1, 1, 0, 0};
        int dc[] = {0, 0, -1, 1};

        for (int i = 0; i < 4; ++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            // Validate boundaries and check if the square is walkable (0 or 2)
            if (nr >= 0 && nr < rows && nc >= 0 && nc < cols && grid[nr][nc] >= 0) {
                int originalVal = grid[nr][nc];
                
                // Mark as visited using -2 to avoid revisit
                grid[nr][nc] = -2; 
                
                // Explore next step
                backtrack(grid, nr, nc, visitedCount + 1);
                
                // Backtrack and restore original value
                grid[nr][nc] = originalVal; 
            }
        }
    }

public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        rows = grid.size();
        cols = grid[0].size();
        
        int startRow = 0, startCol = 0;
        emptySquaresCount = 0;
        totalPaths = 0;

        // Count required steps and locate start and end positions
        for (int r = 0; r < rows; ++r) {
            for (int c = 0; c < cols; ++c) {
                if (grid[r][c] != -1) {
                    emptySquaresCount++; // Count all valid squares (0, 1, 2)
                }
                if (grid[r][c] == 1) {
                    startRow = r;
                    startCol = c;
                } else if (grid[r][c] == 2) {
                    targetRow = r;
                    targetCol = c;
                }
            }
        }

        // Temporarily mark the starting position as visited
        grid[startRow][startCol] = -2;
        
        // Start backtracking from the starting position with initial count 1
        backtrack(grid, startRow, startCol, 1);

        return totalPaths;
    }
};