class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n : int = len(nums)
        result : list[list[int]] = []

        nums.sort()

        dup : set = set()

        # sol2
        # because the first solution, choose the
        # middle one, the left set and right set are added
        # then we need (a, b) to prevent duplicate
        # What if we choose the first a and search for b and c
        for i in range (n - 2):

            if i >= 1 and nums[i] == nums[i - 1]:
                # same a -> the first a did the search
                continue
            left : int = i + 1
            right : int = n - 1

            target : int = - nums[i]
            while left < right:
                s = nums[left] + nums[right]

                if s == target:

                    result += [[nums[i], nums[left], nums[right]]]
                    # shift to prevent duplicates
                    while left < n - 2 and nums[left] == nums[left + 1]:
                        left += 1
                    
                    while right >= 1 and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1


                elif s < target:
                    left += 1
                else:
                    right -= 1
        
        return result


        # exclude the last one
        # sol1
        # for i in range (1, n - 1):
        #     # set 2 trains
        #     left = 0
        #     right = n - 1

        #     target = - nums[i]

        #     while left < i and right > i:
        #         sum = nums[left] + nums[right]

        #         if sum == target:
        #             # found

        #             # check for duplicate
        #             if (nums[left], nums[i]) in dup:
        #                 None
        #             else:
        #                 result += [[nums[left], nums[i], nums[right]]]
        #                 dup.add((nums[left], nums[i]))

        #             left += 1
        #             right -= 1
                
        #         elif sum > target:
        #             right -= 1
        #         else:
        #             left += 1

        return result