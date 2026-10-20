import random

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        
        # i
        # nums n unique binary strings each of len n

        # o
        # binary string n that doesn't appear in nums
        # multiple answers -> any of them

        # c
        # len(nums) == n
        # n >= 1 <= 16
        # len(nums[i]) == n
        # nums[i][j] is either '0' or '1'
        # all strings of nums are unique

        # e
        # n = len(nums)
        # appears = set(nums)

        # res = ""

        # def build_value(index, value):
        #     nonlocal res
        #     if index == n - 1:
        #         # final
        #         if value + "0" not in appears:
        #             res = value + "0"
        #             # return res
        #             return

        #         if value + "1" not in appears:
        #             res = value + "1"
        #             # return res
        #             return

        #     build_value(index + 1, value + "0")
        #     build_value(index + 1, value + "1")

        # build_value(0, "")

        # return res

        # n = len(nums)

        # appears = set(nums)

        # while True:

        #     res = ""

        #     for i in range(n):
        #         value = random.randint(0, 1)

        #         res = res + str(value)

        #     if res not in appears:
        #         return res

        # cantor's diagonalization
        n = len(nums)
        res = ""

        for i in range (0, n):
            b = nums[i][i]

            res += "1" if b == "0" else "0"

        return res