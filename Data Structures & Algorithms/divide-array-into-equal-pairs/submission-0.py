class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        # i
        # array nums 2 * n
        # divide nums into n pairs
        # each element belongs to exactly one pair
        # the elements present in a pair are equal

        # o
        # true -> divided into n pairs
        # false otherwise

        # c
        # len(nums) == 2 * n
        # n >= 1 <= 500
        # nums[i] >= 1 <= 500

        # e
        # len(nums) == 2
        # [1, 2] -> false
        # [1, 1] -> true

        d = {

        }

        for num in nums:
            d[num] = d[num] + 1 if num in d else 1

        for k, v in d.items():
            if v % 2 == 1:
                return False

        return True