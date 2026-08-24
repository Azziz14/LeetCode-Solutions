class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left_boundary = -1
        right_boundary = len(nums)
        current = 0
        while current < right_boundary:
            if nums[current] == 0:
                left_boundary += 1
                nums[left_boundary], nums[current] = nums[current], nums[left_boundary]
                current += 1
            elif nums[current] == 2:
                right_boundary -= 1
                nums[right_boundary], nums[current] = nums[current], nums[right_boundary]
            else:
                current += 1