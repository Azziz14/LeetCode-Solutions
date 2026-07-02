import heapq

class Solution:
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])

        # Starting health after entering (0,0)
        start = health - grid[0][0]
        if start <= 0:
            return False

        # best[r][c] = max remaining health at this cell
        best = [[-1] * n for _ in range(m)]
        best[0][0] = start

        # Max heap (Python has min heap, so store negative)
        heap = [(-start, 0, 0)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while heap:
            cur_health, r, c = heapq.heappop(heap)
            cur_health = -cur_health

            # Reached destination
            if r == m - 1 and c == n - 1:
                return True

            # Skip old weaker states
            if cur_health < best[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    new_health = cur_health - grid[nr][nc]

                    if new_health > 0 and new_health > best[nr][nc]:
                        best[nr][nc] = new_health
                        heapq.heappush(heap, (-new_health, nr, nc))

        return False