class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # input
        # nums
        # move all 0
        # to the end
        # while maintaining
        # the relative order
        # of the non-zero elements

        # output
        # move all 0 to the end
        # maintaining the relative order
        # of non-zero elements

        # constraints
        # len(nums) >= 1 <= 10^4

        # edge cases

        # sol1

        num_0 = 0

        for i in range(len(nums)):
            if nums[0] == 0:
                nums.pop(0)
                num_0 += 1
                
            else:
                # not 0
                value = nums[0]
                nums.pop(0)
                nums += [value]

        nums += [0] * num_0