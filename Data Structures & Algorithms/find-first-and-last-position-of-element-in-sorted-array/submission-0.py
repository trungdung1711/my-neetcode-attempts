class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # i
        # an array of int nums
        # sorted in non-decreasing order

        # o
        # find the starting and ending position of a given target value
        # target is not found -> [-1, -1]

        # c
        # O(logn)
        # len(nums) >= 0 <= 10^5
        # nums[i] >= -10^9 <=10^9
        # non-decreasing array nums -> [1, 1, 2, 2, 3, 3]
        # target >= -10^9 <= 10^9

        # e
        # only 1 value -> [same, same]

        # sol 1
        # left = 0
        # right = len(nums) - 1

        # first = -1
        # second = -1

        # while left <= right:

        #     middle = (left + right) // 2

        #     if nums[middle] > target:
        #         right = middle - 1

        #     elif nums[middle] < target:
        #         left = middle + 1

        #     else:
        #         # nums[middle] == target
        #         #  we have found one value
        #         # [[7] 7 7 ]
        #         # [7 [7] 7 ]
        #         # [7 7 [7] ]
        #         # most left and most right

        #         # Case, we can remove left
        #         if 

        # return [first, second]

        # sol 2
        def most_left(nums) -> int:
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            return right + 1 if right + 1 < len(nums) and nums[right + 1] == target else -1

        def most_right(nums) -> int:
            left = 0
            right = len(nums) - 1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1

            return left - 1 if left - 1 >= 0 and nums[left - 1] == target else -1

        return [most_left(nums), most_right(nums)]