class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        
        # i
        # an array is monotonic
        # if it is either monotone increasing or decreasing
        # for all i <= j nums[i] <= nums[j]
        # for all i <= j nums[i] >= nums[j]
        # given an array nums

        # o
        # true if array is monotonic
        # false otherwise

        # c
        # len(nums) >= 1 <= 10^5
        # nums[i] >= -10^5 <= 10^5

        # e
        # len(arr) == 1 -> True

        if len(nums) == 1:
            return True

        # len(arr) >= 2

        # find the trend
        if nums[0] <= nums[len(nums) - 1]:
            # monotone increasing
            p = 0
            c = 1

            while c <= len(nums) - 1:
                if nums[c] < nums[p]:
                    return False

                p = c
                c += 1

        elif nums[0] >= nums[len(nums) - 1]:
            # monotone decreasing
            p = 0
            c = 1

            while c <= len(nums) - 1:
                if nums[c] > nums[p]:
                    return False

                p = c
                c += 1

        return True