class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        threshold = n // 3
        res = []
        
        count = 0
        for i in range(n):
            count += 1
            # If we reached the end of a block of duplicates or the end of the list
            if i == n - 1 or nums[i] != nums[i + 1]:
                if count > threshold:
                    res.append(nums[i])
                count = 0  # Reset for next element group
                
        return res