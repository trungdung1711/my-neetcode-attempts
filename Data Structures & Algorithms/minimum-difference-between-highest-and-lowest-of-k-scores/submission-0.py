class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        # input
        # nums nums[i] -> score of ith student
        # integer k
        # score of any k students -> d(highest_score, lowest_core) -> minimized
        
        # output
        # min_score

        # constraints
        # k >= 1 <= len(nums) <= 1000
        # nums[i] >= 0 <= 10^5

        # edge cases
        # [10] -> min = 0
        # [1, 2, 3, 4, 5], k = 5

        # sol1
        sorted = nums.sort()

        win_min = nums[0]
        win_max = nums[0]

        # first window [min, max]
        win_min = 0
        win_max = k - 1

        min_dif = nums[win_max] - nums[win_min]

        start = k

        while start < len(nums):
            win_max = start
            win_min = win_max - k + 1

            dif = nums[win_max] - nums[win_min]

            if dif < min_dif:
                min_dif = dif

            start += 1

        return min_dif