class Solution:
    def hammingWeight(self, n: int) -> int:
        
        # i
        # positive integer n
        # number of set bits in its binary representation
        # hamming weigth
        # a set bit -> a bit in the binary representation
        # of a number that has value = 1

        # o
        # return number of set bits

        # c
        # n >= 1 <= 2^31 - 1

        # e

        binary = f"{n:b}"

        res = 0

        for b in binary:
            if b == "1":
                res += 1

        return res