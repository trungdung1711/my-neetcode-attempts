class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        
        # i
        # int array nums

        # o
        # true if you can partition the array
        # into two subsets, such that sum of the elements in both
        # subsets is equal or false otherwise

        # c
        # len(nums) >= 1 <= 200
        # nums[i] >= 1 <= 100

        # e
        # len(nums) == 1 -> return False

        # 1.
        if len(nums) <= 1:
            return False

        s = sum(nums)

        if s % 2 != 0:
            return False

        target = s / 2
        # res = False
        mem = {

        }

        def generate(c, index):
            nonlocal mem
            if index >= len(nums):
                if c == target:
                    return True

                else:
                    return False

            if (c, index) in mem:
                # if we already solved this problem
                # if we have the current sum
                # and we are deciding whether
                # the combination should contain this value
                # in this index
                return mem[(c, index)]

            if c == target:
                # then from the node
                # we can just exclude all the onward
                # elements
                # meaning from that current state
                # we can build a subset whose sum is equal to target
                mem[(c, index)] = True
                return True
            
            elif c > target:
                # from that node
                # even if we exclude elements
                # we can't have a combination
                # whose sum == or become less
                # then target
                mem[(c, index)] = False
                return False

            # smaller
            # the result will depend on
            # [1] Include the current
            # [2] Exclude the current
            a = generate(c, index + 1) or generate(c + nums[index], index + 1)
            mem[(c, index)] = a
            return a

        return generate(0, 0)