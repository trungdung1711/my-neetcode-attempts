class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        # i
        # nums -> can contain duplicates

        # o
        # the power set
        # the solution must not contain duplicate subset


        # c
        # len(nums) >= 1 <= 10
        # nums[i] >= -10 <= 10

        # e
        # len(nums) = 1 -> [] and [value]

        freq = [0 for i in range(0, 21)]

        # calculate for frequency
        for num in nums:
            value = num
            index = value + 10
            freq[index] += 1

        res = []

        def searching(f, n, i, curr):
            nonlocal res
            if n == 0:
                # found
                res.append(curr)

            else:
                # n > 0
                for j in range(i, len(f)):
                    # continue to add i
                    if f[j] > 0:
                        # we have the value
                        temp = f.copy()
                        temp[j] -= 1

                        value = j - 10

                        searching(temp, n - 1, j, curr + [value])


                    elif f[j] == 0:
                        # no value to form the subset
                        # skip that value
                        continue

        for i in range(1, len(nums) + 1):
            searching(freq, i, 0, [])
        
        res.append([])

        return res