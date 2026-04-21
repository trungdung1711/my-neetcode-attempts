class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # input
        # sorted array in ascending order

        # output
        # return the index of target
        i = 0
        j = len(nums) - 1

        # constraints
        # ascending and unique numbers

        # edge cases
        
        while i <= j:
            mid = (i + j) // 2

            # didn't match
            if nums[mid] > target:
                j = mid - 1
            elif nums[mid] < target:
                i = mid + 1
            else:
                return mid

        return -1
