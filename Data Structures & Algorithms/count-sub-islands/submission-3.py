from collections import deque

class Solution:
    def countSubIslands(self, grid1, grid2):

        m = len(grid1)
        n = len(grid1[0])

        visited = set()

        def is_valid(i, j, grid):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False

            return grid[i][j] == 1

        def bfs(i, j):

            if (i, j) in visited or grid2[i][j] == 0:
                return False

            queue = deque()
            queue.append((i, j))

            is_sub = True

            while queue:

                a, b = queue.popleft()

                if (a, b) in visited:
                    continue

                if not is_valid(a, b, grid1):
                    is_sub = False

                visited.add((a, b))

                can = [
                    (a + 1, b),
                    (a - 1, b),
                    (a, b + 1),
                    (a, b - 1)
                ]

                for x, y in can:

                    if is_valid(x, y, grid2) and (x, y) not in visited:
                        queue.append((x, y))

            return is_sub

        res = 0

        for i in range(m):
            for j in range(n):

                if (i, j) not in visited and grid2[i][j] == 1:
                    res += 1 if bfs(i, j) else 0

        return res