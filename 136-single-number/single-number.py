class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = 0
        
        # XOR every number in the array
        for num in nums:
            result ^= num
            
        return result

