class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        s = sum(1 for x in nums if x < target)
        r = nums.count(target)
        return list(range(s, s + r))