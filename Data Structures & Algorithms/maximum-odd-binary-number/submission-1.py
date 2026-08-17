class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        # i
        # a binary string contains at least one '1'
        # rearrange the bit

        # o
        # so that maximum odd binary number
        # that can be created from the string
        # the resulted string can have leading 0s

        # c
        # len(s) >= 1 <= 100
        # s[0] = {'0', '1'}
        # s contains at least one '1' ->

        # e
        # one '1' -> ... 32 16 8 4 2 1 -> return 1

        # an odd number if created by adding odd + even
        # then to create the maximum odd
        # move one '1' to the first place (n - 1)
        # and move all '1' to the end place (0 -->)

        n = len(s)
        first = n - 1
        flag = True
        last = 0

        arr = ['0' for i in range(n)]

        for b in s:
            if b == '1' and flag:
                arr[n - 1] = '1'
                flag = False

            elif b == '1' and not flag:
                arr[last] = '1'
                last += 1

        return "".join(arr)
