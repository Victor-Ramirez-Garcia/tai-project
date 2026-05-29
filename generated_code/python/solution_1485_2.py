from typing import List
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        """
        Algorithm: 0-1 Breadth-First Search (BFS) / Shortest Path.
        
        The problem can be modeled as finding the shortest path in a weighted graph 
        where the edge weight is 0 if the neighbor aligns with the arrow in the current cell,
        and 1 if we need to change the arrow to point to that neighbor.
        
        Using a double-ended queue (deque) allows us to find the shortest path in O(V + E) time.
        Edges with weight 0 are pushed to the front of the deque, and edges with weight 1 
        are pushed to the back.
        
        Time Complexity: O(m * n) - each cell is processed at most once.
        Space Complexity: O(m * n) - for the distance grid and the deque.
        """
        m, n = len(grid), len(grid[0])
        
        # Directions mapping matching the 1-indexed problem statement:
        # 1: right, 2: left, 3: down, 4: up
        # We add a dummy element at index 0 for 1-based indexing alignment
        dirs = [(), (0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Initialize the distance matrix with a large value representing infinity
        dist = [[float('inf')] * n for _ in range(m)]
        dist[0][0] = 0
        
        # 0-1 BFS queue storing tuples of (row, col)
        queue = deque([(0, 0)])
        
        while queue:
            r, c = queue.popleft()
            
            # Since we can reach the target cell with optimal cost early,
            # we can return immediately if we process the bottom-right cell.
            if r == m - 1 and c == n - 1:
                return dist[r][c]
            
            # Explore all 4 possible neighboring directions
            for i in range(1, 5):
                dr, dc = dirs[i]
                nr, nc = r + dr, c + dc
                
                # Check grid boundaries
                if 0 <= nr < m and 0 <= nc < n:
                    # Cost is 0 if the current grid arrow matches the direction 'i'
                    # Otherwise, the cost to change the arrow is 1
                    cost = 0 if grid[r][c] == i else 1
                    
                    # If a cheaper path to the neighbor is found, update and push to queue
                    if dist[r][c] + cost < dist[nr][nc]:
                        dist[nr][nc] = dist[r][c] + cost
                        if cost == 0:
                            queue.appendleft((nr, nc)) # 0-weight edges prioritized
                        else:
                            queue.append((nr, nc))     # 1-weight edges deferred
                            
        return dist[m-1][n-1]