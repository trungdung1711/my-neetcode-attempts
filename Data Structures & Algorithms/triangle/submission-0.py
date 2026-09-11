class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # i
        # triangle array
        # if u are at index i
        # move to either index i or index i + 1 of the next row

        # o
        # minimum path sum from top to bottom

        # c
        # len(triangle) >= 1 <= 200
        # len(triangle[0]) == 1
        # len(trianle[i]) = len(triangle[i-1]) + 1
        # triangle[i][j] >= -10^4 <= 10^4

        # e
        # len(triangle) = 1 -> return triangle[0][0]

        mem = {

        }

        def min_path_sum(layer, index):
            nonlocal mem
            # what is the min path sum from this index

            # base case
            if (layer, index) in mem:
                return mem[(layer, index)]
            
            # base case
            if layer == len(triangle) - 1:
                return triangle[layer][index]

            value = triangle[layer][index]

            possibles = [(layer + 1, index), (layer + 1, index + 1)]

            v1 = min_path_sum(*possibles[0])
            v2 = min_path_sum(*possibles[1])

            res = min(v1, v2) + value

            mem[(layer, index)] = res

            return res

        return min_path_sum(0, 0)