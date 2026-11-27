from typing import List


class Solution:

    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        max_f = max((f for f, _ in items), default=0)
        free_gain = [0] * len(items)

        for f in range(1, max_f + 1):
            cnt = 0
            for _, p in items:
                if f % p == 0:
                    pass
            divisible_count = 0
            for f2, _ in items:
                if f2 % f == 0:
                    divisible_count += 1
            for i, (f1, _) in enumerate(items):
                if f1 == f:
                    free_gain[i] = divisible_count - 1

        dp = [-10**9] * (budget + 1)
        dp[0] = 0

        for i, (_, price) in enumerate(items):
            gain = 1 + free_gain[i]
            new_dp = dp[:]

            for b in range(price, budget + 1):
                if dp[b - price] + gain > new_dp[b]:
                    new_dp[b] = dp[b - price] + gain

            for b in range(price, budget + 1):
                if new_dp[b - price] + 1 > new_dp[b]:
                    new_dp[b] = new_dp[b - price] + 1

            dp = new_dp

        return max(0, max(dp))