class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # input: nums and k
        # output: nums[i] == nums[j] and abs(i, j) <= k -> true
        # else false

        # constraint
        # len(nums) >= 1

        # edge case
        # [1] -> false
        # k can't be 0

        if k == 0:
            return False

        n = len(nums)
        
        for i in range (1, k + 1):
            # loop of possible k values
            for j in range (0, n - i):
                if nums[j] == nums[j + i]:
                    return True
        
        return False