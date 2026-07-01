class Solution:
    def combine(self, n: int, k: int):
        result = []
        path = []

        def backtrack(start):
            # base case
            if len(path) == k:
                result.append(path[:])   # copy current combination
                return

            # try all numbers from start to n
            for i in range(start, n + 1):
                path.append(i)           # choose
                backtrack(i + 1)        # explore
                path.pop()              # unchoose (backtrack)

        backtrack(1)
        return result