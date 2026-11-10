class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for j in range(1, n + 1):
            # Check previous up to 3 steps: j - 1, j - 2, j - 3
            for i in range(max(0, j - 3), j):
                cost = dp[i] + costs[j - 1] + (j - i) ** 2
                if cost < dp[j]:
                    dp[j] = cost
                    
        return dp[n]