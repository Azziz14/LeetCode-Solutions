
from typing import List

class Fenwick:
    def __init__(self, arr):
        self.n = len(arr) - 1
        self.bit = arr[:]

        # O(n) Fenwick construction
        for i in range(1, self.n + 1):
            p = i + (i & -i)
            if p <= self.n:
                self.bit[p] += self.bit[i]

    def add(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i

    def query(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

    def kth(self, k):
        idx = 0
        step = 1 << (self.n.bit_length() - 1)

        while step:
            nxt = idx + step
            if nxt <= self.n and self.bit[nxt] < k:
                idx = nxt
                k -= self.bit[nxt]
            step >>= 1

        return idx + 1


class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        if k * x > n:
            return -1

        vals = sorted(set(nums))
        m = len(vals)
        pos = {v: i + 1 for i, v in enumerate(vals)}

        # Build initial frequency and sum arrays
        freq = [0] * (m + 1)
        total = [0] * (m + 1)
        window_sum = 0

        for i in range(x):
            v = nums[i]
            idx = pos[v]
            freq[idx] += 1
            total[idx] += v
            window_sum += v

        count = Fenwick(freq)
        sums = Fenwick(total)

        costs = []

        # Calculate sliding window costs
        for i in range(n - x + 1):

            median_idx = count.kth((x + 1) // 2)
            median = vals[median_idx - 1]

            lc = count.query(median_idx - 1)
            ls = sums.query(median_idx - 1)

            rc = x - lc - 1
            rs = window_sum - ls - median

            cost = median * lc - ls + rs - median * rc
            costs.append(cost)

            if i + x < n:
                old = nums[i]
                oi = pos[old]

                count.add(oi, -1)
                sums.add(oi, -old)
                window_sum -= old

                new = nums[i + x]
                ni = pos[new]

                count.add(ni, 1)
                sums.add(ni, new)
                window_sum += new

        # Rolling DP
        INF = float('inf')
        prev = [0] * (n + 1)

        for j in range(1, k + 1):
            curr = [INF] * (n + 1)

            for i in range(j * x, n + 1):
                curr[i] = curr[i - 1]

                curr[i] = min(
                    curr[i],
                    prev[i - x] + costs[i - x]
                )

            prev = curr

        return prev[n]
