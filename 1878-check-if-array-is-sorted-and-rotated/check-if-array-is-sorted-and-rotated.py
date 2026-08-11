class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0 
        for i in range(n):
            next_num = (i+1)%n
            if nums[i]>nums[next_num]:
                count+=1
        return count<=1