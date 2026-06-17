class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sort an array containing only 0s, 1s, and 2s in-place using Dutch National Flag algorithm.
      
        Args:
            nums: List of integers containing only 0, 1, and 2
      
        Returns:
            None (modifies the list in-place)
        """
        # Initialize three pointers:
        # left_boundary: rightmost position of 0s section (starts before array)
        # right_boundary: leftmost position of 2s section (starts after array)
        # current: current element being examined
        left_boundary = -1
        right_boundary = len(nums)
        current = 0
      
        # Process elements until current pointer reaches the 2s section
        while current < right_boundary:
            if nums[current] == 0:
                # Move 0 to the left section
                left_boundary += 1
                nums[left_boundary], nums[current] = nums[current], nums[left_boundary]
                # Move current forward since we know the swapped element is processed
                current += 1
            elif nums[current] == 2:
                # Move 2 to the right section
                right_boundary -= 1
                nums[right_boundary], nums[current] = nums[current], nums[right_boundary]
                # Don't increment current as the swapped element needs to be examined
            else:
                # Element is 1, leave it in the middle section
                current += 1