class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                max_area = max(max_area, h * width)

            stack.append(i)

        # remaining bars
        while stack:
            h = heights[stack.pop()]

            if stack:
                width = len(heights) - stack[-1] - 1
            else:
                width = len(heights)

            max_area = max(max_area, h * width)

        return max_area