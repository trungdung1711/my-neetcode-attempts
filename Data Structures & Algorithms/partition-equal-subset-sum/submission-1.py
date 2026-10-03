class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        # i
        # int array nums

        # o
        # true if you can partition the array
        # into two subsets, such that sum of the elements in both
        # subsets is equal or false otherwise

        # c
        # len(nums) >= 1 <= 200
        # nums[i] >= 1 <= 100

        # e
        # len(nums) == 1 -> return False

        # 1.
        if len(nums) <= 1:
            return False

        s = sum(nums)

        if s % 2 != 0:
            return False

        target = s / 2
        res = False

        def generate(nums, index, s):
            nonlocal res

            if s == target:
                res = True
                # found
                return

            if s > target:
                # add or not add
                return

            if index >= len(nums):
                return
            
            # 2 options
            # include index
            generate(nums, index + 1, s + nums[index])
            # not include index
            generate(nums, index + 1, s)

        generate(nums, 0, 0)
        return res