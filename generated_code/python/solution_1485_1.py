from typing import List
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        Algorithm: 0-1 BFS (or Dijkstra's Algorithm)
        
        We treat the grid as a weighted graph where traversing in the direction
        of the arrow costs 0, and changing the direction to any other valid neighbor 
        costs 1. Since edge weights are only 0 and 1, a 0-1 BFS utilizing a double-ended 
        queue (deque) achieves the optimal O(m * n) time complexity.
        
        - 0-cost transitions: Appended to the front of the deque (processed first).
        - 1-cost transitions: Appended to the back of the deque.
        """
        m, n = len(grid), len(grid[0])
        
        # Directions mapping: 1 -> Right, 2 -> Left, 3 -> Down, 4 -> Up
        # Using 1-indexed indexing matching grid values
        dirs = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        
        # Minimum cost table to reach each cell initialized to infinity
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # Deque stores tuples of (row, col)
        dq = deque([(0, 0)])
        
        while dq:
            r, c = dq.popleft()
            
            # Since we can reach the end node early through 0-cost paths, 
            # we can stop as soon as we pop the destination cell.
            if r == m - 1 and c == n - 1:
                return dist[r][c]
                
            # Explore all 4 possible neighboring directions
            for d, (dr, dc) in dirs.items():
                nr, nc = r + dr, c + dc
                
                # Verify boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # If the current arrow points to this neighbor, cost is 0. Else, cost is 1.
                    cost = 0 if grid[r][c] == d else 1
                    
                    # Relaxation step
                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost
                        if cost == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))
                            
        return dist[m - 1][n - 1]