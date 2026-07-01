from collections import deque
from math import inf

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)

        # Step 1: Multi-source BFS to find nearest thief distance
        dist = [[inf] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n:
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))

        # Step 2: Check if path exists with safeness >= val
        def can_reach(val):
            if dist[0][0] < val:
                return False

            q = deque([(0, 0)])
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True

            while q:
                x, y = q.popleft()

                if x == n - 1 and y == n - 1:
                    return True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < n and 0 <= ny < n and
                        not visited[nx][ny] and
                        dist[nx][ny] >= val):

                        visited[nx][ny] = True
                        q.append((nx, ny))

            return False

        # Step 3: Binary search on safeness factor
        left, right = 0, 2 * n
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if can_reach(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
        