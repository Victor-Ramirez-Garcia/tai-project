from typing import List

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(4^(m * n)) in worst-case, but constrained heavily by the grid size (m * n <= 20)
        # Space Complexity: O(m * n) for the recursion stack
        # Algorithm: Backtracking (DFS) with state modifications to track visited cells.
        
        m, n = len(grid), len(grid[0])
        start_r, start_c = 0, 0
        empty_count = 0
        
        # Count the number of non-obstacle squares to visit and locate the starting position
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    start_r, start_c = r, c
                    empty_count += 1
                elif grid[r][c] == 0:
                    empty_count += 1
                elif grid[r][c] == 2:
                    empty_count += 1  # The target cell counts as a required step
                    
        paths_count = 0
        
        def backtrack(r: int, c: int, remain: int) -> None:
            nonlocal paths_count
            
            # Base case: if we reach the end square and have visited all required cells
            if grid[r][c] == 2:
                if remain == 1:
                    paths_count += 1
                return
            
            # Mark the current cell as visited using an obstacle placeholder (-1)
            temp = grid[r][c]
            grid[r][c] = -1
            
            # Explore all 4-directional neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != -1:
                    backtrack(nr, nc, remain - 1)
            
            # Undo the choice (backtrack) to restore the original grid state
            grid[r][c] = temp

        # Start the backtracking search from the starting square
        backtrack(start_r, start_c, empty_count)
        return paths_count