class Solution:
    def numSubseq(self, nums: list[int], target: int) -> int:

        res = 0

        def dfs(index, mi, ma, length):
            nonlocal res

            if index == len(nums):
                return

            # Include nums[index]
            new_mi = min(mi, nums[index])
            new_ma = max(ma, nums[index])

            if new_mi + new_ma <= target:
                res += 1

            dfs(
                index + 1,
                new_mi,
                new_ma,
                length + 1
            )

            # Don't include nums[index]
            dfs(
                index + 1,
                mi,
                ma,
                length
            )

        dfs(0, float("inf"), -float("inf"), 0)

        return res % (10**9 + 7)