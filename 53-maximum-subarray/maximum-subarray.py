class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        best_ending = nums[0]
        i = 0
        ans=nums[0]
        for i in range(1,n):
            v1 = best_ending+nums[i]
            v2= nums[i]
            best_ending = max(v1,v2)
            ans = max(ans,best_ending)
        return ans 