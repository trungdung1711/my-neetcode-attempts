class Solution:
    def canPartitionKSubsets(self, nums: list[int], k: int) -> bool:
        
        # i
        # int array nums
        # k

        # o
        # true if it is possible to divide
        # array into k non-empty subset
        # whose sums are all equal

        # c
        # k >= 1 <= len(nums)
        # nums[i] >= 1 <= 10^4
        # frequency of each element in the range
        # [1, 4]

        # e
        # k = 1 -> one subset = the whole set == sum
        # k = len(nums) -> each value is a subset -> one value [1, 1, 1, 1...]

        # idea
        # I feel that the idea of this problem
        # is quite like the idea of the place matches to make the square
        # 1. k * sum(each) = sum(nums)

        s = sum(nums)

        if s % k != 0:
            return False

        else:
            s_each = s / k
            # each subset must have the sum to be this value

            # state
            # current_sum, target_sum, subset, candidates

            res = False

            def dfs(current_sum, target_sum, subset, candidates):
                nonlocal res
                
                if subset == 0:
                    res = True
                    return

                else:
                    if current_sum < target_sum:
                        # add more element
                        for i, element in enumerate(candidates):
                            # add element
                            new_candidates = candidates.copy()
                            new_candidates.pop(i)
                            dfs(current_sum + element, target_sum, subset, new_candidates)

                    elif current_sum == target_sum:
                        # we have created new subset
                        dfs(0, target_sum, subset - 1, candidates)

                    else:
                        # current_sum > target_sum
                        return

            dfs(0, s_each, k, nums)

            return res