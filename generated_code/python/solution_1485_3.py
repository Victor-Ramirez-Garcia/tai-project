from typing import List
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        Algorithm: 0-1 BFS (or Dijkstra's)
        
        We can model the grid as a graph where each cell is a node. From a cell (r, c),
        we can move in 4 directions: Right, Left, Down, Up.
        - Moving in the direction the arrow points has a cost of 0.
        - Moving in any other valid direction has a cost of 1.
        
        Since the edge weights are only 0 and 1, we can use 0-1 BFS using a double-ended 
        queue (deque) to achieve O(m * n) time complexity.
        - If the cost is 0, append to the front of the deque.
        - If the cost is 1, append to the back of the deque.
        
        Time Complexity: O(m * n), each cell is processed at most once.
        Space Complexity: O(m * n) to maintain the distance grid and the deque.
        """
        m, n = len(grid), len(grid[0])
        
        # Directions corresponding to 1: Right, 2: Left, 3: Down, 4: Up
        # We match standard 0-indexed offset arrays with 1-indexed values:
        # Index 0 is a dummy, 1->(0,1), 2->(0,-1), 3->(1,0), 4->(-1,0)
        dirs = [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Distance array initialized to infinity
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Deque for 0-1 BFS: stores tuples of (row, col)
        dq = deque([(0, 0)])
        
        while dq:
            r, c = dq.popleft()
            
            # If we reached the bottom-right corner, return the cost
            if r == m - 1 and c == n - 1:
                return dist[r][c]
            
            # Explore all 4 possible directions
            for i in range(1, 5):
                nr, nc = r + dirs[i][0], c + dirs[i][1]
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # Cost is 0 if we follow the arrow, 1 otherwise
                    cost = 0 if grid[r][c] == i else 1
                    
                    # Relaxation step
                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost
                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
                            
        return dist[m - 1][n - 1]