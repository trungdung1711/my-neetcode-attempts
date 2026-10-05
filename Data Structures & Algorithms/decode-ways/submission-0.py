class Solution:
    def numDecodings(self, s: str) -> int:
        
        # i
        # a secret message
        # encoded as a string of numbers
        # "1" -> "A"
        # "26" -> "Z cn"
        # but while decoding
        # many different ways
        # you can decode because 
        # some codes are contained in other codes
        # "2" and "5" in "25"
        # there may be strings that are impossible to decode

        # o
        # return the number of ways to decode it
        # if the entire string cannot be decoded in any valid way, return 0

        # c
        # len(s) >= 1 <= 100
        # s contains only digits and may contain leading 0s

        # e
        # s == "2" -> only 1

        def is_valid(c):
            if c[0] == "0":
                # leading 0
                return False

            n = int(c)

            if n <= 0 or n > 26:
                return False

            return True

        mem = {

        }

        def num_ways(index):
            nonlocal mem

            if s[index:] in mem:
                return mem[s[index:]]

            if index == len(s) - 2:
                # final last
                if is_valid(s[index]):
                    a = num_ways(index + 1)

                else:
                    a = 0

                if is_valid(s[index:index + 2]):
                    b = 1

                else:
                    b = 0

                mem[s[index:]] = a + b

                return a + b

            if index == len(s) - 1:
                # final value
                return 1 if is_valid(s[index]) else 0

            # if index == len(s) - 2:
            #     # final value


            else:
                # find the number of ways of decoding s[index:]

                # at index
                if is_valid(s[index]):
                    a = num_ways(index + 1)

                else:
                    a = 0

                if is_valid(s[index:index + 2]):
                    b = num_ways(index + 2)

                else:
                    b = 0

                mem[s[index:]] = a + b

                return a + b

        return num_ways(0)