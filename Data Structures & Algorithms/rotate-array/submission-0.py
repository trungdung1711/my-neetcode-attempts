class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # i
        # int array nums
        # rotate to the right by k steps
        # k non-negative

        # o
        # array rotated to the right
        # by k steps
        # modify the array in-place

        # c
        # len(nums) >= 1 <= 10^5
        # nums[i] >= -2^31 <= 2^31 - 1
        # k >= 0 <= 10^5

        # e
        # k == 0 -> don't modify at all
        # k == len(nums) -> don't modify at all
        # k > len(nums) -> k % len(nums)

        steps = k % len(nums)

        if steps == 0:
            return None

        else:
            # reverse the array
            nums.reverse()

            p1 = 0
            p2 = steps - 1

            n1 = steps
            n2 = len(nums) - 1

            while p1 < p2:
                temp = nums[p1]

                nums[p1] = nums[p2]
                nums[p2] = temp
                p1 += 1
                p2 -= 1

            while n1 < n2:
                temp = nums[n1]

                nums[n1] = nums[n2]
                nums[n2] = temp
                n1 += 1
                n2 -= 1