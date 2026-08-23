class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candid = nums[0]
        count = 0

        for i in nums:
            if candid == i:
                count += 1
            else:
                count -= 1

                if count < 0:
                    candid = i
                    count = 1

        return candid