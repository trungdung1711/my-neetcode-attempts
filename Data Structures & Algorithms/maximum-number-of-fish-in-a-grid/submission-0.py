class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        # i
        # 0-indexed 2D grid
        # m * n
        # (r, c) 
        # grid[r][c] = 0 -> land
        # water cell containing fish grid[r][c] > 0 <= 0 -> water
        # fisher can start at any water cell (r, c)
        # operations:
        # - catch the fish
        # - move to any adjacent water cell

        # o
        # maximum number of fish the fisher can catch
        # or 0 if no water cell exists

        # e
        # [[0]] -> return 0

        # c
        # m == grid.length == row
        # n == grid[i].length == column
        # m, n >= 1 <= 10
        # grid[i][j] >= 0 <= 10

        m = len(grid)
        n = len(grid[0])
        # 1, 1

        def possibles(i, j):

            candidates = [
                (i, j + 1),
                (i, j - 1),
                (i + 1, j),
                (i - 1, j),
            ]

            res = []

            for a, b in candidates:
                if a < 0 or b < 0 or a >= m or b >= n:
                    continue

                # posible
                if grid[a][b] == 0:
                    continue

                # not land, fish -> move
                res.append((a, b))

            return res

        visited = set()

        def catch_fish(cell):
            nonlocal visited

            i, j = cell

            queue = deque()

            queue.append((i, j))

            fishes = 0

            while queue:

                c1, c2 = queue.pop()

                if (c1, c2) in visited:
                    continue

                if grid[c1][c2] > 0:
                    # fish

                    fishes += grid[c1][c2]

                    visited.add((c1, c2))

                    queue.extend(possibles(c1, c2))

                else:
                    # <= 0
                    continue

            return fishes

        res = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    
                    # might be this line
                    # is not needed, because
                    # we will check it again
                    # inside catch_fish
                    if (i, j) in visited:
                        continue

                    else:
                        f = catch_fish((i, j))

                        res = max(f, res)

        return res