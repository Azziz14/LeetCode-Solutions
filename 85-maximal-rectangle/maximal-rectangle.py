class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(heights):
            stack = []
            max_rect = 0

            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]

                    if stack:
                        width = i - stack[-1] - 1
                    else:
                        width = i

                    max_rect = max(max_rect, h * width)

                stack.append(i)

            while stack:
                h = heights[stack.pop()]

                if stack:
                    width = len(heights) - stack[-1] - 1
                else:
                    width = len(heights)

                max_rect = max(max_rect, h * width)

            return max_rect

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == "1":
                    heights[c] += 1
                else:
                    heights[c] = 0

            max_area = max(max_area, largestRectangleArea(heights))

        return max_area