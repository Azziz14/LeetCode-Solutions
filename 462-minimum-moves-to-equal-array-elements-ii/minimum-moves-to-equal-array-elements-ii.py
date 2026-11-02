class Solution:

  def minMoves2(self, nums: list[int]) -> int:
    # Sort the array to easily find the median
    nums.sort()

    # The optimal number to make all elements equal to is the median.
    # For an array of size n, the median is at index n // 2.
    median = nums[len(nums) // 2]

    # Calculate the total absolute difference between each element and the median
    moves = 0
    for num in nums:
      moves += abs(num - median)

    return moves