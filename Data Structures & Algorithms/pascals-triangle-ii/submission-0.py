class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        
        # i
        # rowIndex -> return rowIndex (0-indexed)
        # of the Pascal's triangle

        # o
        # return rowIndex (0-indexed) of the Pascal's triangle

        # c
        # rowIndex >= 0 <= 33

        # e
        # index == 0 -> [1]
        # index == 1 -> [1, 1]

        if rowIndex == 0:
            return [1]

        triangle = [[1]]
        for i in range(1, rowIndex + 1):

            # build the i index
            prev = triangle[i - 1]

            len_i = len(prev) + 1
            arr = []
            for j in range(0, len_i):
                if j == 0 or j == len_i - 1:
                    arr.append(1)

                else:
                    arr.append(prev[j-1] + prev[j])

            triangle.append(arr)

        return triangle[rowIndex]                    