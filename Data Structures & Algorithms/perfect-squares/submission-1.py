class Solution:
    def numSquares(self, n: int) -> int:
        
        # i
        # an integer n
        # the least number of perfect square numbers
        # that sum to n
        # a perfect square is an integer that is a square of an integer
        # 1-4-9-16

        # o
        # The least number of perfect square numbers
        # that sum to n

        # c
        # n >= 1 <= 10^4

        # e
        # 

        mem = {
            1 : 1,
            2 : 2
        }

        def least_number(num, l):
            nonlocal mem
            if num in mem:
                return mem[num]

            if num == 1:
                # least number of square
                return 1

            if num == 0:
                # given value 0
                # the least number of square is 0
                return 0

            # get the square root of num
            # we can get the maximum square number that <= num
            max_perfect = math.isqrt(num)

            candidates = []

            for i in range(max_perfect, 0, -1):
                # from the maximum perfect
                square = i ** 2
                # recursive call
                # least number of perfect squares
                candidates.append(least_number(num - square, l + 1))

            # least number perfect square = _ + 1 (we have use the square)
            mem[num] = min(candidates) + 1
            return mem[num]

        return least_number(n, 0)