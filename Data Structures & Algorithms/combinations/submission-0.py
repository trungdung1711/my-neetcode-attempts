class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        # input
        # n and k int
        # combinations of
        # k numbers
        # from range [1, n]

        # output
        # combination
        # of k numbers
        # choosing from [1, n]

        # constraints
        # n >= 1 <= 20
        # n >= k >= 1

        # edge cases
        # n == k == 1-> return [[1]]
        res = []

        def backtracking(num, tem, left):
            if left == 0:
                res.append(tem)
                return

            # left > 0
            for number in range(num, n + 1):
                # choose one
                backtracking(number + 1, tem + [number], left - 1)
                # backtracking
        
        backtracking(1, [], left=k)

        return res