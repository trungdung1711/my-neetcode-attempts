class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # input
        # mxn integer matrix
        # each row sorted in non-decreasing order
        # first integer of each row is greater than the last
        # integer of the previous row
        # non-decreasing order -> row -> column
        
        # output
        # true if target is in matrix
        # false otherwise

        # constraints
        # O(log(m * n))
        # m = len(matrix) == row
        # n = len(matrix[i]) == column
        # m, n >= 1 <= 100
        # matrix[i][j] >= -10^4 <= 10^4

        # edge cases
        # [[3]] - 1x1 matrix
        # [[1, 2, 3, 4]] 1xn matrix

        left = 0
        right = len(matrix) - 1

        while left <= right:

            middle = (left + right) // 2

            if matrix[middle][0] == target:
                return True

            elif matrix[middle][0] < target:
                left = middle + 1

            else:
                right = middle - 1

        # start finding from left
        left_row = 0
        right_row = len(matrix[0]) - 1

        left = left - 1

        while left_row <= right_row:

            middle = (left_row + right_row) // 2

            if matrix[left][middle] == target:
                return True

            elif matrix[left][middle] > target:
                right_row = middle - 1

            else:
                left_row = middle + 1

        return False