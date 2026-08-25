class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        # i
        # 2 pairs -> (a * b) - (c + d)

        # o
        # choose 4 distinct indices
        # produce difference is maximized

        # c
        # len(nums) >= 4 <= 10^4
        # nums[i] >= 1 <= 10^4

        # e
        # len(nums) == 4
        # choose 4

        # max_1 * max_2 - (min_1 + min_2)

        nums = sorted(nums)

        return nums[len(nums) - 1] * nums[len(nums) - 2] - (nums[0] * nums[1])