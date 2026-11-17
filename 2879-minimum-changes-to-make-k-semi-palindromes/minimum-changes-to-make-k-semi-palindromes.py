class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        
        divisors = [[] for _ in range(n + 1)]
        for length in range(2, n + 1):
            for d in range(1, length):
                if length % d == 0:
                    divisors[length].append(d)
                    
        def get_cost(sub: str) -> int:
            m = len(sub)
            min_changes = float('inf')
            for d in divisors[m]:
                changes = 0
                for start in range(d):
                    group = sub[start::d]
                    left, right = 0, len(group) - 1
                    while left < right:
                        if group[left] != group[right]:
                            changes += 1
                        left += 1
                        right -= 1
                min_changes = min(min_changes, changes)
            return min_changes

        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                cost[i][j] = get_cost(s[i:j + 1])
                
        dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        
        for j in range(1, k + 1):
            for i in range(2 * j, n + 1):
                for p in range(2 * (j - 1), i - 1):
                    dp[i][j] = min(dp[i][j], dp[p][j - 1] + cost[p][i - 1])
                    
        return dp[n][k]