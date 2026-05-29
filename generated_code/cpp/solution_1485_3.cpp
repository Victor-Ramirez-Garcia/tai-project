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
        // Using 0-indexed offset array corresponding to 1, 2, 3, 4
        int dx[] = {0, 0, 1, -1};
        int dy[] = {1, -1, 0, 0};
        
        // Distance array initialized to a large value (infinity)
        vector<vector<int>> dist(m, vector<int>(n, 1e9));
        
        // Deque for 0-1 BFS
        deque<pair<int, int>> dq;
        
        // Start from (0, 0) with a cost of 0
        dist[0][0] = 0;
        dq.push_front({0, 0});
        
        while (!dq.empty()) {
            auto [r, c] = dq.front();
            dq.pop_front();
            
            // If we reached the bottom-right corner, we can return immediately
            if (r == m - 1 && c == n - 1) {
                return dist[r][c];
            }
            
            // Explore all 4 possible neighboring directions
            for (int i = 0; i < 4; ++i) {
                int nr = r + dx[i];
                int nc = c + dy[i];
                
                // Ensure the neighboring cell is within grid boundaries
                if (nr >= 0 && nr < m && nc >= 0 && nc < n) {
                    // Cost is 0 if moving in the direction of the arrow, otherwise 1
                    int cost = (grid[r][c] == i + 1) ? 0 : 1;
                    
                    // Relaxation step
                    if (dist[r][c] + cost < dist[nr][nc]) {
                        dist[nr][nc] = dist[r][c] + cost;
                        if (cost == 0) {
                            dq.push_front({nr, nc}); // Higher priority
                        } else {
                            dq.push_back({nr, nc});  // Lower priority
                        }
                    }
                }
            }
        }
        
        return dist[m - 1][n - 1];
    }
};