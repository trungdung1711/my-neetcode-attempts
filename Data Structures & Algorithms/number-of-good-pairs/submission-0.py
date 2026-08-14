class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # i
        # nums
        # (i, j) nums[i] == nums[j]
        # and i < j

        # o
        # number of good pairs

        # c
        # len(nums) >= 1 <= 100
        # nums[i] >= 1 <= 100

        # e
        # [1, 1, 1, 1]

        res = 0
        freq = [0 for i in range(0, 101)]
        # 1 -> 100

        for num in nums:

            # count pair
            prev = freq[num]

            if prev > 0:
                # num appears
                res += prev


            freq[num] += 1

        return res