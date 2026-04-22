class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # input
        # array sorted and target
        
        # output
        # index -> target is found
        # index -> inserted

        # constraint
        # sorted in ascending order
        # distinct
        # len(nums) >= 1 <= 10^4
        
        # edge case
        
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        # left > right
        return left