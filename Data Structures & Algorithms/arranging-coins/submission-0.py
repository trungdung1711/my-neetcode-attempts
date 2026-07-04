class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        # input
        # n coins, build a staircase
        # staircase consists of k rows
        # ith row has exactly i coins
        # the last row may be incomplete

        # output
        # n, return number of complete row
        # you will build

        # constraints
        # n >= 1 <= 2^31 - 1

        # edge cases
        # n = 1 return 1
        # n = 2 return 1

        # res = 0

        # sol 1
        def coin_left_at_i(i):
            return n - ((0 + i) * (i - 0 + 1)) / 2

        left = 0
        right = n

        while left <= right:
            mid = (left + right) // 2

            coin = coin_left_at_i(mid)

            if coin == 0:
                return mid

            elif coin > 0:
                left = mid + 1

            elif coin < 0:
                right = mid - 1

        # left > right
        return left - 1

        # sol 2
        # run with O(N)
        # res = 0
        # remain = n
        # i = 0
        # while remain > 0:
        #     res = i
        #     remain -= i
        #     i += 1

        # # remain == 0
        # # remain < 0
        # if remain == 0:
        #     return res

        # elif remain < 0:
        #     return res - 1