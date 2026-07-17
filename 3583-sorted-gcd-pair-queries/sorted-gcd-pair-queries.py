import math
from typing import List
from itertools import accumulate
import bisect

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        max_num = max(nums)
        
        # Step 1: Count frequency of each number
        freq = [0] * (max_num + 1)
        for num in nums:
            freq[num] += 1
            
        # Step 2: Compute pairs with exact GCD using inclusion-exclusion backwards
        gcd_pair_counts = [0] * (max_num + 1)
        
        for i in range(max_num, 0, -1):
            # Count elements that are multiples of i
            total_multiples = 0
            for j in range(i, max_num + 1, i):
                total_multiples += freq[j]
                
            # Form total pairs from these multiples
            pairs = total_multiples * (total_multiples - 1) // 2
            
            # Subtract pairs that have a strictly larger multiple as their true GCD
            for j in range(2 * i, max_num + 1, i):
                pairs -= gcd_pair_counts[j]
                
            gcd_pair_counts[i] = pairs
            
        # Step 3: Construct the prefix sum array
        prefix_sums = list(accumulate(gcd_pair_counts))
        
        # Step 4: Answer each query via binary search
        ans = []
        for q in queries:
            # We look for the first GCD index where cumulative pairs > q
            idx = bisect.bisect_right(prefix_sums, q)
            ans.append(idx)
            
        return ans
