import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        max_so_far = -1
        
        # Step 1: Build the prefix GCD array
        for num in nums:
            max_so_far = max(max_so_far, num)
            prefixGcd.append(math.gcd(num, max_so_far))
            
        # Step 2: Sort the array
        prefixGcd.sort()
        
        # Step 3: Two-pointer inward simulation
        total_sum = 0
        left, right = 0, len(prefixGcd) - 1
        while left < right:
            total_sum += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return total_sum
