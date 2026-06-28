class Solution:
    def mySqrt(self, x: int) -> int:
        
        # input
        # a non-negative integer x
        
        # output
        # return the square root of x
        # rounded down to the nearest integer

        # constraints
        # don't use any built-in function
        # x >= 0 <= 2^31 - 1

        # edge cases
        # x = 0 -> return 0
        # x = 1 -> return 1
        # x = 2 -> return 1
        # x = 3 -> return 1
        
        # sol 1
        # k = 0

        # while k * k <= x:
        #     k += 1

        # else:
        #     # k * k > x
        #     return k - 1

        # sol 2
        left = 0
        right = (x // 2) + 1

        while left <= right:
            mid = (left + right) // 2

            val = mid * mid

            if val > x:
                right = mid - 1

            elif val < x:
                left = mid + 1

            else:
                return mid

        # left > right
        return right
