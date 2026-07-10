class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        # input
        # nums containing n + 1 integers
        # nums[i] >= 1 <= n
        # there is only one repeated
        # number in nums

        # output
        # return the repeated number

        # constraints
        # don't modify nums
        # constant extra space
        # n >= 1 <= 10^5
        # len = n + 1
        # nums[i] >= 1 <= n
        # all intergers appear only once
        # one interger that appears two or more times

        # edge cases

        # using the pigeon hole principle
        # because nums[i] >= 1 <= n
        # meaning that we have n holes
        # but we have n + 1
        # then in the worst-case scenario
        # at least one hole contains 2 numbers

        n = len(nums) - 1
        l = n + 1

        # sol 1: O(N^2)
        # for i in range(l):
        #     for j in range(i + 1, l):
        #         if nums[i] == nums[j]:
        #             return nums[i]

        # sol2: 
        # we all know that nums[i] >= 1 nums[i] <= N
        # slow = 0
        # fast = 0

        # # Move the pointers first before comparison
        # while True:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]
        #     if slow == fast:
        #         break

        # # nums[slow] == nums[fast]
        # return nums[slow]

        # sol3: negative?
        res = float("inf")
        for i in range(l):
            index = i
            value = nums[index]

            # mark
            if nums[abs(value)] < 0:
                res = abs(value)

            # else
            nums[abs(value)] *= -1

        for i in range(l):
            nums[i] = abs(nums[i])

        return res