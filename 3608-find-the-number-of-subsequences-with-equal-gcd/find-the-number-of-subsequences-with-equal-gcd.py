import math

class Solution:
    def subsequencePairCount(self, nums: list[int]) -> int:
        MOD = 1_000_000_007
        max_num = max(nums)
        
        # Space-optimized DP table
        dp = [[0] * (max_num + 1) for _ in range(max_num + 1)]
        dp[0][0] = 1  # Base case: Both seq1 and seq2 are empty initially
        
        for num in nums:
            next_dp = [row[:] for row in dp]  # Create a copy for the next state
            for x in range(max_num + 1):
                for y in range(max_num + 1):
                    if dp[x][y] == 0:
                        continue
                    
                    ways = dp[x][y]
                    
                    # Option 1: Put 'num' in seq1
                    nx = math.gcd(x, num)
                    next_dp[nx][y] = (next_dp[nx][y] + ways) % MOD
                    
                    # Option 2: Put 'num' in seq2
                    ny = math.gcd(y, num)
                    next_dp[x][ny] = (next_dp[x][ny] + ways) % MOD
            
            dp = next_dp
            
        # Sum counts where both GCDs match and are greater than 0
        ans = sum(dp[g][g] for g in range(1, max_num + 1)) % MOD
        return ans
