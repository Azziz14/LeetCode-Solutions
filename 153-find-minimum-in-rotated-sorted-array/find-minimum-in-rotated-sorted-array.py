class Solution:
    def findMin(self, nums: List[int]) -> int:
        answer = nums[0] 
        min_ans = nums[0]
        for i in range(1,len(nums)):
            if nums[i]<min_ans:
                min_ans = nums[i]
                answer = min(answer,min_ans)
        return answer
