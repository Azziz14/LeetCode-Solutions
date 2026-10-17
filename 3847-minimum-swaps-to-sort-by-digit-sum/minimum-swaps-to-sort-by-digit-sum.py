from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            return sum(int(digit) for digit in str(n))
        
        n = len(nums)
        # Pair each number with its (digit_sum, value, original_index)
        indexed_nums = []
        for i, val in enumerate(nums):
            indexed_nums.append((get_digit_sum(val), val, i))
        
        # Sort based on digit sum, then by value (as a tiebreaker)
        indexed_nums.sort(key=lambda x: (x[0], x[1]))
        
        # Find the minimum swaps using cycle detection on permutations
        visited = [False] * n
        swaps = 0
        
        for i in range(n):
            if visited[i] or indexed_nums[i][2] == i:
                continue
            
            # Traverse the cycle
            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = indexed_nums[curr][2]
                cycle_size += 1
            
            if cycle_size > 1:
                swaps += (cycle_size - 1)
                
        return swaps