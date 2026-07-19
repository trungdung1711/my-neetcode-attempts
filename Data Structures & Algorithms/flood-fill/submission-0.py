class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        # input
        # image
        # image[i][j] pixel value
        # sr sc color
        # flood fill starting from image[sr][sc]

        # output
        # flood fill
        # -> color
        # same color as the starting pixel
        # directly adjacent -> flood
        # return the image after filling

        # constraints
        # m == image.length
        # n == image[i].length
        # m, n >= 1 <= 50
        # image[i][j] >= 0, color < 2^16
        # sr, sc >= 0 < m, n

        # edge cases
        # [[1]] -> only one -> return
        
        q = deque()
        m = len(image)
        n = len(image[0])

        def adjacent(o):
            i, j = o
            current_color = image[i][j]

            c = [
                (i + 1, j),
                (i - 1, j),
                (i, j + 1),
                (i, j - 1),
            ]

            can = []

            for a, b in c:
                if a < 0 or b < 0 or a >= m or b >= n:
                    continue

                if image[a][b] != current_color:
                    continue

                if image[a][b] == color:
                    continue

                #
                can.append((a, b))

            return can

        q.append((sr, sc))

        while len(q) != 0:

            cur = q.popleft()
            for p in adjacent(cur):
                q.append(p)

            # color it
            image[cur[0]][cur[1]] = color

        return image