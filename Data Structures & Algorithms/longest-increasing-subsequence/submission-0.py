class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        
        # i
        # nums

        # o
        # longest strictly increasing subsequence

        # c
        # len(nums) >= 1 <= 2500
        # nums[i] >= -10^4 <= 10^4

        # e

        # 1. The longest increasing subsequence starting at index i
        # we know that at an index j, we find that nums[i] > nums[j]
        # 2. Those are overlapping, when we have multiple paths which lead to
        # the same question

        mem = {

        }

        def dfs(index):
            nonlocal mem

            if index in mem:
                return mem[index]

            if index == len(nums) - 1:
                return 1

            # find the next possible values in the sequence

            can = []
            for j in range(index + 1, len(nums)):
                if nums[j] > nums[index]:
                    can.append(1 + dfs(j))

            if len(can) == 0:
                # no value to create an increasing sequence
                mem[index] = 1
                return mem[index]

            else:
                mem[index] = max(can)

            return mem[index]

        
        return max([dfs(i) for i in range(0, len(nums))])