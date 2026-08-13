class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        # i
        # one element if each pair must be
        # even and the other must be odd
        # given nums

        # o
        # true nums is special array
        # false otherwise

        # c
        # len(nums) >= 1 <=100
        # nums[i] >= 1 <= 100

        # e
        # len(nums) == 1 -> return True
        # 2 -> pain 1
        # 3 -> pair 2

        if len(nums) == 1:
            return True

        for i in range(0, len(nums) - 1):

            # one must be odd
            # the other must be even
            # odd + even = odd
            # even + even = even
            # odd + odd -> even
            if (nums[i] + nums[i + 1]) % 2 != 1:
                return False

        return True