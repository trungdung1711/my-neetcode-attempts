# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # input
        # a number from 1 to n
        
        # output
        # use the guess_api and return that number

        # constraint
        # n >= 1
        # pick >= 1 <= n

        # edge case
        
        left = 1
        right = n

        while left <= right:
            i_guess = (left + right) // 2
            res = guess(i_guess)

            if res == 0:
                return i_guess
            elif res == -1:
                right = i_guess - 1
            elif res == 1:
                left = i_guess + 1
            else:
                None