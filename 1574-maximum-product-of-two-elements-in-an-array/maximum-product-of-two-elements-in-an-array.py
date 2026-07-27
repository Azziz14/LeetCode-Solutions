class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = 0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                current_product = (nums[i]-1)*(nums[j]-1)
                max_product = max(max_product, current_product)
        return max_product