class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get dimensions of the matrix
        num_rows, num_cols = len(matrix), len(matrix[0])

        # Initialize binary search boundaries
        # Treat the 2D matrix as a flattened 1D array
        left, right = 0, num_rows * num_cols - 1
        first_true_index = -1

        # Binary search using the template: find first index where element >= target
        while left <= right:
            mid = (left + right) // 2

            # Convert 1D index to 2D coordinates
            row, col = divmod(mid, num_cols)

            # Feasible condition: matrix[row][col] >= target
            if matrix[row][col] >= target:
                first_true_index = mid
                right = mid - 1
            else:
                left = mid + 1

        # Check if first_true_index points to the target
        if first_true_index == -1:
            return False
        row, col = divmod(first_true_index, num_cols)
        return matrix[row][col] == target
