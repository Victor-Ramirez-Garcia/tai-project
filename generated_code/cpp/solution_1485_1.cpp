#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Directions corresponding to the grid sign values:
        // 1: Right, 2: Left, 3: Down, 4: Up
        // Using 0-indexed offset array for convenience:
        // Index 0: Dummy, Index 1: Right, Index 2: Left, Index 3: Down, Index 4: Up
        int dr[] = {0, 0, 0, 1, -1};
        int dc[] = {0, 1, -1, 0, 0};
        
        // Distance array initialized to infinity
        vector<vector<int>> dist(m, vector<int>(n, 1e9));
        
        // Double-ended queue for 0-1 BFS
        deque<pair<int, int>> dq;
        
        // Start from top-left cell
        dist[0][0] = 0;
        dq.push_back({0, 0});
        
        while (!dq.empty()) {
            auto [r, c] = dq.front();
            dq.pop_front();
            
            // If we reached the destination, we can return the cost immediately
            if (r == m - 1 && c == n - 1) {
                return dist[r][c];
            }
            
            // Explore all 4 possible directions
            for (int i = 1; i <= 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                // Check grid boundaries
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    // Cost is 0 if the direction matches the grid's sign, else 1
                    int weight = (grid[r][c] == i) ? 0 : 1;
                    
                    if (dist[r][c] + weight < dist[nr][nc]) {
                        dist[nr][nc] = dist[r][c] + weight;
                        // 0-1 BFS optimization: 
                        // Push to front if weight is 0, push to back if weight is 1
                        if (weight == 0) {
                            dq.push_front({nr, nc});
                        } else {
                            dq.push_back({nr, nc});
                        }
                    }
                }
            }
        }
        
        return dist[m - 1][n - 1];
    }
};