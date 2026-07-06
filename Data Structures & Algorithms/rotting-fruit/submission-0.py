class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        # input
        # m x n grid
        # 0 -> empty
        # 1 -> fresh
        # 2 -> rotten
        # every minute, fresh orange
        # adjacent (4 directions) -> become rotten

        # output
        # minimum number of minutes
        # until no cell has
        # a fresh orange
        # impossible -> -1

        # constraints
        # m = len(grid)
        # n = len(grid[i])
        # m, n >= 1 <= 10
        # grid[i][j] belongs {0, 1, 2}

        # edge cases
        # [[1]] -> -1
        m, n = len(grid), len(grid[0])

        def possible_cells(cell):
            x, y = cell
            possibles = [
                (x + 1, y),
                (x - 1, y),
                (x, y + 1),
                (x, y - 1),
            ]

            real_possibles = []

            

            for a, b in possibles:
                if a < 0 or b < 0 or a >= m or b >= n:
                    continue

                elif grid[a][b] == 2:
                    continue

                elif grid[a][b] == 0:
                    continue

                else:
                    # not rotting
                    # if one is affected by one
                    # then after that time
                    # it can't be affected by others
                    real_possibles.append((a, b))
                

            return real_possibles

        queue = []

        # intial cells
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 2:
                    queue.append((i, j))

        times = 0

        while len(queue) > 0:

            num = len(queue)
            new = False

            for i in range(num):
                o = queue.pop(0)

                for a, b in possible_cells(o):
                    grid[a][b] = 2
                    queue.append((a, b))
                    new = True

            if new is True:
                times += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return times