class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # i
        # an array of nums of n int
        # nums[i] [1, n]

        # o
        # return an array of all integers
        # in the range [1, n] thar do not appear in nums

        # c
        # n = len(nums)
        # n >= 1 <= 10^5
        # nums[i] >= 1 <= n

        # e
        # n == 1, [1] -> return []

        s = set([i for i in range(1, len(nums) + 1)])

        for num in nums:
            s.discard(num)

        return list(s)