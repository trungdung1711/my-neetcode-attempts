class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        
        # i
        # 0-indexed int array nums (even length)
        # an equal number of positive and negative ints

        # o
        # return the new array of nums
        # such that
        # - every consecutive pair -> opposite signs
        # - all ints with the same sign, order is the same as
        # the order in nums
        # the re-arranged array begins with a positive int

        # c
        # len(nums) >= 2 <= 2*10^5
        # len(nums) % 2 == 0
        # abs(nums[i]) >= 1 <= 10^5
        # len(nums > 0) == len(nums < 0)
        # not required to do the modification in-place

        # e
        # [-1, 1] -> [1, -1]

        pos = 0
        neg = 0
        res = []

        while nums[pos] < 0:
            pos += 1

        while nums[neg] > 0:
            neg += 1

        while pos < len(nums) and neg < len(nums):
            # add values
            res.append(nums[pos])
            res.append(nums[neg])

            # find the next pos and neg
            pos += 1
            neg += 1

            # find the next positive number
            while pos < len(nums) and nums[pos] < 0:
                pos += 1

            # find the next negative number
            while neg < len(nums) and nums[neg] > 0:
                neg += 1

        return res