class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        max_element = nums[0]
        answer = 0
        for i in range(1,len(nums)):
            if nums[i]>max_element:
                max_element = nums[i]
                answer = i 
        return answer