#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minCost(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        // Directions: 1 -> right, 2 -> left, 3 -> down, 4 -> up
        // Using 0-indexed arrays matching the 1-based problem directions:
        // Index 1: right (0, 1), Index 2: left (0, -1), Index 3: down (1, 0), Index 4: up (-1, 0)
        int dirs[5][2] = {{0, 0}, {0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        // Distance array initialized to infinity
        vector<vector<int>> dist(m, vector<int>(n, 1e9));
        
        // Deque for 0-1 BFS
        deque<pair<int, int>> dq;
        
        // Start from (0, 0) with a cost of 0
        dist[0][0] = 0;
        dq.push_back({0, 0});
        
        while (!dq.empty()) {
            auto [r, c] = dq.front();
            dq.pop_front();
            
            // If we reached the bottom-right corner, return the minimum cost
            if (r == m - 1 && c == n - 1) {
                return dist[r][c];
            }
            
            // Explore all 4 possible directions
            for (int i = 1; i <= 4; ++i) {
                int nr = r + dirs[i][0];
                int nc = c + dirs[i][1];
                
                // Check boundaries
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    // If the direction matches the grid's arrow, cost is 0. Otherwise, cost is 1.
                    int cost = (grid[r][c] == i) ? 0 : 1;
                    
                    // Relaxation step
                    if (dist[r][c] + cost < dist[nr][nc]) {
                        dist[nr][nc] = dist[r][c] + cost;
                        
                        // 0-1 BFS: push to front if cost is 0, to back if cost is 1
                        if (cost == 0) {
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