class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        # Initialize DP array with a copy of the triangle's bottom row
        dp = list(triangle[-1])
        
        # Iterate backwards from the second-to-last row up to the top
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update current position with the minimum of its two children
                dp[col] = triangle[row][col] + min(dp[col], dp[col + 1])
                
        # The top element now holds the total minimum path sum
        return dp[0]
