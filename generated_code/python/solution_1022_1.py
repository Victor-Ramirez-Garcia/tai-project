from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(4^(m*n)) in the worst case, but heavily pruned. 
        # Given constraints (m * n <= 20), back tracking is highly efficient and optimal.
        # Space Complexity: O(m * n) for the recursion call stack.
        
        m, n = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        empty_squares = 0
        
        # Step 1: Scan the grid to find the starting position and count total walkable squares
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    empty_squares += 1
                elif grid[r][c] == 0:
                    empty_squares += 1
                elif grid[r][c] == 2:
                    empty_squares += 1  # Include the ending square in the count
                    
        self.paths_count = 0
        
        # Step 2: Define backtracking function to explore paths
        def backtrack(r: int, c: int, remain: int):
            # Base Case: If we reach the target square
            if grid[r][c] == 2:
                # If all non-obstacle squares have been visited, we found a valid path
                if remain == 1:
                    self.paths_count += 1
                return
            
            # Mark the current square as visited by temporarily setting it as an obstacle
            temp = grid[r][c]
            grid[r][c] = -1
            
            # Explore 4-directional neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    backtrack(nr, nc, remain - 1)
                    
            # Backtrack: Restore the square's original value
            grid[r][c] = temp
            
        # Kickstart backtracking from the starting position
        backtrack(start_r, start_c, empty_squares)
        
        return self.paths_count