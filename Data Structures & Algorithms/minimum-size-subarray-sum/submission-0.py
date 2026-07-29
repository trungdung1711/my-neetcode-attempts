class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # i
        # array of positive int
        # nums and a positive target

        # o
        # minimal length of a subarray
        # whose sum is >= target
        # no such subarray return 0

        # c
        # target >= 1 <= 10^9
        # len(nums) >= 1 <= 10^5
        # nums[i] >= 1 <= 10^4

        # e
        # len(nums) == 1, check whether nums[0] >= target -> return
        # else 0

        # remember that we need a way to reuse the information of the window
        left = 0
        right = 0
        sum = 0

        # always 0
        res = float("inf")

        while left <= right and right <= len(nums):

            if sum >= target:
                # record
                res = right - left if (right - left) < res else res

                # shrink
                sum -= nums[left]
                left += 1

            else:
            # sum < target
                # still < target
                # expand
                if right == len(nums):
                    break
                else:
                    
                    right += 1
                    sum += nums[right - 1]



        return res if res != float("inf") else 0