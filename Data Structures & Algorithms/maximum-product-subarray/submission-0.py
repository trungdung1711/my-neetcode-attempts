class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        # i
        # int array nums

        # o
        # subarray largest product
        # return that product

        # c
        # len(nums) >= 1 <= 2 * 10^4
        # nums[i] >= -10 <= 10
        # product of any subarray fit in 32-bit int

        # e
        # len(nums) == 1 -> return that value
        # subarray contains 0 -> All 0
        # subarray contains 2n negative int -> positive

        res = -float("inf")

        min_val = 1
        max_val = 1

        for i in range(0, len(nums)):
            val = nums[i]

            new_max = max(val, max_val * val, min_val * val)
            new_min = min(val, max_val * val, min_val * val)

            res = max(new_max, res, val)

            min_val = new_min
            max_val = new_max

        return res