class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        
        # Early exit if s is shorter than t
        if n < m:
            return 0
            
        # dp[i] stores the number of distinct subsequences matching t[0...i-1]
        dp = [0] * (m + 1)
        
        # Base case: An empty string t has exactly 1 subsequence match (the empty subsequence)
        dp[0] = 1
        
        # Iterate through each character of s
        for j in range(1, n + 1):
            # Traverse backwards to use values from the previous iteration safely
            for i in range(m, 0, -1):
                if t[i - 1] == s[j - 1]:
                    dp[i] = dp[i] + dp[i - 1]
                    
        return dp[m]
