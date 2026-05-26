class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # input
        # m x n grid
        # 1 == land
        # 0 == water
        # island is formed by connecting adjacent lands
        # horizontally or vertically
        # 4 edges are surrounded by water

        # output
        # number of islands

        # constraints
        # m, n >= 1 <= 300
        # grid[i][j] == '0' or '1'

        # edge cases
        # dot -> islands
        # all -> only 1 island

        self.num = 0

        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.bfs(grid, (i, j))

                elif grid[i][j] == "0":
                    continue

                elif grid[i][j] == "x":
                    continue

        return self.num

    def bfs(self, grid, location):
        self.num += 1

        i, j = location
        stack = []

        stack.append(location)

        grid[i][j] = "x"

        while len(stack) > 0:
            current_location = stack.pop()
            c, d = current_location
            grid[c][d] = "x"

            for a, b in self.next_locations(grid, current_location):
                stack.append((a, b))
                grid[a][b] = "x"


    def next_locations(self, grid, location):
        i, j = location
        m = len(grid)
        n = len(grid[0])

        possibles = [
            (i + 1, j),
            (i, j + 1),
            (i - 1, j),
            (i, j - 1),
        ]

        possibles_v2 = [

        ]

        for a, b in possibles:
            if a < 0 or a >= m or b < 0 or b >= n:
                continue

            elif grid[a][b] == "0":
                continue

            elif grid[a][b] == "x":
                continue

            else:
                # == "1"
                possibles_v2.append((a, b))

        return possibles_v2