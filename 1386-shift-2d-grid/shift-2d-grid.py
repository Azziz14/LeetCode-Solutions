class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(grid), len(grid[0])
        total_elements = m * n
        
        # Optimize k if it's larger than total elements
        k = k % total_elements
        
        # Initialize an empty result grid with the same dimensions
        result = [[0] * n for _ in range(m)]
        
        for r in range(m):
            for c in range(n):
                # Convert 2D coordinate to 1D index
                old_1d_index = r * n + c
                
                # Apply the shift and wrap around using modulo
                new_1d_index = (old_1d_index + k) % total_elements
                
                # Convert 1D index back to 2D coordinate
                new_r = new_1d_index // n
                new_c = new_1d_index % n
                
                # Assign the value to its new destination
                result[new_r][new_c] = grid[r][c]
                
        return result
