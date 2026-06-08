class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        Find the minimum path sum from top-left to bottom-right corner.
        Movement is only allowed down or right at any point.
      
        Args:
            grid: 2D list of non-negative integers
          
        Returns:
            Minimum sum of all numbers along the path
        """
        # Get dimensions of the grid
        rows, cols = len(grid), len(grid[0])
      
        # Initialize DP table to store minimum path sum to each cell
        dp = [[0] * cols for _ in range(rows)]
      
        # Base case: starting position
        dp[0][0] = grid[0][0]
      
        # Initialize first column (can only come from above)
        for row in range(1, rows):
            dp[row][0] = dp[row - 1][0] + grid[row][0]
      
        # Initialize first row (can only come from left)
        for col in range(1, cols):
            dp[0][col] = dp[0][col - 1] + grid[0][col]
      
        # Fill the DP table for remaining cells
        # Each cell's minimum path sum is the minimum of coming from above or left
        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + grid[row][col]
      
        # Return the minimum path sum to reach bottom-right corner
        return dp[-1][-1]
