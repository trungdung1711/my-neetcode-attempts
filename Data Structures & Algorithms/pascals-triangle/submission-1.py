class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        # i
        # numRows

        # o
        # return the first numRows
        # of the Pascal's triangle

        # c
        # numsRow >= 1 <= 30

        # e
        # numRows == 1 -> return [[1]]

        res = []
        for i in range(numRows):

            if i == 0:
                res.append([1])

            else:
                cur = []

                prev = res[i - 1]

                for j in range(len(prev) + 1):
                    if j == 0 or j == len(prev):
                        cur.append(1)

                    else:
                        cur.append(prev[j - 1] + prev[j])

                res.append(cur)

        return res