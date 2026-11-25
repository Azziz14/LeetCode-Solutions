from collections import Counter


class Solution:
    def smallestUniqueSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        base1, mod1 = 100003, 10**9 + 7
        base2, mod2 = 100019, 10**9 + 9

        p1 = [1] * (n + 1)
        p2 = [1] * (n + 1)
        h1 = [0] * (n + 1)
        h2 = [0] * (n + 1)

        for i in range(n):
            p1[i + 1] = (p1[i] * base1) % mod1
            p2[i + 1] = (p2[i] * base2) % mod2
            h1[i + 1] = (h1[i] * base1 + nums[i]) % mod1
            h2[i + 1] = (h2[i] * base2 + nums[i]) % mod2

        def has_unique_of_len(length: int) -> bool:
            counts = Counter()
            for i in range(n - length + 1):
                j = i + length
                hash1 = (h1[j] - h1[i] * p1[length]) % mod1
                hash2 = (h2[j] - h2[i] * p2[length]) % mod2
                counts[(hash1, hash2)] += 1
            return any(c == 1 for c in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique_of_len(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        return ans