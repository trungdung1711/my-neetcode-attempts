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
        # 1. I feel that the idea of this problem
        # is quite like the idea of the place matches to make the square
        # 1. k * sum(each) = sum(nums)
        # 
        # 2.Take the element and fill the bucket

        # s = sum(nums)

        # if s % k != 0:
        #     return False

        # else:
        #     s_each = s / k
        #     # each subset must have the sum to be this value

        #     # state
        #     # current_sum, target_sum, subset, candidates

        #     res = False

        #     def dfs(current_sum, target_sum, subset, candidates):
        #         nonlocal res

        #         if subset == 0:
        #             res = True
        #             return

        #         else:
        #             if current_sum < target_sum:
        #                 # add more element
        #                 for i, element in enumerate(candidates):
        #                     # add element
        #                     candidates.pop(i)
        #                     dfs(current_sum + element, target_sum, subset, candidates)
        #                     candidates

        #             elif current_sum == target_sum:
        #                 # we have created new subset
        #                 dfs(0, target_sum, subset - 1, candidates)

        #             else:
        #                 # current_sum > target_sum
        #                 return

        #     dfs(0, s_each, k, nums)

        #     return res

        # 2. idea
        # there are k buckets
        # each bucket must contain target = s /
        # choose values from the array to fill in the bucket
        # use the buckets list to track the filling
        # use the True/False list to track which element that
        # we have used -- True-can be used, False-Already used

        s = sum(nums)
        if s % k != 0:
            return False

        target = s / k
        candidates = [True for i in range(len(nums))]
        buckets = [0 for i in range(k)]

        res = False

        def dfs(index, buckets, candidates):
            nonlocal res
            # we are working on buckets[index]
            # we have those available elements inside candidates
            if index == k:
                # fill all bucket
                res = True
                return
            
            else:
                # index [0, k - 1]
                for i in range(0, len(candidates)):
                    if candidates[i] == False:
                        continue

                    else:
                        # we can use that value
                        if buckets[index] + nums[i] < target:
                            # choose that element
                            pre_bucket = buckets[index]
                            candidates[i] = False
                            buckets[index] = buckets[index] + nums[i]
                            # recursive call
                            dfs(index, buckets, candidates)
                            # backtracking
                            candidates[i] = True
                            buckets[index] = pre_bucket

                        elif buckets[index] + nums[i] == target:
                            # successfully fill one bucket
                            pre_bucket = buckets[index]
                            candidates[i] = False
                            buckets[index] = buckets[index] + nums[i]
                            # recursive call
                            dfs(index + 1, buckets, candidates)
                            # backtracking
                            candidates[i] = True
                            buckets[index] = pre_bucket

                        else:
                            # buckets[index] + nums[i] > target
                            continue

        dfs(0, buckets, candidates)

        return res