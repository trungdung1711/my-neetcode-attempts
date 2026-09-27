class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        
        # i
        # a binary array nums
        # int goal

        # o
        # number of non-empty
        # subarrays with a sum goal
        # subarray is a contiguous part of the array

        # c
        # len(nums) >= 1 <= 3*10^4
        # nums[i] is either 0 or 1
        # goal >= 0 <= nums[length]

        # e
        # [1, 1, 1], goal = 3 -> return 1
        # [0, 0, 0], goal = 0 -> return 3 + 2 + 1

        # 1. Discard numbers of sub-array
        # continuously expand the window
        # if window == goal -> +1
        # else window invalid -> we have check all subarray start at i
        # now move left -> checking at i + 1
        # 0 -> sum keeping + 1
        # 1 -> loss -> increase right to find subarray start at i + 1
        # notice that we have checked [i + 1, current] -> previous calculation
        # now if the sub-array becomes invalid, then we know that we have check
        # all sub-array starting at i [i--invalid], now left += 1
        # checking for the sub-array starting at i + 1, and we know that
        # the sum is valid
        # 0 -> sum unchanged -> res + 1, because we know that from that
        # new index, we need to move up until the right to get a valid one
        # then we don't need to recompute everything
        # NOTE: when s == goal, and if we expand subarrays until nums[right] == 1
        # then when we shrink the window (0), we won't count the sub-array (valid)
        # when moving right previous -> maximum sub-arrays
        # NOTE: there is one optimization step, store the valid subarrays starting with left
        # and use that to calculate the number of valid subarrays starting at left + 1

        left = 0
        right = 0
        s = nums[left]
        res = 0

        while True:
            if left >= len(nums):
                break

            # current window
            if s < goal:
                # move right to add more element
                # we are finding the valid sub-array
                # starting at left index
                right += 1

                if right >= len(nums):
                    # we can't make any valid sub-array starting
                    # at left
                    break


                else:
                    # update the sum
                    s += nums[right]

            elif s == goal:
                res += 1
                # left - right which is a valid sub-array starting at left
                # then let's check whether we could find more valid sub-array
                # starting at left [left - right]
                # then we need to check remaining valid sub-arrays starting at left
                # [left - right]
                i = right + 1

                while i < len(nums):
                    if nums[i] == 1:
                        break

                    # nums[i] == 0
                    # check valid sub-array starting at left
                    res += 1
                    i += 1

                # then sub-array starting at left is exhausted
                # then let's find valid subarray starting at left + 1

                # current array [0, 0] -> valid
                if left == right:
                    # one value and already valid
                    left += 1
                    right += 1

                    if left >= len(nums):
                        break

                    s = s - nums[left - 1] + nums[right]

                else:
                    s -= nums[left]
                    left += 1


            else:
                # we can reach this case
                # where the current sum

                # s > goal
                # we have found all valid sub-arraya starting at left
                # now let's find valid sub-arrays starting at left + 1
                # reuse the first valid sub-array starting at left for the case of left + 1

                if left == right:
                    left += 1
                    right += 1

                    if left >= len(nums):
                        break

                    s = s - nums[left - 1] + nums[right]

                else:

                    left += 1

                    if left >= len(nums):
                        break
                    
                    s -= nums[left - 1]

        return res