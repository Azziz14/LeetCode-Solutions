import math
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        # Helper function to count distinct multiples <= x using PIE
        def count_less_equal(x: int) -> int:
            total_count = 0
            # Iterate through all non-empty subsets using bitmasking
            for mask in range(1, 1 << n):
                bits_set = 0
                lcm_val = 1
                for i in range(n):
                    if (mask >> i) & 1:
                        bits_set += 1
                        lcm_val = math.lcm(lcm_val, coins[i])
                        # Early exit if LCM exceeds x to prevent unnecessary work
                        if lcm_val > x:
                            break
                
                if lcm_val <= x:
                    # Odd size subset -> Add, Even size subset -> Subtract
                    if bits_set % 2 == 1:
                        total_count += x // lcm_val
                    else:
                        total_count -= x // lcm_val
            return total_count

        # Binary search bounds
        low = 1
        high = min(coins) * k
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if count_less_equal(mid) >= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans