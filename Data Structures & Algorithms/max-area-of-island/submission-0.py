class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # input
        # m x n binary grid
        # island is a group of 1
        # 4 directionally (vertical + horizontal)

        # output
        # maximum area of an island in
        # grid
        # no island return 0

        # constraints
        # m = len(grid)
        # n = len(grid[i])
        # m, n >= 1 <= 50
        # grid[i][j] is either 0 or 1

        # edge cases
        # there is no 1 -> return 0
        # there is all 1 -> return m * n

        m = len(grid)
        n = len(grid[0])

        area = 0
        explored = set()

        def bfs(land):
            nonlocal area

            if land in explored:
                return 0

            else:
                cur_area = 0
                queue = list()
                queue.append(land)
                explored.add(land)

                while len(queue) > 0:
                    first = queue.pop(0)
                    cur_area += 1
                    # explored.add(first)

                    # add possibles
                    i, j = first
                    possibles = [
                        (i + 1, j),
                        (i - 1, j),
                        (i, j + 1),
                        (i, j - 1)
                    ]

                    for u, v in possibles:
                        if u >= m or v >= n:
                            continue

                        elif u < 0 or v < 0:
                            continue

                        elif grid[u][v] == 0:
                            continue

                        elif (u, v) in explored:
                            continue

                        else:
                            # add to the behind
                            queue.append((u, v))
                            explored.add((u, v))


                if cur_area > area:
                    area = cur_area

                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs((i, j))

                elif (i, j) in explored:
                    continue

        return area