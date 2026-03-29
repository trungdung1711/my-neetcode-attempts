class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n : int = len(nums)
        result : list[list[int]] = []

        nums.sort()

        dup : set = set()

        # exclude the last one
        for i in range (1, n - 1):
            # set 2 trains
            left = 0
            right = n - 1

            target = - nums[i]

            while left < i and right > i:
                sum = nums[left] + nums[right]

                if sum == target:
                    # found

                    # check for duplicate
                    if (nums[left], nums[i]) in dup:
                        None
                    else:
                        result += [[nums[left], nums[i], nums[right]]]
                        dup.add((nums[left], nums[i]))

                    left += 1
                    right -= 1
                
                elif sum > target:
                    right -= 1
                else:
                    left += 1

        return result