class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        # input
        # num

        # output
        # true if num is a perfect square
        # false otherwise
        # perfect square == integer
        # is a square of an interger
        # the product of some interger with itself

        # constraints
        # num >= 1 <= 2^31 - 1
        # must not use any built-in lib like sqrt

        # edge cases
        # 0 -> out of constraints

        # finding the first int, such that n * n == num
        # False False False False True True True True

        left = 0
        right = (num // 2) + 1

        while left <= right:
            mid = (left + right) // 2

            if mid * mid >= num:
                right = mid - 1

            elif mid * mid < num:
                left = mid + 1

        # left > right
        if (left) ** 2 == num:
            return True

        else:
            return False