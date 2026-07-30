class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # i
        # a binary array nums

        # o
        # maximum number of consecutive 1

        # c
        # len(nums) >= 1 <= 10^5
        # nums[i] = {0, 1}

        # e
        # len(nums) == 1 -> return 1
        max = float("-inf")
        l = 0
        for num in nums:
            if num == 1:
                # expand
                l += 1
                # update
                max = l if l > max else max

            else:
                # shrink
                l = 0

        return max if max != float("-inf") else 0