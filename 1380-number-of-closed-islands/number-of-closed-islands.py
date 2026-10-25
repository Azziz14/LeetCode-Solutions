class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # If out of bounds, the island touches the border (not closed)
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            # If water (1) or already visited, return True (doesn't invalidate the island)
            if grid[r][c] == 1:
                return True
            
            # Mark the current cell as visited by turning it into water (1)
            grid[r][c] = 1
            
            # Explore all 4 directions
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            
            # An island is closed only if all four directions are valid closed paths
            return left and right and up and down

        closed_islands = 0
        
        for r in range(rows):
            for c in range(cols):
                # Find an unvisited land cell (0)
                if grid[r][c] == 0:
                    if dfs(r, c):
                        closed_islands += 1
                        
        return closed_islands
        