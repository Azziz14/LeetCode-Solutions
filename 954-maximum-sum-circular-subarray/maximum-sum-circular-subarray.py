class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        currmax= nums[0]
        currmin = nums[0]
        n = len(nums)
        max_sum = nums[0]
        min_sum=nums[0]
        for i in range(1,n):
            currmax = max(nums[i],currmax+nums[i])
            max_sum = max(max_sum,currmax)
            currmin = min(nums[i],currmin+nums[i])
            min_sum= min(min_sum,currmin)
        if max_sum<0:
            return max_sum
        return max(max_sum,total-min_sum)