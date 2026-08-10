class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # i
        # array of int nums
        # pivot index = sum (left) == sum(right)
        # index = 0 -> left == 0
        # index = len(nums) - 1 -> right = 0

        # o
        # the pivot index of this array
        # leftmost pivot index
        # if there is no such index -> -1

        # c
        # len(nums) >= 1 <= 10^4
        # nums[i] >= -1000 <= 1000

        # e
        # [1] -> return 0
        # [1, 0] -> return 0

        s = sum(nums)

        index = 0
        left = 0
        right = s - nums[index]

        while index < len(nums):
            # we have left and right
            if left == right:
                return index

            else:
                # not equal
                # update left
                index += 1
                if index >= len(nums):
                    break

                left += nums[index - 1]
                right -= nums[index]

        return -1