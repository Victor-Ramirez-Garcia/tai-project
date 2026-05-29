from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(4^(M*N)) worst-case, but heavily pruned by grid boundaries and obstacles. 
        # Given constraints (M * N <= 20), DFS with backtracking is optimal and efficient.
        # Space Complexity: O(M * N) for the recursion stack.
        
        m, n = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        empty_slots = 0
        
        # Step 1: Find the starting position and count the number of squares to visit.
        # We need to visit all '0's and the starting square '1', so total squares to visit
        # equals (count of 0s) + 1.
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    empty_slots += 1
                elif grid[r][c] == 0:
                    empty_slots += 1
                    
        paths_count = 0
        
        # Step 2: DFS with backtracking to find all valid paths.
        def dfs(r: int, c: int, remain: int):
            nonlocal paths_count
            
            # Base Case: If we reach the destination square '2'
            if grid[r][c] == 2:
                # If we visited all required squares, we found a valid path.
                if remain == 0:
                    paths_count += 1
                return
            
            # Mark the current square as visited using an obstacle placeholder (-1)
            temp = grid[r][c]
            grid[r][c] = -1
            
            # Explore 4-directional neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                # Check boundaries and ensure the neighbor is walkover-able (0 or 2)
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    dfs(nr, nc, remain - 1)
                    
            # Backtrack: Restore the original value of the square
            grid[r][c] = temp

        # Start the DFS traversal from the starting square.
        # 'remain' tracks how many squares (including the target) are left to visit.
        dfs(start_r, start_c, empty_slots)
        
        return paths_count