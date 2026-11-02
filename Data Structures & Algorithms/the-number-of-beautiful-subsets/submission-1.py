class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        
        # i
        # nums of positive ints
        # positive int k
        # nums is beautiful
        # doesn't contain 2 ints
        # |i - j| == k

        # o
        # number of non-empty beautiful subsets nums

        # c
        # len(nums) >= 1 <= 18
        # nums[i], k >= 1 <= 1000

        # e
        # len(nums) == 1 -> return {}
        # len(nums) == 2 -> return {}, {}, {} if |i - j| != k

        # observe
        # we want to build the subset
        # such that there is no 2 elements i, j
        # such that |i - j| == k -> add an element to subset -> check

        c = Counter()
        res = 0

        def dfs(index, c):
            nonlocal res
            if index >= len(nums):
                # sucessfully build a beautiful subset
                res += 1
                return

            else:
                # index < len(nums)
                # try to add this nums[index] into subset
                i = k + nums[index]
                j = nums[index] - k

                if i not in c and j not in c:
                    # it is OK to add
                    saved = c.copy()
                    c[nums[index]] += 1
                    dfs(index + 1, c)
                    # backtracking
                    # c[nums[index]] -= 1
                    dfs(index + 1, saved)

                else:
                    # don't add -> skip this path
                    dfs(index + 1, c)

        dfs(0, c)
        return res - 1 # empty set