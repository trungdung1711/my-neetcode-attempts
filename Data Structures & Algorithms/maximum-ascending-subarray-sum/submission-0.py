class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        
        # i
        # an array of positive integers nums
        # maximum possible sum of a strictly increasing subarray
        # in nums

        # o
        # max possible sum of a strictly increasing subarray

        # c
        # len(nums) >= 1 <= 100
        # nums[i] >= 1 <= 100

        # e
        # [2] -> return 2

        sum = 0
        res = float("-inf")
        prev = float("-inf")

        for num in nums:
            if num > prev:
                # update window
                sum += num
                prev = num

                if sum > res:
                    res = sum


            
            else:
                # window is broken
                sum = num
                prev = num

                if sum > res:
                    res = sum

        return res