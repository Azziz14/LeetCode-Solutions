class Solution:
    def findMissingElements(self, nums):
        s = set(nums)
        start = min(nums)
        end = max(nums)

        return [x for x in range(start, end + 1) if x not in s]
