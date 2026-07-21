class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        # input
        # peak element
        # strictly greater than its neighbours
        # nums int array
        # find a peak element and return its index
        # multiple peaks -> any of it
        # nums[-1] = nums[n] = -inf
        # run in O(logn)

        # output
        # return the peak element's index

        # constraints
        # len(nums) >= 1 <= 1000
        # nums[i] >= -2^31 <= 2^31-1
        # nums[i] != nums[i+1] for all valid i

        # edge cases
        # len(nums) == 1 [5] -> return that peak

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            l = nums[mid - 1] if mid - 1 >= 0 else -float("inf")
            r = nums[mid + 1] if mid + 1 < len(nums) else -float("inf")

            if nums[mid] > l and nums[mid] < r:
                left = mid + 1

            elif nums[mid] > r or nums[mid] < l:
                right = mid - 1

        return right + 1
