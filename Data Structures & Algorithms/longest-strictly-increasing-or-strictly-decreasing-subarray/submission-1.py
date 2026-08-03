class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        
        # i
        # an array of intergers nums

        # o
        # return the length of the longest subarray
        # of nums which is either strictly increasing
        # or strictly decreasing

        # c
        # len(nums) >= 1 <= 50
        # nums[i] >= 1 <= 50

        # e
        # only one value -> return that value

        res = 1
        size = 1
        prev = nums[0]

        flag = True # increase

        for i in range(1, len(nums)):
            if nums[i] > prev:
                if flag is True:
                    # continue increasing
                    flag = True
                    size += 1
                    res = max(res, size)

                else:
                    # it is decreasing
                    flag = True
                    size = 2
                    res = max(res, size)


            elif nums[i] < prev:
                # decrease
                if flag is False:
                    # continue decreasing
                    flag = False
                    size += 1
                    res = max(res, size)

                else:
                    # it is increasing
                    flag = True
                    size = 2
                    res = max(res, size)

            else:
                # nums[i] == prev
                flag = True
                size = 1
                res = max(res, size)

            prev = nums[i]


        return res