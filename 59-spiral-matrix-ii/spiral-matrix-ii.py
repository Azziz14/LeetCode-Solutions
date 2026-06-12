class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        Generate an n x n matrix filled with elements from 1 to n² in spiral order.
      
        Args:
            n: The size of the square matrix
          
        Returns:
            A 2D list representing the spiral matrix
        """
        # Initialize n x n matrix filled with zeros
        matrix = [[0] * n for _ in range(n)]
      
        # Direction vectors: right, down, left, up
        # Using pairs: (row_delta, col_delta) for each direction
        directions = [0, 1, 0, -1, 0]  # Compact representation of (0,1), (1,0), (0,-1), (-1,0)
      
        # Starting position and direction index
        row = col = 0  # Start at top-left corner
        direction_index = 0  # Start moving right
      
        # Fill the matrix with values from 1 to n²
        for value in range(1, n * n + 1):
            # Place current value at current position
            matrix[row][col] = value
          
            # Calculate next position based on current direction
            next_row = row + directions[direction_index]
            next_col = col + directions[direction_index + 1]
          
            # Check if we need to change direction:
            # - If next position is out of bounds
            # - If next position is already filled (non-zero)
            if (next_row < 0 or next_row >= n or 
                next_col < 0 or next_col >= n or 
                matrix[next_row][next_col] != 0):
                # Turn clockwise (move to next direction)
                direction_index = (direction_index + 1) % 4
          
            # Move to next position using current (possibly updated) direction
            row += directions[direction_index]
            col += directions[direction_index + 1]
      
        return matrix