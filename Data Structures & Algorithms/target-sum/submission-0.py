class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        
        # i
        # nums
        # target
        # build expression out of nums
        # "+" "-" before each interger in nums
        # contatenate all the intergers

        # o
        # number of different expressions
        # that you can build, evaluates to target

        # c

        # e

        # follow along
        dp = {

        }
        # (index, sum) -> ways

        def finding(index, sum):
            nonlocal dp

            if index >= len(nums):
                if sum == target:
                    return 1

                return 0

            if (index, sum) in dp:
                return dp[(index, sum)]

            res = finding(index + 1, (sum + nums[index])) + finding(index + 1,(sum - nums[index]))

            dp[(index, sum)] = res

            return res

        return finding(0, 0)