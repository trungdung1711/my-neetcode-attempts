class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # i
        # an array of len(n)
        # sorted in ascending order
        # rotated between 1 and n times
        # n times -> the same
        # 1 times -> move to the right side
        # sorted, rotated array nums of unique element

        # o
        # return the minimum element of this array

        # c
        # n == len(nums)
        # n >= 1 <= 5000
        # nums[i] >= -5000 <= 5000
        # ints are unique
        # sorted and rotated between 1 and n

        # e
        # rotated 1 times -> move right 1 times (min is 1)
        # rotated n times -> move right n times -> min is 0 (same array)
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                # right side normally sorted
                r = m

            elif nums[m] > nums[r]:
                # pattern = up -> down -> up (again)
                l = m + 1
            
            elif l + 1 == r:
                return nums[l]

            elif l == r:
                return nums[l]