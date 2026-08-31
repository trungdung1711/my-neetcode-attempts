class Solution:
    def check(self, nums: List[int]) -> bool:
        
        # i
        # nums
        # sorted in non-decreasing order
        # rotated some number of positions (0)

        # o
        # true if those conditions match
        # false otherwise
        # rotate = move the right to the left

        # c
        # len(nums) >= 1 <= 100
        # nums[i] >= 1 <= 100

        # e
        # len(nums) == 1 -> true
        # dupplicates [1, 2, 2, 2, 4]
        # [5, 5, 5, 5, 5, 5]

        first = nums[0]
        prev = first

        flag = False

        for i in range(1, len(nums)):
            if not flag and nums[i] >= prev:
                prev = nums[i]
                continue

            elif not flag and nums[i] < prev:
                if nums[i] > first:
                    return False
                # decrease
                flag = True
                prev = nums[i]
            
            elif flag:
                if nums[i] > first:
                    return False

                elif nums[i] < prev:
                    return False

                elif nums[i] >= prev:
                    prev = nums[i]

        return True