class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        
        # i
        # nums of size n, non-negative integers
        # n - 1 operations
        # ith operation -> ith element of nums
        # nums[i] == nums[i + 1]
        # nums[i] = nums[i] * 2
        # nums[i + 1] = 0
        # otherview skip
        # shift aoo 0s to the end of the array

        # o
        # return the array applied operations

        # c
        # len(nums) >= 2 <= 2000
        # nums[i] >= 0 <= 1000

        # e

        for i in range(0, len(nums) - 1):

            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0

        # shifting
        num_0 = 0
        res = []

        for num in nums:
            if num == 0:
                num_0 += 1

            else:
                res.append(num)

        return res + [0] * num_0