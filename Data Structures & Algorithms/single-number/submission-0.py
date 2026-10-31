class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # i
        # non-empty array of integers
        # nums
        # every elements appears twice except for one
        # find that single number

        # o
        # return the number that appears only once
        # in the array

        # c
        # len(nums) >= 1 <= 3*10^4
        # nums[i] >= -3*10^4 <= 3*10^4
        # TC: O(N)
        # SC: O(1)

        # e
        # len(nums) == 1 -> return

        if len(nums) == 1:
            return nums[0]

        res = 0

        for num in nums:
            res ^= num

        return res