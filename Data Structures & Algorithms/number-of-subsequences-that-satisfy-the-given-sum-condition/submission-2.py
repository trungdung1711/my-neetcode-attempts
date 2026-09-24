class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:
        
        # i
        # an array of integers nums and an int target

        # o
        # non-emtpy subsequences of nums
        # the sum of the min and max on it
        # <= target
        # return x % 10^9 + 7

        # c
        # len(nums) >= 1 <= 10^5
        # nums[i] >= 1 <= 10^6
        # target >= 1 <= 10^6

        # e
        # len(nums) == 1 -> return that value

        # idea
        # the brute force approach
        # for every i, check for every element behind it
        # O(N^2)
        # it is not finding the lonest subarray -> expanding?
        # number of subsequences
        # 6 + 5 + 4 + 3 + 2 + 1 -> subarray
        # subsequence allows us to skip element when creating

        # 1. Use DFS to search for the sequences that satisfy
        # the condition?
        # but this is time exceeding problem

        # 2. Think about sorting -> min and max
        # and then if min + max < target -> check for elements inside that

        # res = 0

        # def dfs(index, mi, ma, l):
        #     nonlocal res
        #     # each index, we have two choices
            
        #     # choose contain or not contain
            
        #     # check condition
        #     if index >= len(nums):
        #         return

        #     if l == 0:
        #         # empty subsequence
        #         None
            
        #     elif l >= 1:
        #         # check the condition
        #         if mi + ma <= target:
        #             res += 1

        #     # choose
        #     # 1. include
        #     dfs(index + 1, min(mi, nums[index]), max(ma, nums[index]), l + 1)

        #     # 2. not include
        #     dfs(index + 1, mi, ma, l)

        # dfs(0, float("inf"), -float("inf"), 0)

        # return res % (10^9 + 7)

        # nums = sorted(nums)

        # a = 0
        # b = len(nums) - 1

        # # 0 1 2 3 4 5 -> elements inside = b - a - 1

        # res = 0

        # while a <= b:

        #     if nums[a] + nums[b] <= target:
        #         if a == b:
        #             res += 1
        #         else:
        #             # [0 1 2 3 4 5]
        #             res += 2 ** (b - a - 1)

        #         # after that, we could move a
        #         a += 1

        #     else:
        #         # sum > target
        #         # reduce
        #         b -= 1

        # return res % (10**9 + 7)

        nums = sorted(nums)

        res = 0
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):

                if nums[i] + nums[j] <= target:
                    if i == j:
                        res += 1

                    else:
                        res += 2 ** (-i + j - 1)

        return res % (10**9 + 7)