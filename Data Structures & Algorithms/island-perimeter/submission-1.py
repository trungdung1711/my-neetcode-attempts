class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # input
        # a grid of row x col
        # where
        # grid[j][j] == 1 -> land
        # grid[i][j] == 0 -> water
        # only one island

        # output
        # define the island perimeter

        # constraints
        # row = grid.length
        # col = grid[i].length
        # row, col >= 1 <= 100
        # values of grid[i][j] = {0, 1}

        # edge cases

        m = len(grid)
        n = len(grid[0])

        def four_directions(point):
            a, b = point
            return [
                (a + 1, b),
                (a, b + 1),
                (a - 1, b),
                (a, b - 1)
            ]

        def check(point):
            a, b = point
            if a >= m or b >= n or a < 0 or b < 0:
                return 0

            return grid[a][b]

        res = 0

        for i in range(m):
            for j in range(n):
                if check((i, j)) == 1:
                    # check 4 directions

                    for d in four_directions((i, j)):
                        if check(d) == 0:
                            res += 1

        return res