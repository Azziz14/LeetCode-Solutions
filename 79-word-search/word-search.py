class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            # whole word found
            if index == len(word):
                return True

            # invalid conditions
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                board[r][c] != word[index]):
                return False

            # mark visited
            temp = board[r][c]
            board[r][c] = "#"

            # explore 4 directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # backtrack (restore)
            board[r][c] = temp

            return found

        # try every starting cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False