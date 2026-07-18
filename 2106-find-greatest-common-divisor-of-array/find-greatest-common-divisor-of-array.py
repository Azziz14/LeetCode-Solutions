import math
from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        # Step 1: Find the smallest and largest elements
        min_num = min(nums)
        max_num = max(nums)
        
        # Step 2: Compute and return their GCD
        return math.gcd(min_num, max_num)
