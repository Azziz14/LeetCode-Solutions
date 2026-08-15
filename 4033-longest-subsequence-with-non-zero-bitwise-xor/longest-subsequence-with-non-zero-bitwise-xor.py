class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        # Case 1: All elements are 0
        if all(x == 0 for x in nums):
            return 0
        
        # Calculate total XOR sum
        total_xor = 0
        for num in nums:
            total_xor ^= num
            
        # Case 2 & 3: Total XOR check
        return len(nums) if total_xor != 0 else len(nums) - 1
