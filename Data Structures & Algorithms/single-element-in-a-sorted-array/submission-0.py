class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        # i
        # sorted array, only ints
        # every element appears exactly twice
        # except for one that appears only once

        # o
        # return element which f(element) == 1

        # c
        # O(logn) and O(1) space
        # len(nums) >= 1 <= 10^5
        # nums[i] >= 0 <= 10^5

        # e
        # if there is only one e
        # len(nums) == 1 -> return that
        # len(nums) >= 3

        # sol 1: use the length


        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            # case 1
            if mid - 1 >= 0 and nums[mid - 1] == nums[mid]:
                # case 5 [5] 6 6
                l = right - (mid - 1) + 1

                if l % 2 == 0:
                    # strip the right
                    right = mid - 2

                else:
                    # strip the left
                    left = mid + 1

            elif mid + 1 < len(nums) and nums[mid + 1] == nums[mid]:
                # case [5] 5 6 6

                l = right - mid + 1

                if l % 2 == 0:
                    # strip the right
                    right = mid - 1

                else:
                    # strip the left
                    left = mid + 2

            else:

                return nums[mid]