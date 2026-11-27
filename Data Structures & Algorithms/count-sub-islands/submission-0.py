class Solution:
    def countSubIslands(self, grid1: list[list[int]], grid2: list[list[int]]) -> int:
        
        # i
        # m * n binary matrices
        # grid1 and grid2
        # 0 -> water
        # 1 -> land
        # island groups of 1 connected 4-directionally
        # cell outside -> water
        # island in grid2 is a sub-island if there is
        # an island in grid1 contains all cells -> make up this island

        # o
        # number of islands in grid2 -> sub-islands

        # c
        # m = len(grid1) = len(grid2)
        # n = len(grid1[i]) = len(grid2[i])
        # m, n >= 1 <= 500
        # grid1[i][j] and grid2[i][j] are either 0 or 1

        # e

        # BFS on the land -> acoording land -> land -> subland
        # water -> stop

        m = len(grid1)
        n = len(grid1[0])

        visited = set()

        def is_valid(i, j, grid):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False

            else:
                if grid[i][j] == 1:
                    return True

                else:
                    return False

        def bfs(i, j):

            nonlocal visited

            if (i, j) in visited:
                return False

            queue = deque()

            queue.appendleft((i, j))

            is_sub = True

            while queue:

                # check land
                a, b = queue.pop()
                
                if not is_valid(a, b, grid1):
                    is_sub = False

                # visited
                visited.add((a, b))

                can = [
                    (a + 1, b),
                    (a - 1, b),
                    (a, b + 1),
                    (a, b - 1)
                ]

                for c in can:
                    m, n = c

                    if is_valid(m, n, grid2) and (m, n) not in visited:
                        queue.appendleft((m, n))

            return is_sub

        res = 0

        for i in range(m):
            for j in range(n):

                if (i, j) not in visited and grid2[i][j] != 0:
                    res += 1 if bfs(i, j) else 0

        return res